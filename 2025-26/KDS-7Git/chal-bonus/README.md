## Explanation of the Approach

### Design Choices
1. I Used Raw TCP sockets to connect and communicate over a dynamic dns address (by duckDNS). I also set the priority class to high so that response delay could be minimized. 

2. It Runs powershell subprocess for the getting the execution output. Also using raw sockets helped minimize the visibility and bypass windows defender. (No Defender Popups visible during testing)

3. The host should be listening on the port 4444 using `nc -lvp 4444` and as soon as the target runs the script and/or restarts the pc, the host will recieve a `connected to <IP> 4444` message on the terminal. Host can send any arbitrary command over that and get the output correspondingly.

4. The startup script is copied into LOCALAPPDATA directory in the target OS, and runs as powershell.exe witht the name of Windows Update Service to reduce risks of Suspicion.

5. The script prints nothing on the target OS while executing and returns as soon as the execution completes. This reduces the risk of suspicion from the Target User. A hanging check is also applied which checks if any such case then aborts the operation. (less Suspicion)

6. Finally, since we do not have direct access to the target system's processes or registry, I chose to persist the tunnel using Windows scheduled tasks, which ensures that it starts up automatically on OS boot and persists as long as possible.

### Challenges Encountered
1. The first and biggest challenge was that chatGPT and Gemini were not responding to any code related-query related to this reverse tunnelling challenge.

2. I struggled since Initially I had no knowledge of the PowerShell commands and such commands were flagged by the AI models, so they did not responded even with some help for such commands. (e.g. how to make the command run without showing logs, etc)

3. The IP address of the host may change so the script must not contain the direct raw IP. But, I found an easy, free to use solution which was DDNS.

### Assumptions and Limitations
1. The first and very bold assumption that the scripts make is the Admin Privelages, without which it will fail to run. This was done to ensure the connection survives reboot.

2. Every time the target tries to connect to the host, the latter should have to be listening, delay in which might lead to failure to connect.

3. When the script is ran the connection will be until the powershell is not closed and will be restarted once the target reboots.

4. Once disconnected there is no way to regain connection, until rerun of the script or reboot (if ran once with admin).

5. Target User can check the running pid no. using netstat and use that to check the process on task manager, where it can be stopped, till next reboot.
