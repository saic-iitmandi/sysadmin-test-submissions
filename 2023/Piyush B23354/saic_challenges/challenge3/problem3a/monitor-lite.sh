#!/bin/bash

# Function to monitor Docker containers and display status
monitor_containers() {
    echo "Monitoring Docker containers..."

    # Associative array to store previous container states
    declare -A prev_states

    while true; do
        # Get the list of all containers
        all_containers=$(docker ps -a --format "{{.Names}}: {{.Status}}")

        # Check for changes in container states
        IFS=$'\n'
        for container_info in $all_containers; do
            container_name=$(echo "$container_info" | cut -d ':' -f 1)
            container_status=$(echo "$container_info" | cut -d ':' -f 2)

            # Compare current state with previous state
            prev_status="${prev_states[$container_name]}"
            if [[ "$prev_status" != "$container_status" ]]; then
                # Update previous state
                prev_states[$container_name]=$container_status

                # Display container status
                echo "Container '$container_name' - Status: $container_status"
            fi
        done

        # Sleep for a specified interval before checking again (e.g., 60 seconds)
        echo "Sleeping for 60 seconds before checking containers again..."
        sleep 60
    done
}

# Start monitoring containers
monitor_containers
