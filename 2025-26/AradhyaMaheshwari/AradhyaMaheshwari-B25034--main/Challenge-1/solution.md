## Methodology

### Step 1: Login into the VM
Using the given credentials i logged into the VM.

### Step 2: Verify Current User Context
Used whoami to comfirm the identity of logged-in user. Used id and groups to determine whether the user had administrative privileges or belonged to any privileged groups.

### Step 3: Identify Operating System and Kernel Version
Used uname -a , cat /etc/os-release to identify the operating system and kernel version, which helps assess system age and potential vulnerability categories. 
Found out that the system was running Ubuntu 14.04.6 LTS with an older Linux kernel.

### Step 4: Enumerate Listening Services
Used ss -tulnp to identify network services listening on the system and locate potential attack surfaces. The output revealed services listed on ports 80,5000,9000 which indicated the presence of a web application.

### Step 5: Inspect Web Services on localhost
Used curl http://localhost:5000 , curl http://localhost to inspect the application running on ports. The response displays “Helios Internal Dashboard”, indicating a custom internal service.

### Step 6: Inspect HTTP Headers and Server Information
Used curl -i http://localhost , curl -i http://localhost:5000 to identify the web server software and analyze HTTP response headers.
Port 80 was served by nginx, while port 5000 was served by a Python BaseHTTP server.

### Step 7: Test Supported HTTP Methods
curl -X POST http://localhost:5000,
curl -X HEAD http://localhost:5000,
curl -X OPTIONS http://localhost:5000,
They are used to determine which HTTP methods were supported by the application.
Only GET requests were supported. All other methods returned 501 Unsupported Method .

### Step 8: Enumerate Common Application Paths
curl -i http://localhost:5000/status,
curl -i http://localhost:5000/health,
curl -i http://localhost:5000/debug,
to check for hidden endpoints or internal API routes commonly found in server applications.
All tested paths returned 404 Not Found, indicating the application does not use route-based logic.

### Step 9: Inspect Running Processes
Used ps aux to identify running processes and determine whether any services were executing with elevated privileges. Helios-related processes were running as the root user, significantly increasing the impact of any vulnerability.

### Step 10: Locate Application Installation Directory
ls -l /opt,
ls -l /opt/helios,
To locate the installation directory of the Helios application.
Helios was installed under /opt/helios, indicating a custom third-party service.

### Step 11: Inspect Helios Directory Permissions
ls -l /opt/helios/runtime,
ls -l /opt/helios/web,
Used to check file permissions for potential writable directories or misconfigurations. The directories were not writable by the student user, ruling out direct file modification attacks.

### Step 12: Check for Scheduled Tasks (Cron Jobs)
ls -la /etc/cron*,
cat /etc/crontab,
Used to identify any automated tasks running as root that could be abused. No misconfigured or user-writable cron jobs were found.

### Step 13: Check for SUID Binaries
Used find / -perm -4000 -type f 2>/dev/null to locate binaries that execute with root privileges. No unusual or exploitable SUID binaries were discovered.

### Step 14: Inspect Shared Memory and Runtime Locations
Used ls -lt /dev/shm,
ls -lt /run/shm to observe shared memory usage, which is commonly used for inter-process communication in internal automation systems. Shared memory locations were active and owned by root, indicating that Helios likely reacts to system state rather than direct user input.

## Conclusions
In Challenge 1, a systematic enumeration of the provided virtual machine was performed after logging in as a low-privileged user. Initial analysis confirmed that the user did not possess administrative rights, ruling out direct privilege escalation through sudo or group misconfigurations. Network and service enumeration revealed a custom internal web application, identified as the Helios Internal Dashboard, running on localhost ports 80 and 5000, with nginx acting as a reverse proxy to a Python-based backend service. Further investigation showed that the application accepted only GET requests and exposed no interactive user interface, hidden endpoints, or exploitable HTTP methods. Common privilege escalation vectors such as writable directories, misconfigured cron jobs, and SUID binaries were also examined and found to be properly secured. Process inspection confirmed that Helios components were running with root privileges, significantly increasing the potential impact of any vulnerability. Overall, the findings indicate that the system is hardened against conventional exploitation techniques, and any successful privilege escalation would likely stem from a deeper trust-boundary or system-state-based flaw rather than direct user input or configuration errors.
