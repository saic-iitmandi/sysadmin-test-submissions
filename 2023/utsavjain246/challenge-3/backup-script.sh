#!/bin/bash


SAIC_DATA_PATH="/home/utsav/Desktop/challenge-3/saic-data"
GITHUB_LANG_DATA_PATH="/home/utsav/Desktop/challenge-3/postgres-data"


BACKUP_DESTINATION="/home/utsav/Desktop/challenge-3/backup"

# timestamp for the backup file
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

zip -r "$BACKUP_DESTINATION/saic_website_backup_$TIMESTAMP.zip" "$SAIC_DATA_PATH"

zip -r "$BACKUP_DESTINATION/github_lang_backup_$TIMESTAMP.zip" "$GITHUB_LANG_DATA_PATH"

echo "Backup completed successfully at $(date)."

