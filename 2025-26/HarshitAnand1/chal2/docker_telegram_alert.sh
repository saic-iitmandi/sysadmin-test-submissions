#!/bin/bash

# Set these environment variables before running:
# export TELEGRAM_BOT_TOKEN="your_token_here"
# export TELEGRAM_CHAT_ID="your_chat_id_here"

TOKEN=${TELEGRAM_BOT_TOKEN:-"YOUR_TELEGRAM_BOT_TOKEN_HERE"}
CHAT_ID=${TELEGRAM_CHAT_ID:-"YOUR_TELEGRAM_CHAT_ID_HERE"}

STATUS=$(docker ps -a)

ALERT=$(echo "$STATUS" | grep -E "Restarting|Exited")

if [ ! -z "$ALERT" ]; then

MESSAGE="🚨 DOCKER ALERT 🚨%0A%0A$ALERT"

curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
     -d chat_id=$CHAT_ID \
     -d text="$MESSAGE" > /dev/null
fi
