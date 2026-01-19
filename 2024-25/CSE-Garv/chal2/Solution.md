
# **Complete Guide for Docker Volume Backup and Restore with Cron Automation**

This guide will walk you through:

- Creating Docker volumes with sample data
- Running the backup and restore scripts
- Setting up automated backups with cron
- Understanding log files and troubleshooting

### **Table of Contents**
1. [Prerequisites](#1-prerequisites)
2. [Step 1: Create Docker Volumes and Add Sample Data](#2-create-docker-volumes-and-add-sample-data)
3. [Step 2: Download and Configure the Backup and Restore Script](#3-download-and-configure-the-backup-and-restore-script)
4. [Step 3: Run Backup and Restore Scripts](#4-run-backup-and-restore-scripts)
5. [Step 4: Automate Backups Using Cron](#5-automate-backups-using-cron)
6. [Step 5: Check Logs](#6-check-logs)

---

### **1. Prerequisites**

Before starting, ensure the following:

- **Docker is installed**: You need Docker to create and manage volumes and containers. [Install Docker](https://docs.docker.com/get-docker/).
- Basic knowledge of using the terminal or command line.

---

### **2. Create Docker Volumes and Add Sample Data**

We will create sample Docker volumes and add sample data that will be backed up.

#### Step 1: Create Docker Volumes

Run the following commands to create Docker volume:

```bash
docker volume create sample_volume
```

#### Step 2: Add Sample Data

Now we’ll add some sample data to the volumes using an `alpine` container:

```bash
docker run --rm -v sample_volume:/data alpine /bin/sh -c "echo 'Hello, Docker Backup!' > /data/sample.txt"
```

#### Step 3: Verify Data

You can verify the data is in the volumes by running:

```bash
docker run --rm -v sample_volume:/data alpine cat /data/sample.txt
```

This should output the following:

```
Hello, Docker Backup!
```


Now your Docker volumes are ready to be backed up!

---

### **3. Download and Configure the Backup and Restore Script**

#### Step 1: Create the Script File

Create a new file called `docker_backup_restore.sh`:

```bash
nano docker_backup_restore.sh
```

#### Step 2: Paste the Script

Paste the following code into the file. This script handles both backup and restore of Docker volumes.

```bash
#!/bin/bash

# Define the backup directory and log file
BACKUP_DIR="/path/to/backup/directory"
LOG_FILE="${BACKUP_DIR}/docker_backup_restore_log_$(date +'%Y-%m-%d').log"
TIMESTAMP=$(date +'%Y-%m-%d_%H-%M-%S')

# Ensure the backup directory exists
mkdir -p $BACKUP_DIR

# Function to log messages
log_message() {
    echo "$1" >> $LOG_FILE
}

# Start logging
log_message "===== Backup/Restore Started: $(date) ====="

# Check if an argument is provided (backup or restore)
if [ "$1" == "backup" ]; then
    log_message "Backup operation selected."

    # Fetch the list of Docker volumes available on the system
    VOLUMES=$(docker volume ls -q)

    # Loop through each volume and create a backup
    for VOLUME in $VOLUMES; do
        BACKUP_FILE="${BACKUP_DIR}/${VOLUME}_${TIMESTAMP}.tar.gz"
        
        # Log the start of the backup for this volume
        log_message "Backing up volume: $VOLUME"

        # Create the backup using a temporary Alpine container
        docker run --rm -v $VOLUME:/volume -v $BACKUP_DIR:/backup alpine \
            tar czf /backup/$(basename $BACKUP_FILE) -C /volume . >> $LOG_FILE 2>&1
        
        # Log the completion of the backup for this volume
        if [ $? -eq 0 ]; then
            log_message "Backup completed for volume: $VOLUME, saved to $BACKUP_FILE"
        else
            log_message "Error occurred while backing up volume: $VOLUME"
        fi
    done
elif [ "$1" == "restore" ]; then
    log_message "Restore operation selected."

    # Fetch the list of Docker volumes available on the system
    VOLUMES=$(docker volume ls -q)

    # Loop through each volume and restore from the most recent backup
    for VOLUME in $VOLUMES; do
        # Find the most recent backup file for this volume
        BACKUP_FILE=$(ls $BACKUP_DIR | grep "^$VOLUME" | sort -r | head -n 1)
        
        # Log that no backup was found if applicable
        if [ -z "$BACKUP_FILE" ]; then
            log_message "No backup found for volume: $VOLUME"
            continue
        fi
        
        # Log the start of the restore for this volume
        log_message "Restoring volume: $VOLUME from $BACKUP_FILE"
        
        # Restore the volume from the selected backup using a temporary Alpine container
        docker run --rm -v $VOLUME:/volume -v $BACKUP_DIR:/backup alpine \
            tar xzf /backup/$BACKUP_FILE -C /volume >> $LOG_FILE 2>&1
        
        # Log the completion of the restore for this volume
        if [ $? -eq 0 ]; then
            log_message "Restore completed for volume: $VOLUME from $BACKUP_FILE"
        else
            log_message "Error occurred while restoring volume: $VOLUME"
        fi
    done
else
    log_message "Invalid argument. Please use 'backup' or 'restore'."
    echo "Usage: ./docker_backup_restore.sh [backup|restore]"
fi

# Log the end of the operation
log_message "===== Backup/Restore Ended: $(date) ====="
```

#### Step 3: Save the File

Save the script (`Ctrl+X`, then `Y` to confirm).

#### Step 4: Make the Script Executable

Run the following command to make the script executable:

```bash
chmod +x docker_backup_restore.sh
```

---

### **4. Run Backup and Restore Scripts**

#### Run the Backup Script

To back up the Docker volumes:

```bash
./docker_backup_restore.sh backup
```

This will back up all Docker volumes and store them in the specified backup directory.

#### Run the Restore Script

To restore the Docker volumes from the most recent backup:

```bash
./docker_backup_restore.sh restore
```

This will restore all Docker volumes from the most recent backup found in the backup directory.

---

### **5. Automate Backups Using Cron**

You can automate the backup process by setting up a cron job to run the backup script daily at midnight.

#### Step 1: Open the Crontab File

Run the following command to edit your crontab:

```bash
crontab -e
```

#### Step 2: Add the Cron Job

Add the following line to schedule the backup every day at midnight:

```
0 0 * * * /path/to/docker_backup_restore.sh backup >> /path/to/backup/directory/docker_backup_restore_log_$(date +\%Y-\%m-\%d).log 2>&1
```

#### Step 3: Save and Exit

Save and exit the editor (`Ctrl+X`, then `Y` to confirm). This cron job will now automatically run the backup script every day at midnight.

---

### **6. Check Logs**

To check the logs for the backup or restore operations, you can view the log files in the backup directory.

```bash
cat /path/to/backup/directory/docker_backup_restore_log_YYYY-MM-DD.log
```

These logs will show you which volumes were backed up or restored, and whether any errors occurred.


