# Making the python code
- Coding the base part was easy by studying the docs and ofc chatgpt on how to use os and copy directories. 
- It scans every 2s (so that its not much resource intensive and it doesn't show up on the top in any resource monitor) whether there is any new drives. If there is not, it just keeps scanning otherwise it activates the setup.
- If the 'lol' folder was found, it saved the folder to the System/Logs folder and also wrote it in the drive_log.
- Also compressed the folder into .zip and then pushed it to the azure storage account by the name '{currentUnix}-lol'
- The main issue was finding a suitable easy cloud storage. All the ones suggested on the google were either too complicated or just didn't work lol. Ended up using Azure after a lot of search cuz I have used this earlier for some projects as well for storing stuff so just copied over the code frmo there lol.

# Hiding it in the system
- Created a task in Windows Task Scheduler.
- Steps for tht were:
1) 'Create Task' 
2) Wrote the name as "System Process" to disguise it even if someone manages to find it.
3) Hidden and configure for windows 10
4) Go to Triggers tab and set the trigger to "On startup" so the script automatically starts when the computer is powered on hehe.
5) Go to Actions and set it to strt a program. Chose the python.exe file in it and put the path of the python file i just coded.
6) Set the conditions to always be on no matter if the user is signed in or not.
7) Set the settings to restart it 10 times every 1 minute if it doesn't work.

# What else I did
- Hid all the errors, no logs using print. Only stores the file contents in the System/Logs
- If azure doesn't work, itll simply save the folder and ignore the azure thing.
- Using task scheduler doesn't even show up in Task Manager which is amazing for what we are doing.