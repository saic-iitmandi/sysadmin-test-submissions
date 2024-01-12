#!/bin/bash

#paratmeters
TODAY=$(TZ=":Asia/Kolkata" date)
IST_LOCAL=$(TZ=":Asia/Kolkata" date +%A_%F)

cd /home/abhinandan/Documents/SysAdmin/PS2_Monitor

SCRAPE()
{
	python3 monitor.py > "$1"
}
COMPARE()
{
	shafirstScrape=$(shasum firstScrape | awk '{ print $1 }')
	shasecondScrape=$(shasum secondScrape | awk '{ print $1 }')
	if [ "$shafirstScrape" != "$shasecondScrape" ]
	then
		echo "change detected."
		diff secondScrape firstScrape > DIFF.txt
		mv secondScrape firstScrape
		echo "Running notify script!"
		python3 mail.py
		rm DIFF.txt
		# Clearing docker
		docker rm `docker ps -aqf status=exited`
	else
		echo "No change detected"
		# as there are no changes lets just nuke secondScrape.
		rm secondScrape
	fi
}



main()
{
	if [ -f firstScrape ]
	then
		SCRAPE secondScrape
	else
		SCRAPE firstScrape
		SCRAPE secondScrape
	fi
	COMPARE
}
main
