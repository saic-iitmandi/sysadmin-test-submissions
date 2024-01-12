#!/bin/bash
#write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "55 23 * * * cd locationtothebackupscript; ./backup.sh" >> mycron
#install new cron file
crontab mycron
rm mycron