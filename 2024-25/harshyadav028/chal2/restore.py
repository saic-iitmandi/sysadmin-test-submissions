import os
import subprocess
from datetime import datetime

BACKUP_FOLDER = "." # current folder 
LOG_FILE = "./restore_logfile.log"

# log message
def log_message(message):
    """Log a message to the log file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as log:
        log.write(f"[{timestamp}] {message}\n")
    print({message})

# find latest backup function
def filter_backup(volume_name):
# Filter files matching the volume name and extension
    files = [f for f in os.listdir(BACKUP_FOLDER) if f.startswith(f"{volume_name}") and f.endswith(".tar.gz")]
    if not files:
        return None
    # Sort files by their names (timestamp ensures correct order)
    files.sort()  # Lexicographical sort works due to timestamp format
    return os.path.join(BACKUP_FOLDER, files[-1])  # Return the latest file

# restore one volume again in the docker container
def restore_volume(volume_name): 
    log_message(f"Starting restore for volume: {volume_name}")
    backup_file = filter_backup(volume_name)
    
    if not backup_file:
        log_message(f"No backup file found for {volume_name}")
        return
    
    try:
        # Restore the backup into the volume
        subprocess.run(["docker", "run", "--rm",
                        "-v", f"{volume_name}:/volume",  # Ensures correct volume mount
                        "-v", f"{os.getcwd()}:/backup",
                        "alpine", "sh", "-c", f"tar xzf /backup/{os.path.basename(backup_file)} -C /volume"],
                       check=True)
        
        log_message(f"Restore successful for volume: {volume_name}")

    except subprocess.CalledProcessError as e:
        log_message(f"Failed to restore volume {volume_name}. Error: {e}")
# restore all volumes
def restore_all_volumes():
    log_message("starting full restore proccess")
    volume_actual_names = [f.split(".")[0] for f in os.listdir(BACKUP_FOLDER) if f.endswith(".tar.gz")]
    for volume_name in volume_actual_names:
        restore_volume(volume_name)
    log_message("all volumes restored successfully")

# main execution
if __name__ == "__main__":
    # # restore specified volumes

    # volumes = input("Enter the specified volume names you want to restore (comma-seprated):  ").strip().split(",")
    # for volume in volumes:
    #     restore_volume(volume.strip())

    # # restore all volumes from their latest backups
    restore_all_volumes()