# entrypoint.ps1 (entrypoint script for the Nginx container)

# Read the template content
$templateContent = Get-Content -Raw -Path "/etc/nginx/nginx.conf.template"

# Substitute variables
$nginxConf = $templateContent -replace '\{\{ n_instances \}\}', $env:n_instances

# Write the generated nginx.conf
$nginxConf | Out-File -FilePath "/etc/nginx/nginx.conf"

# Start Nginx
Start-Process "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -NoNewWindow -Wait
