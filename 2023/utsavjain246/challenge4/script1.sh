#!/bin/bash

# Function
run_by_id() {
    local image_id=$1
    local container_name=$2
    local host_port=$3
    
    docker pull $image_id
    docker run -d -p $host_port:3000 --name $container_name $image_id
}

# Deploy the image by ID with port mapping
run_by_id $image_id $container_name $host_port

