#!/bin/bash
img_id="d8e1f39c17d0"
echo "Let's pull the image first"
sleep 1
docker pull metavinayak/matrix
sleep 3
echo "Enter the number of instances of the image you want to create : "
read num
for ((i=1; i<=$num; i++)); do
    docker run -d --name instance${i} -p 808$i:3000 $img_id
done