#!/bin/bash
CONTAINER_NAME="practical_margulis"
sudo_password="" 
output_file="/home/fach/Monitor/status.txt"

no_of_containers=$(echo $sudo_password | sudo -S docker ps | grep $CONTAINER_NAME | wc -l)

if [ "$no_of_containers" -ge 1 ]; then  
	echo "$CONTAINER_NAME is running!" >> $output_file 
else   
	echo "$CONTAINER_NAME is not running!" >> $output_file
fi
