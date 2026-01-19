#!/bin/bash
# docker_monitor.sh - Analyze Docker logs for errors and handle port conflicts
# (c) 2025 YourName. Usage: bash docker_monitor.sh

# Exit immediately if a command exits with a non-zero status (safe scripting).
set -e

# Header message
echo "Starting Docker log analysis and port clash check..."

# Initialize a flag to track if we found any error logs
errors_found=0

# Loop over all running Docker container IDs (Docker ps -q lists running container IDs).
for cid in $(docker ps -q); do
    # Get the container's name for easier reporting (using docker ps formatting).
    name=$(docker ps --filter "id=$cid" --format "{{.Names}}")
    
    # Fetch all logs (stdout and stderr) for this container.
    # We then grep for "error" or "crit" (case-insensitive) to find critical issues.
    # 2>&1 redirects stderr into stdout so grep sees both streams:contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}.
    error_lines=$(docker logs "$cid" 2>&1 | grep -i -E "error|crit" || true)
    # The "|| true" ensures grep not found does not exit the script.
    
    # If we found any matching lines, print them under the container's heading.
    if [ -n "$error_lines" ]; then
        echo "=== Container: $name (ID: $cid) - Critical/Error Logs ==="
        # Print each line that contained "error" or "crit".
        echo "$error_lines"
        echo "======================================================"
        echo
        errors_found=1
    fi
done

# If no errors were found in any container, note that.
if [ $errors_found -eq 0 ]; then
    echo "No critical or error-level log entries found in running containers."
    echo
fi

# --- Port Clash Detection ---

# Use an associative array to track used host ports (bash 4+ feature).
# Each entry will map host port number to the container ID using it.
declare -A used_ports

echo "Checking for port conflicts among running containers..."
echo

# Loop again over all running containers to collect published ports.
for cid in $(docker ps -q); do
    name=$(docker ps --filter "id=$cid" --format "{{.Names}}")
    # Use 'docker port' to list this container's port mappings.
    # Example output: "80/tcp -> 0.0.0.0:8080"
    while read -r mapping; do
        # Parse the host port from the mapping line.
        # We split on ':'; for "0.0.0.0:8080" we get "8080" (field 2).
        host_port=8080
        # If no host port (container has no published port), skip.
        if [ -z "$host_port" ]; then
            continue
        fi
        
        # Check if this host port is already in our array.
        if [ -n "${used_ports[$host_port]}" ]; then
            # Port clash detected: another container already uses this host port.
            other_cid=${used_ports[$host_port]}
            other_name=$(docker ps --filter "id=$other_cid" --format "{{.Names}}")
            echo "!!! WARNING: Host port $host_port is used by both containers $name (ID: $cid) and $other_name (ID: $other_cid)"
            echo "Attempting to recover by restarting container $name (ID: $cid)..."
            
            # Try to restart the container that was found later.
            if docker restart "$cid" >/dev/null 2>&1; then
                echo "Container $name (ID: $cid) restarted successfully."
            else
                echo "Failed to restart container $name (ID: $cid)."
            fi
            echo
        else
            # No conflict: record that this port is now in use by this container.
            used_ports[$host_port]=$cid
        fi
    done <<< "$(docker port "$cid")"
done

echo "Port conflict check complete."
