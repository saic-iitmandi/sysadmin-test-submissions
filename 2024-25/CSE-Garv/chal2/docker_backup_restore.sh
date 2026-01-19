#!/bin/bash

# Docker Backup and Restore Script
# Author: Your Name
# Description: Automates backup and restore processes for Docker volumes.

# Configuration
BACKUP_DIR="/home/epicgamer/backup"  # Directory to store backups
LOG_FILE="$HOME/docker_backup_restore.log"  # Log file location
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Ensure backup directory exists
mkdir -p "$BACKUP_DIR"

log_message() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

backup_volumes() {
    log_message "Starting backup process."
    local volumes=$(docker volume ls --quiet)

    for volume in $volumes; do
        local backup_file="$BACKUP_DIR/${volume}_$TIMESTAMP.tar.gz"

        log_message "Backing up volume: $volume to $backup_file"

        docker run --rm \
            -v $volume:/data \
            -v $BACKUP_DIR:/backup \
            alpine tar czf /backup/${volume}_$TIMESTAMP.tar.gz -C /data .

        if [ $? -eq 0 ]; then
            log_message "Backup for volume $volume completed successfully."
        else
            log_message "Error occurred while backing up volume $volume."
        fi
    done

    log_message "Backup process completed."
}

restore_volumes() {
    log_message "Starting restore process."

    local volume_to_restore="$1"
    local restore_file="$2"

    if [[ -z $volume_to_restore || -z $restore_file ]]; then
        log_message "Error: Volume name and backup file must be provided."
        exit 1
    fi

    log_message "Restoring volume: $volume_to_restore from $restore_file"

    docker volume create $volume_to_restore

    docker run --rm \
        -v $volume_to_restore:/data \
        -v $BACKUP_DIR:/backup \
        alpine sh -c "tar xzf /backup/$restore_file -C /data"

    if [ $? -eq 0 ]; then
        log_message "Restore for volume $volume_to_restore completed successfully."
    else
        log_message "Error occurred while restoring volume $volume_to_restore."
    fi

    log_message "Restore process completed."
}

# Display usage information
usage() {
    echo "Usage: $0 [backup|restore] [options]"
    echo "  backup                  Perform a backup of all Docker volumes."
    echo "  restore <volume> <file> Restore a specific Docker volume from a backup file."
    echo "Examples:"
    echo "  $0 backup"
    echo "  $0 restore my_volume my_volume_20230101_120000.tar.gz"
    exit 1
}

# Main script logic
case "$1" in
    backup)
        backup_volumes
        ;;
    restore)
        restore_volumes "$2" "$3"
        ;;
    *)
        usage
        ;;
esac
