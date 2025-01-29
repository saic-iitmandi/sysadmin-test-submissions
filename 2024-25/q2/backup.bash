#!/bin/bash

BACKUP_DIR=/backups/

mkdir -p ~/backups/

TIMESTAMP=date+%y%m%d_%H%M%S #yyyymmddhhmmss mein hai
LOG_FILE=backup.log

# Function to log messages
log() {
    echo "[$(date +"%Y-%m-%d %H:%M:%S")] $1" | tee -a "$LOG_FILE"
}

# making backup process ka function
backup() {
    # storing all docker volumes in a variable
    VOLUMES=$(docker volume ls --quiet)

    for v in $VOLUMES
    do
        ARCHIVE_NAME="$BACKUP_DIR/${v}_$TIMESTAMP.tar.gz" #name with timestamp

        log "Backing up volume: $VOLUME to $ARCHIVE_NAME" #logentry

        # actual backup now
        docker run --rm \
            -v $v:/data \
            -v $BACKUP_DIR:/backup \
            alpine \
            sh -c "tar -czf /backup/$(basename $ARCHIVE_NAME) -C /data ."

        if [ $? -eq 0 ]; then
            log "Backup successful"
        else
            log "Error."
        fi
    done

    log "Backup process completed."
}

# restore process function
restore() {
    log "Starting restore process..."

    for ARCHIVE in $(ls $BACKUP_DIR | grep ".tar.gz$") #basically looking through all zips
    do
        VOLUME=$(echo $ARCHIVE | cut -d'_' -f1)
        log "Restoring volume: $VOLUME from $ARCHIVE"

        # Ensure the volume exists
        docker volume create $VOLUME

        # Restore the volume
        docker run --rm \
            -v $VOLUME:/data \
            -v $BACKUP_DIR:/backup \
            alpine \
            sh -c "tar -xzf /backup/$ARCHIVE -C /data"

        if [ $? -eq 0 ]; then
            log "Restore successful"
        else
            log "Error."
        fi
    done

    log "Restore process completed."
}


# Main script
case $1 in
    backup)
        backup
        ;;
    restore)
        restore
        ;;
    *)
        echo "incorrect input"
        ;;
esac