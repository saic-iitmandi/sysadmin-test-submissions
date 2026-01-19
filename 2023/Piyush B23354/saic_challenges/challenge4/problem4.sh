#!/bin/bash

IMAGE_NAME="matrix"
TAG="latest"

USERNAME="metavinayak"

# Pulling the Docker image from Docker Hub
docker pull $USERNAME/$IMAGE_NAME:$TAG

docker run -d --name $IMAGE_NAME-$TAG -p 8080:3000 $USERNAME/$IMAGE_NAME:$TAG
