# Get the path to your PowerShell script
$scriptPath = "C:\Users\Dell\Desktop\backup.ps1"

# Set the time for scheduling (11:55 PM)
$scheduledTime = "23:55"

# Create a new scheduled task
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File $scriptPath"
$trigger = New-ScheduledTaskTrigger -Daily -At $scheduledTime
$task = Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "BackupTask" -Force

Write-Host "Scheduled task created to run the backup script at $scheduledTime daily."
