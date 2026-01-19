#!/bin/bash

REPORT="docker_report_$(date +%F_%T).txt"

echo "Docker Container Log Analysis Report" > $REPORT
echo "Generated on: $(date)" >> $REPORT
echo "----------------------------------" >> $REPORT

# Get running containers
containers=$(docker ps --format "{{.ID}} {{.Names}}")

for c in $containers; do
    cid=$(echo $c | awk '{print $1}')
    cname=$(echo $c | awk '{print $2}')

    echo -e "\nContainer: $cname ($cid)" >> $REPORT
    echo "-------------------------" >> $REPORT

    logs=$(docker logs --since 15m $cid 2>&1)

    # Detect critical errors
    critical=$(echo "$logs" | grep -Ei "error|fail|crash|exception")

    if [ -n "$critical" ]; then
        echo "CRITICAL LOGS FOUND:" >> $REPORT
        echo "$critical" >> $REPORT
    else
        echo "No critical errors found." >> $REPORT
    fi

    # Detect port clash
    port_error=$(echo "$logs" | grep -Ei "address already in use|port.*already")

    if [ -n "$port_error" ]; then
        echo "⚠ PORT CLASH DETECTED" >> $REPORT
        echo "$port_error" >> $REPORT

        echo "Attempting automatic recovery..." >> $REPORT

        image=$(docker inspect --format='{{.Config.Image}}' $cid)
        new_port=$(shuf -i 3000-65000 -n 1)

        docker stop $cid
        docker rm $cid

        docker run -d -p $new_port:80 $image

        echo "Service restored on new port: $new_port" >> $REPORT
    fi
done

echo -e "\nSummary completed." >> $REPORT
