#!/bin/bash

docker pull "$1"
docker run -d -p 8000:3000 "$1"

