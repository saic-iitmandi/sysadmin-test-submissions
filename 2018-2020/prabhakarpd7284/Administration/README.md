# Task 1
### Step 1
- Rclone<br>
It is an utility to sync files on multiple cloud storage.<br>
Installation - https://rclone.org/install/<br>
`$ sudo curl https://rclone.org/install.sh | sudo bash`<br>
Run `rclone config` and add multiple cloud storage accounts.

### Step 2
- Cron<br>
It is a daemon to execute scheduled commands in linux.<br>
Aim of using cron is to schedule task of running a bash script every 3 hours which sync files to multiple cloud storages.<br>
http://www.unixgeeks.org/security/newbie/unix/cron-1.html<br>
http://man7.org/linux/man-pages/man8/cron.8.html<br>

Run [this script](alljobs.sh) in your terminal. If you see output like below, then you are good to go to next step, else follow the above given links.

![cron jobs all users list](cron_jobs.png)
>`sudo nano cog`<br> 
`SHELL=/bin/bash`<br>
`* */3 * * * cmd`

Replace `cmd` with `cd $file_path && rclone sync $file_name gdrive : $file_name` __i.e.__ terminal command to sync the file every 3 hours.<br>
You can confirm the scheduled job by running [this script](alljobs.sh) in your terminal. It lists all scheduled jobs by all users by cron daemon.

