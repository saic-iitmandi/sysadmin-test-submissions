#!/bin/bash

# Checking if the user provided the number of intansces wanted
if [ -z "$NUM_PORTS" ]; then
  echo "Please set the NUM_PORTS environment variable."
  exit 1
fi

cat <<EOF > docker-compose.yml
version: '3'

services:
EOF

#writing the services to the docker-compose.yml file
for ((i = 0; i < NUM_PORTS; i++)); do
  PORT=$((10000 + i)) 
  cat <<EOF >> docker-compose.yml
  app$i:
    image: metavinayak/matrix:latest
    ports:
      - "$PORT:3000" # Change the container port if needed
    networks:
      - my-network
EOF
done

cat <<EOF >> docker-compose.yml

networks:
  my-network:
EOF

docker-compose up -d
