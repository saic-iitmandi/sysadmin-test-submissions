#!/bin/bash

prev=$(cat ids.txt)
docks=$(docker ps --format "{{.ID}}")
docker ps --format "{{.ID}}" > ids.txt
#echo $docks
ids=$(echo $docks | tr " " "\n")

for i in $prev
do
	if [[ $ids =~ $i ]]; then
   		echo "It's there! $i"
   	else
   		echo "It's NOT there! $i">monitor.txt
   		echo "$(docker ps -af "id=$i")">>monitor.txt
   		echo " $(docker logs $i| sed -r "s/\x1B\[([0-9]{1,2}(;[0-9]{1,2})?)?[mGK]//g"| sed -e 's/\]0;//g' -e 's/\[?2004[hl]//g')">>monitor.txt
   		cat monitor.txt | mail -s "Docker Exited" saic@students.iitmandi.ac.in
	fi
done



