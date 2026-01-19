#!/bin/bash

# Function to log access
log_access() {
    timestamp=$(date +"[%Y-%m-%d %H:%M:%S]")
    log_level="[INFO]"
    http_method="$1"
    path="$2"
    status_code="$3"
    client_ip="$4"
    
    echo "${timestamp} ${log_level} ${http_method} ${path} - Status: ${status_code} - IP: ${client_ip}"
}

# Function to log errors
log_error() {
    timestamp=$(date +"[%Y-%m-%d %H:%M:%S]")
    log_level="[ERROR]"
    error_type="$1"
    error_desc="$2"
    stack_trace="$3"

    echo "${timestamp} ${log_level} ${error_type}: ${error_desc} - Stack Trace: ${stack_trace}"
}

# Log access and error logs for Docker containers
log_docker_logs() {
    # Get all running Docker container IDs
    container_ids=$(docker ps -q)

    # Iterate through each container and get its logs
    for container_id in $container_ids; do
        # Access logs
        docker logs --tail=10 "$container_id" | while read -r line; do
            log_access $line >> access.txt
        done

        # Error logs
        docker logs --tail=10 "$container_id" 2>&1 1>&3 | while read -r line; do
            log_error $line >> errors.txt
        done 3>&1 1>&2
    done
}

# Run the function to log Docker container logs
log_docker_logs
