import os
import tarfile
import time
import docker
from datetime import datetime
import subprocess # for macos

# constant files path
BACKUP_FOLDER = "./backup" # where all the backup files will be stored
LOG_FILE = "./backup_logfile.log" # maintains a log file when the script is executing with timestamps

# ensures backup directory exists
# os.makedirs(BACKUP_FOLDER, exist_ok=True)

# log messages function
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE,"a") as log_text:
        log_text.write(f"{timestamp} {message} \n")
    print({message})

# initialize docker client (this is used to connect us to docker and its images,volumes etc.)
docker_client = docker.from_env()

# function to backup one volume
def backup_volume(volume_name):
    # for linux as in linux volumes mounts are stored in local system not in docker desktop as in macos
    # try:
    #     # create a tar.gz archive for the volume
    #     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    #     backup_file = os.path.join(BACKUP_FOLDER, f"{volume_name}_{timestamp}.tar.gz")
    #     log_message(f"Starting backup for volume: {volume_name}")

    #     # get the volume mount path
    #     volume = docker_client.volumes.get(volume_name)
    #     mount_path = volume.attrs["Mountpoint"]

    #     # compress the volume content to archive tar.gz file
    #     with tarfile.open(backup_file,"w:gz") as tar:
    #         tar.add(mount_path, arcname= os.path.basename(mount_path))

    #     log_message(f"backup completed for volume: {volume_name}, saved to {backup_file}")

    # except Exception as e:
    #     log_message(f"Failed to backup volume: {volume_name}, Error: {str(e)}")

    # macos code (this approach ensures compatibility with Docker Desktop on macos)
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_file = os.path.join(BACKUP_FOLDER, f"{volume_name}_{timestamp}.tar.gz")
        
        subprocess.run(["docker", "run", "--rm", 
                        "-v", f"{volume_name}:/volume",  # Removed timestamp from volume mount
                        "-v", f"{os.getcwd()}:/backup", 
                        "alpine", "sh", "-c", f"tar czf /backup/{volume_name}_{timestamp}.tar.gz -C /volume ."],
                       check=True)
        
        log_message(f"Backup successful: {backup_file}")

    except subprocess.CalledProcessError as e:
        log_message(f"Failed to backup volume: {volume_name}, Error: {e}")

# backup all volumes in the container
def backup_all_volumes():
    log_message("starting full backup process")
    try:
        volumes = docker_client.volumes.list()
        for volume in volumes:
            volume_name = volume.name
            backup_volume(volume_name)

        log_message("All volumes backed up successfully.")

    except Exception as e:
        log_message(f"Failed to backup all volumes. Error: {str(e)}")

# main execution
if __name__ == "__main__":
    backup_all_volumes()

