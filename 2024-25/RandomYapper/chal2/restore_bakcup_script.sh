#!/bin/bash

BACKUP_DIR="$HOME/docker_backups"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
LOG_FILE="$BACKUP_DIR/backup_restore.log"


mkdir -p "$BACKUP_DIR"

echo "[$TIMESTAMP] Starting Docker Backup Process" | tee -a "$LOG_FILE"

backup_volumes() {
    for volume in $(docker volume ls --format "{{.Name}}"); do
        echo "Backing up volume: $volume" | tee -a "$LOG_FILE"
        docker run --rm -v $volume:/data -v $BACKUP_DIR:/backup alpine tar -czf /backup/${volume}_$TIMESTAMP.tar.gz /data
    done
    echo "Backup completed successfully." | tee -a "$LOG_FILE"
}


restore_volumes() {
    latest_backup=$(ls -t "$BACKUP_DIR"/*.tar.gz | head -n 1)
    if [ -z "$latest_backup" ]; then
        echo "No backup files found!" | tee -a "$LOG_FILE"
        exit 1
    fi

    for volume in $(docker volume ls --format "{{.Name}}"); do
        archive="$BACKUP_DIR/${volume}_*.tar.gz"
        if ls $archive 1> /dev/null 2>&1; then
            latest_archive=$(ls -t $archive | head -n 1)
            echo "Restoring volume: $volume from $latest_archive" | tee -a "$LOG_FILE"
            docker run --rm -v $volume:/data -v $BACKUP_DIR:/backup alpine tar -xzf /backup/$(basename $latest_archive) -C /data
        else
            echo "No backup found for volume: $volume" | tee -a "$LOG_FILE"
        fi
    done
    echo "Restore process completed." | tee -a "$LOG_FILE"
}


case "$1" in
    backup)
        backup_volumes
        ;;
    restore)
        restore_volumes
        ;;
    *)
        echo "Usage: $0 {backup|restore}"
        exit 1
        ;;
esac
