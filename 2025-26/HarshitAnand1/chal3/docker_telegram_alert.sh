#!/bin/bash

TOKEN=REDACTED_TOKEN
CHAT_ID=5507927858

STATUS=$(docker ps -a)

ALERT=$(echo "$STATUS" | grep -E "Restarting|Exited")

if [ ! -z "$ALERT" ]; then

MESSAGE="🚨 DOCKER ALERT 🚨%0A%0A$ALERT"

curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
     -d chat_id=$CHAT_ID \
     -d text="$MESSAGE" > /dev/null
fi
