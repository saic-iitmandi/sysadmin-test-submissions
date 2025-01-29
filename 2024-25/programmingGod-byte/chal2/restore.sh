#!/bin/bash


BACKUP_DIR=/home/shivam-kumar/Desktop/systemadministration/problem2/backup
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
LOG_FILE="/var/log/saic_docker_restore.log"

echo "" > "${LOG_FILE}" 

restore_latest_volume() {
    local volume=$1
    echo "Restoring volume: ${volume} from the latest backup" >> "${LOG_FILE}" 
    latest_archive=$(ls -t ${BACKUP_DIR}/${volume}_*.tar.gz | head -n 1)
    if [ -z "$latest_archive" ]; then
        echo "No backup found for volume: ${volume}" >> "${LOG_FILE}" 
        return
    fi
    docker volume create ${volume} >> "${LOG_FILE}" 
    docker run --rm -v ${volume}:/volume -v ${latest_archive}:/backup.tar.gz busybox tar -xzf /backup.tar.gz -C /volume
    echo "Restored volume: ${volume} from ${latest_archive}" >> "${LOG_FILE}" 
}

mount_volume_to_containers() {
    local volume=$1
    echo "Mounting restored volume: ${volume} to containers" >> "${LOG_FILE}" 
    json_file="${BACKUP_DIR}/${volume}.json"
    if [ ! -f "$json_file" ]; then
        echo "No JSON file found for volume: ${volume}" >> "${LOG_FILE}" 
        return
    fi

  
    docker run -d --name temp_container -v ${volume}:/volume busybox sleep infinity >> "${LOG_FILE}" 

 
    containers=$(jq -c '.containers[]' < "$json_file")
    for container_info in $containers; do
        container=$(echo "$container_info" | jq -r '.container')
        mount_point=$(echo "$container_info" | jq -r '.mount_point')
        
       
        docker cp temp_container:/volume/. ${container}:${mount_point} 2>/dev/null
        echo "Volume: ${volume} mounted to container: ${container} at mount point: ${mount_point}" >> "${LOG_FILE}" 
    done

    
    docker rm -f temp_container >> "${LOG_FILE}" 
}

restore_all_latest_volumes() {
    echo "Restoring all volumes from the latest backups" >> "${LOG_FILE}" 
    for latest_archive in $(ls -t ${BACKUP_DIR}/*.tar.gz | awk -F'_' '{print $1}' | sort -u); do
        volume=$(basename ${latest_archive} | cut -d'_' -f1)
        restore_latest_volume ${volume}
        mount_volume_to_containers ${volume}
    done
    echo "All volumes restored from latest backups." >> "${LOG_FILE}" 
}

echo "Enter the name of the volume to restore or type 'all' to restore all volumes:"
read volume_name

if [ "$volume_name" == "all" ]; then
    restore_all_latest_volumes
else
    restore_latest_volume $volume_name
    mount_volume_to_containers $volume_name
fi
