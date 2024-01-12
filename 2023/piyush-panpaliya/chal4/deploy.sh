#!/bin/bash
IMAGES=("metavinayak/matrix")

PORT=8000
for IMAGE in "${IMAGES[@]}"; do

    docker stop $PORT || true
    docker rm $PORT || true

    docker image pull $IMAGE
    echo "Running $IMAGE on port $PORT"
    docker run -d --name $PORT -p $PORT:3000 "$IMAGE"
    ((PORT++))
done