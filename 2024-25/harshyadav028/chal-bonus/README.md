## BONUS CHALLENGE:

### Tasks done:
1. Created a python script to enumerates into the drive or any directory and log the files and folders names in the _basic_v_log_file.log_.
2. Define a function inside the _script.py_ _upload_to_gofile_ which uploads _basic_v_log_file.log_ log file to a server which converts its link and by clicking that link you can see the log file content easily without any efforts of google drive api setup and OAuth from console.cloud.google.com.
3. Created a python script _monitor_external_drive.py_ to monitor when an external drive is connected to the system and then stored all the new drives or known drives connected names to _external_drive_monitor.log_.

### Approach:
1. After reading the challenge, I realized to break the challenge into five parts: 
- Enumerating the files and folders name present in the directory and storing them in the log file.
- Uploading the log file which was created online so that anyone can access that file easily.
- Creating a python script which monitor the external drives and log drive names to the _external_drive_monitor.log_ log file 
- Create a script which runs in background and start automatically when the system is powered on or rebooted.
- Script which search for "_lol_" folder in the drive and if found copy its content and also upload it online.
2.  Creating a script which enumerates the files and folders name from the specified directory and store them in a  log file is a simple task:
- You can go through the _script.py_ its is self-explaining code.
3. Task of uploading the log file online for everyone access seems easy but is a weird task to me:
- While searching the alternative of google drive I found file.io website but while reading the website docs I got to know that this website is sold to some other company/website(LimeWire) which offers this service but is paid.
- Then I searched for other alternative like transfer.sh, anon files etc. but these services were down or not available.
- Finally after lots of effortful searching, I found Gofile.io wich id still in use and there is no need to create account also.
- I defined a function to upload log file which ahas a server provides by Gofile.io linked which generated a link when called from which we can access the contents which we have uploaded.
4. Created a script which monitor external drives:
- Get to know about _psutil_ python library  (for monitoring system hardware)
- Used in-built functions like _psutil.disk_partitions()_ for checking for the external drive connected.
- Set up a log message function which time to time log about the new drives connected to the system.
5. Finally imported the enumerates function in monitor_external_drive script and use dit to log all the files and folders names present in that drive with drive name.

### Improvements:
1. The set up of python script 	which should run as a background service (daemon) and start automatically whenever the system is powered on or rebooted.
2. The task which includes extracting and copying the content of folder named “_lol_” if it exists is pending.

