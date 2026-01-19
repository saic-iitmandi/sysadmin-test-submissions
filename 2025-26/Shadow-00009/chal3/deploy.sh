#!/bin/bash

# Challenge 3 Deployment Script
# Usage: ./deploy.sh

echo "=========================================="
echo "      Challenge 3: Docker Deployments     "
echo "=========================================="

# 1. Check if Docker is running
if ! docker info > /dev/null 2>&1; then
  echo "Error: Docker is not running. Please start Docker Desktop."
  exit 1
fi

echo "[*] Docker is running."

# 2. Build and Start Containers
# The -d flag runs it in 'detached' mode (in the background)
# --build forces a rebuild of the images to ensure changes are picked up
echo "[*] Building and starting services..."
docker-compose up -d --build

# 3. Validation
if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "       DEPLOYMENT SUCCESSFUL              "
    echo "=========================================="
    echo "Services are running on:"
    echo " - RoyalChess Frontend: http://localhost:3000"
    echo " - RoyalChess Backend:  http://localhost:5000"
    echo " - STAC Frontend:       http://localhost:3001"
    echo " - STAC Backend:        http://localhost:8000"
    echo ""
    echo "Security Check:"
    echo " - Databases (Mongo/Postgres) are NOT accessible on localhost."
    echo " - They are isolated within the internal Docker network."
    echo ""
    echo "Useful Commands:"
    echo " - View logs:   docker-compose logs -f"
    echo " - Stop app:    docker-compose down"
    echo " - List running: docker ps"
else
    echo "Error: Deployment failed. Check the logs above."
fi