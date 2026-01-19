## **Challenge 2 - Docker Scripting**
I bifurcated the challenge into two parts one part is backup part and another is restore part.

## Backup Process:

### Flow:
- I used docker SDK to access the containers on machine and date time to show it in log file.
- Set up the location of backup directory where volumes backup files will be stored with volume name and backup time.
- Set up location of log file where all logs will be shown.
- Created function which push log message with timestamp to backup log file.
- Initialized docker client which connect us either our machine docker.
- Identify all Docker volumes.
- Created function for one backup volume to be restored with volume name as parameter
- Create a compressed archive  **.tar.gz** for each volume with a timestamp.
- Run the loop to back up all volumes available in the machine docker containers.

## Restore Process:

### Flow:
- Set up restore search folder path and log file path.
- Create filter function to filter files on the basis of files that ends with  “.tar.gz” and latest timestamp.
- Created function to restore specific volume to that specified docker container.
- Also made script if want to restore all volume files that are backed up in the folder.

## Instructions:
- Backup script and Restore script are python scripts so can be executed on any compiler or from terminal.

### By Terminal:
- `docker run -dit --name sample-container -v sample_volume:/data alpine` (you can also create a sample nginx container also).   // Create a sample docker environment
- `docker exec -it sample-container sh -c "echo 'Hello, Docker Volume!' > /data/sample.txt"`. // Add sample data to volume 

### By Docker Desktop app:
- Create docker container 
- Cretae volume in that container 
- Add data in the volume

- Test the backup script.
- Edit the volume data and again backup volume.
- Run the restore script to check the volume is restored with new data.
