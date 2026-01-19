#!/bin/bash

# ==============================
# Docker Log & Port Health Tool
# ==============================

REPORT="summary_report.txt"

echo "==== Docker Health Report: $(date) ====" > $REPORT

echo "[*] Starting analysis..."

# ---------- 1. LOG ANALYSIS ----------

echo "[*] Checking container logs..." | tee -a $REPORT

for id in $(docker ps -q)
do
    NAME=$(docker inspect --format '{{.Name}}' $id | sed 's/\///')

    echo "---- Logs for $NAME ----" | tee -a $REPORT

    ERRORS=$(docker logs $id 2>&1 | grep -Ei "error|critical|failed|fatal|exception")

    if [ ! -z "$ERRORS" ]; then
        echo "CRITICAL ISSUES FOUND IN: $NAME" | tee -a $REPORT
        echo "$ERRORS" | tee -a $REPORT
        echo "-----------------------------------" | tee -a $REPORT
    else
        echo "No critical issues in $NAME" | tee -a $REPORT
    fi
done


# ---------- 2. PORT CLASH DETECTION ----------

echo "" | tee -a $REPORT
echo "[*] Checking for Port Clashes..." | tee -a $REPORT

docker ps --format "{{.Names}} {{.Ports}}" > portinfo.txt

CLASH=$(cat portinfo.txt | grep -o "[0-9]*->" | sort | uniq -d)

if [ -z "$CLASH" ]; then
    echo "No port clash detected" | tee -a $REPORT
else
    echo "PORT CLASH DETECTED on: $CLASH" | tee -a $REPORT

    CNAME=$(grep "$CLASH" portinfo.txt | awk '{print $1}')

    echo "Affected container: $CNAME" | tee -a $REPORT
    echo "Attempting automatic recovery..." | tee -a $REPORT

    docker restart $CNAME

    if [ $? -eq 0 ]; then
        echo "Container $CNAME restarted successfully" | tee -a $REPORT
    else
        echo "Recovery failed for $CNAME" | tee -a $REPORT
    fi
fi


# ---------- 3. SUMMARY ----------

echo "" | tee -a $REPORT
echo "Analysis complete. Detailed report saved in $REPORT" | tee -a $REPORT
