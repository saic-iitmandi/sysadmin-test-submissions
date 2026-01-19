# First Step was installing docker desktop

-ensured that Docker was running in WSL and created a sample Docker setup.

# Second Step

-Created a Docker Compose file in your test directory
-With the command nano docker-compose.yml
-Made the docker Containers docker-compose up -d

# Third Step

-Created the backup and restore script nano restore_bakcup_script.sh and made a typo ;\_\_;
-Wrote code for it to happen manually
-Made it an executable chmod +x restore_bakcup_script.sh

# Fourth Step

-Ran the backup and restore commands with ./restore_bakcup_script.sh backup
and ./restore_bakcup_script.sh restore

# Fifth Step

-Set up a cron job to make the script run automatically at midnight with
-crontab -e
-added 0 0 \* \* \* /mnt/c/Users/shiva/OneDrive/Documents/sysAdmin/sysAdmin2025/dockerTestapp/restore_bakcup_script.sh backup >> /mnt/c/Users/shiva/OneDrive/Documents/sysAdmin/sysAdmin2025/dockerTestapp/backup_restore.log 2>&1

# Copied Logs between WSL and windows using

-cp /path/to/logfile/backup_restore.log /mnt/c/Users/shiva/OneDrive/Documents/sysAdmin/sysAdmin2025/dockerTestapp/
