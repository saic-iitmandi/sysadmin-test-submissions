#!/bin/bash

# Function to monitor Docker containers and echo alert on container stop
monitor_containers() {
    echo "Monitoring Docker containers..."

    # Associative array to store previous container states
    declare -A prev_states

    while true; do
        # Get the list of running containers
        current_containers=$(docker ps --format "{{.Names}}: {{.Status}}")

        # Check for changes in container states
        IFS=$'\n'
        for container_info in $current_containers; do
            container_name=$(echo "$container_info" | cut -d ':' -f 1)
            container_status=$(echo "$container_info" | cut -d ':' -f 2)

            # Compare current state with previous state
            prev_status="${prev_states[$container_name]}"
            if [[ "$prev_status" != "$container_status" ]]; then
                # Check if the container has stopped
                if [[ "$container_status" == *"Exited"* ]]; then
                    # Prepare alert content
                    alert_date=$(date +"%Y-%m-%d %H:%M:%S")
                    alert_message="Container '$container_name' stopped at $alert_date. Reason: $container_status"

                    # Echo alert to shell
                    echo "$alert_message"
                fi

                # Update previous state
                prev_states[$container_name]=$container_status
            fi
        done

        # Sleep for a specified interval before checking again (e.g., 60 seconds)
        sleep 60
    done
}

# Start monitoring containers
monitor_containers

