#!/bin/sh
set -e

echo "Starting RoyalChess (production mode)..."

cd /app

echo "Starting backend..."
node server/dist/server.js &

echo "Starting frontend..."
cd client
npx next start -p 3000
