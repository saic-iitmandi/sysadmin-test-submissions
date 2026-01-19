#!/bin/bash

# setting up the basic stuff
BACKUP_DIR="/home/divyanshjindal/dockerBackup"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
LOG_FILE="/var/log/docker_backup_restore.log"

mkdir -p "$BACKUP_DIR" # backup directory

# Backup Docker volumes function
backupVolume() {
    echo "[INFO] Starting Docker volume backup..." | tee -a "$LOG_FILE"
    for volume in $(docker volume ls --format "{{.Name}}"); do
        echo "[INFO] Backing up volume: $volume" | tee -a "$LOG_FILE"
        docker run --rm -v "$volume":/data -v "$BACKUP_DIR":/backup alpine tar czf "/backup/${volume}_${TIMESTAMP}.tar.gz" -C /data .
    done
    echo "[INFO] Backup completed successfully." | tee -a "$LOG_FILE"
}

# Restore Docker volumes function
restoreVolume() {
    echo "[INFO] Starting Docker volume restore..." | tee -a "$LOG_FILE"
    for backup in "$BACKUP_DIR"/*.tar.gz; do
        volume_name=$(basename "$backup" | sed -E 's/_([0-9-]+_[0-9-]+)\.tar\.gz//')
        echo "[INFO] Restoring volume: $volume_name from $backup" | tee -a "$LOG_FILE"
        docker volume create "$volume_name"
        docker run --rm -v "$volume_name":/data -v "$BACKUP_DIR":/backup alpine tar xzf "/backup/$(basename "$backup")" -C /data
    done
    echo "[INFO] Restore completed successfully." | tee -a "$LOG_FILE"
}

# doing stuff based on the input
case "$1" in
    backup)
        backupVolume
        ;;
    restore)
        restoreVolume
        ;;
    *)
        echo "Usage: $0 {backup|restore}" | tee -a "$LOG_FILE"
        exit 1
        ;;
esac
