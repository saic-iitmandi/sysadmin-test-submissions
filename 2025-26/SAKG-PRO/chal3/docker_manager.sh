#!/bin/bash

# Configuration
REPORT_FILE="system_health_report.log"
ERROR_KEYWORDS="ERROR|CRITICAL|FATAL|panic|failed to start"
PORT_CLASH_KEYWORDS="address already in use|bind: address already in use|failed to bind|port is already allocated"
START_PORT=9000

echo "================================================"
echo "      DOCKER MONITOR & RECOVERY SYSTEM"
echo "================================================"

find_free_port() {
    local port=$1
    while netstat -tuln | grep -q ":$port "; do
        ((port++))
    done
    echo "$port"
}

# Define your website services
SERVICES=("frontend" "api_docs" "landing_page")

echo "Select a service to manage:"
select SERVICE_NAME in "${SERVICES[@]}"; do
    if [[ -n "$SERVICE_NAME" ]]; then
        echo ">>> Analyzing Service: $SERVICE_NAME"
        
        # Identify container
        CONTAINER_ID=$(docker ps -a --filter "label=com.docker.compose.service=$SERVICE_NAME" --format "{{.ID}}" | head -n 1)
        
        # Get Status and Logs
        STATUS=$(docker inspect --format='{{.State.Status}}' "$CONTAINER_ID" 2>/dev/null || echo "missing")
        LOGS=$(docker logs "$CONTAINER_ID" 2>&1)

        # 1. TRIGGER RECOVERY IF BROKEN
        if [[ "$STATUS" != "running" ]] || echo "$LOGS" | grep -Ei "$PORT_CLASH_KEYWORDS" >/dev/null || [ "$STATUS" == "missing" ]; then
            echo "[!] PORT CLASH DETECTED for '$SERVICE_NAME'"
            
            # Find image and free port
            IMAGE=$(docker inspect --format='{{.Config.Image}}' "$CONTAINER_ID" 2>/dev/null || echo "nginx:alpine")
            NEW_PORT=$(find_free_port $START_PORT)

            echo "[+] ACTION: Migrating to Port $NEW_PORT"
            
            # Cleanup and Restart
            docker rm -f "restored_$SERVICE_NAME" "$CONTAINER_ID" >/dev/null 2>&1
            docker run -d --name "restored_$SERVICE_NAME" -p "$NEW_PORT":80 "$IMAGE"
            
            echo "[✓] RESTORED: Access at http://localhost:$NEW_PORT"
        
        # 2. PROVIDE LOGS IF HEALTHY
        else
            echo "[✓] $SERVICE_NAME is healthy."
            echo "1) View Live Logs"
            echo "2) Run Error Analysis"
            read -p "Select an option: " CHOICE
            
            case $CHOICE in
                1)
                    echo "Streaming logs (Ctrl+C to stop)..."
                    docker logs -f --tail 50 --timestamps "$CONTAINER_ID"
                    ;;
                2)
                    CRITICAL_LOGS=$(echo "$LOGS" | grep -Ei "$ERROR_KEYWORDS")
                    [ -n "$CRITICAL_LOGS" ] && echo "$CRITICAL_LOGS" || echo "No errors found."
                    ;;
            esac
        fi
        break
    fi
done