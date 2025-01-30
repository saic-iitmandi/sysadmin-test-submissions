BACKUP_DIR="/home/utkarshsahu/Chal2/backup"  # Specify your backup directory
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
LOG_FILE="/var/log/docker_backup_restore.log"

log() {
  echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" | tee -a "$LOG_FILE"
}

backup() {
  log "Starting Docker volumes backup."
  mkdir -p "$BACKUP_DIR/$TIMESTAMP"

  for volume in $(docker volume ls -q); do
    log "Backing up volume: $volume"
    docker run --rm \
      -v $volume:/data \
      -v "$BACKUP_DIR/$TIMESTAMP":/backup \
      alpine tar czf "/backup/${volume}.tar.gz" -C /data .
  done

  log "Backup completed. Files are stored in $BACKUP_DIR/$TIMESTAMP."
}

restore() {
  if [ -z "$1" ]; then
    log "No backup timestamp provided. Restoring from latest backup."
    LATEST_BACKUP=$(ls -td $BACKUP_DIR/* | head -1)
  else
    LATEST_BACKUP="$BACKUP_DIR/$1"
  fi

  if [ ! -d "$LATEST_BACKUP" ]; then
    log "Backup directory $LATEST_BACKUP not found!"
    exit 1
  fi

  log "Restoring from backup directory: $LATEST_BACKUP"

  for file in $LATEST_BACKUP/*.tar.gz; do
    volume=$(basename "$file" .tar.gz)
    log "Restoring volume: $volume"
    docker run --rm \
      -v $volume:/data \
      -v "$LATEST_BACKUP":/backup \
      alpine tar xzf "/backup/${volume}.tar.gz" -C /data
  done

  log "Restore completed."
}

case "$1" in
  backup)
    backup
    ;;
  restore)
    restore "$2"
    ;;
  *)
    echo "Usage: $0 {backup|restore [timestamp]}"
    exit 1
    ;;
esac
