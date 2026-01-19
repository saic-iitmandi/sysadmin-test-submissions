#!/bin/bash


docker volume create firstVolume

docker volume create secondVolume


docker run -d --name con1 -v firstVolume:/data ubuntu sleep infinity
docker run -d --name con2 -v secondVolume:/data ubuntu sleep infinity


docker exec con1 sh -c 'echo "Random content for firstVolume" > /data/random1.txt'


docker exec con2 sh -c 'echo "Random content for secondVolume" > /data/random2.txt'


docker exec con1 cat /data/random1.txt


docker exec con2 cat /data/random2.txt

