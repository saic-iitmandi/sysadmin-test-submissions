#!/bin/bash

BACKUP_DIR=/home/shivam-kumar/Desktop/systemadministration/problem2/backup
BACKUP_HISTORY_DIR=/home/shivam-kumar/Desktop/systemadministration/problem2/backupHistory
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
LOG_FILE="/var/log/saic_docker_backup.log"


DIRECTORY="backupHistory"
if [ ! -d "$DIRECTORY" ]; then
  mkdir -p "$DIRECTORY"
fi

if [ -d "$BACKUP_DIR" ]; then
  rm -r "${BACKUP_DIR}"
fi

echo "" > "${LOG_FILE}" 
echo "Starting backup process..." >>"${LOG_FILE}"

docker volume ls -q | while read volume; do
    ARCHIVE_NAME="${BACKUP_DIR}/${volume}_${TIMESTAMP}.tar.gz"
    echo "Backing up volume: ${volume} to ${ARCHIVE_NAME}" >>"${LOG_FILE}" 
    docker run --rm -v ${volume}:/volume -v ${BACKUP_DIR}:/backup busybox tar -czf /backup/${volume}_${TIMESTAMP}.tar.gz -C /volume ./
    
    containers=$(docker ps -a --filter "volume=${volume}" --format '{{.ID}}')
    container_array=()
    for container in $containers; do
        mount_point=$(docker inspect --format='{{ range .Mounts }}{{ if eq .Name "'${volume}'" }}{{ .Destination }}{{ end }}{{ end }}' $container)
        container_array+=("{\"container\": \"$(docker inspect --format='{{.Name}}' $container | cut -d'/' -f2)\", \"mount_point\": \"${mount_point}\"}")
    done
    
    json_content="{\"volume\": \"${volume}\", \"containers\": [$(IFS=,; echo "${container_array[*]}")]}"
    echo $json_content > "${BACKUP_DIR}/${volume}.json"
done

echo "Backup process completed." >>"${LOG_FILE}"

mkdir "${BACKUP_HISTORY_DIR}/${TIMESTAMP}"
cp -r "${BACKUP_DIR}/"*  "${BACKUP_HISTORY_DIR}/${TIMESTAMP}"
