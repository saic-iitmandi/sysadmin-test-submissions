First step was installing docker in my Ubuntu system.
- Wrote the code dockerBackupRestore.sh which is the file to access and run all the code in an easier and organised method
- `chmod +x dockerBackupRestore.sh` to convert the .sh file into an executable file.
- Created backup using `sudo ./dockerBackupRestore.sh backup`
- Restore the backup `sudo ./dockerBackupRestore.sh restore`

# Testing basic functionality
- `sudo docker run -d --name my_test_container -v my_test_volume:/data alpine sh -c "echo 'Hello World' > /data/test.txt && sleep 3600"`
- This created a new file in the docker /data/test.txt and wrote "Hello world" in it essentially
- Running backup code `sudo ./dockerBackupRestore.sh backup`
- Removing the container and the volume from backup `sudo docker rm -f my_test_container` and `sudo docker volume rm my_test_volume`
- Restoring the data `sudo ./dockerBackupRestore.sh restore`
- Verifying if the data is restored or not `sudo docker run --rm -v my_test_volume:/data alpine cat /data/test.txt`
- This displays the expected output of "Hello World"

# Viewing the logs
- `sudo cat /var/log/docker_backup_restore.log`

# Automatic backup every 24h at midnight with a cron expression
- Opening the cron expression editor using `crontab -e`
- Type the code in 'cronexp.txt' file in there and save everything.
- Checked cron expressions running using `crontab -l`

- I didn't really get much issues for this problem ;-;