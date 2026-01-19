import psutil  # For monitoring system hardware
import time
import datetime
import os    
from script import enumerate_files_and_folders  

# log events to a file for tracking
log_file = "external_drive_monitor.log"

# log messages function
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file,"a") as log_text:
        log_text.write(f"{timestamp} {message} \n")
    print({message})

def get_external_drives():
    external_drives = []
    for partition in psutil.disk_partitions():


        if 'removable' in partition.opts or 'cdrom' in partition.opts:         # check if the device is removable
            external_drives.append(partition.mountpoint)
    return external_drives

def monitor_external_drives(log_file):
    log_message("Monitoring for external drives...")

    # initialize with current connected drives
    known_drives = set(get_external_drives())
    log_message(f"Initial known drives: {known_drives}")

    while True:
        try:

            current_drives = set(get_external_drives())  # get currently connected external drives

            new_drives = current_drives - known_drives  # check for new drives which are added newly to host system

            if new_drives:
                for drive in new_drives:
                    log_message(f"New external drive detected: {drive}") # log the detection of the new drive
                    
                    enumerate_files_and_folders(drive, log_file)  # this function access the files inside the external drive

                known_drives = current_drives   # update known drives
            
            time.sleep(5)

        except Exception as e:
            log_message(f"Error occurred: {e}")    # log any errors that occur
            break

if __name__ == "__main__":
    monitor_external_drives("drive_log_file.log")
