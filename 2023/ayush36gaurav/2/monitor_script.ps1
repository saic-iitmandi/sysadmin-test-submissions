# Email notification function
function Send-Email {
    param (
        [string]$containerId,
        [string]$containerName,
        [string]$currentState,
        [string]$lastKnownState,
        [string]$programRunning,
        [string]$exitCode
    )

    $subject = "Sysadmin test 2023 - Challenge 2"
    $from = "--Sender's Email--"
    $to = "Receiver's Email"

    $body = @"
Dear Sysadmin,

A container has changed its state from $lastKnownState to $currentState.

Container ID: $containerId
Container Name: $containerName
Program Running: $programRunning
Timestamp: $(Get-Date)
Exit Code: $exitCode

Thank You
Ayush Gaurav
Localhost Server
"@

    $securePassword = ConvertTo-SecureString -String "--App Password--" -AsPlainText -Force
    $credentials = New-Object System.Management.Automation.PSCredential ($from, $securePassword)

    Send-MailMessage -From $from -To $to -Subject $subject -Body $body -SmtpServer "smtp.gmail.com" -Port 587 -UseSsl -Credential $credentials
}

# Hashtable to store previous states
$previousStates = @{}

# Monitor Docker events
docker events --filter event=die --filter event=stop --filter event=start --filter event=restart `
    --format '{{.ID}} {{.Actor.ID}} {{.Actor.Attributes.name}}' | ForEach-Object {
        $eventInfo = $_ -split ' '
        $event_id, $container_id, $container_name = $eventInfo

        # Get information about the container
        $program_running = docker inspect --format '{{.Config.Cmd}}' $container_id
        $exit_code = docker inspect --format '{{.State.ExitCode}}' $container_id

        # Log the event
        Write-Host "Container $container_name ($container_id) has changed state"
        Write-Host "Program Running: $program_running"
        Write-Host "Exit Code: $exit_code"

        # Get the current state of the container
        $currentState = docker inspect -f '{{.State.Status}}' $container_name

        # Check if the container has a previous state
        if ($previousStates.ContainsKey($container_id)) 
        {
            $lastKnownState = $previousStates[$container_id]
        }
        else{$lastKnownState = "Created"}

        # Compare current state with the last known state
        if ($lastKnownState -ne $currentState) {
            # Send email notification
            Send-Email -containerId $container_id -containerName $container_name -currentState $currentState -lastKnownState $lastKnownState -programRunning $program_running -exitCode $exit_code
        }

        # Store the current state as the previous state
        $previousStates[$container_id] = $currentState
    }
