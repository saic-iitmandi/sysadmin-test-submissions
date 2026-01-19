# Challenge 1 – Gain Access to a Remote

## Objective
The objective of this challenge was to analyze the provided Helios virtual machine(https://drive.google.com/file/d/1pN_jN7UCKShA6XbkrXWlnc1smIOONNB6/view?usp=sharing), enumerate exposed services, and identify potential security weaknesses and gain root privileges to find flag present as root/flag.txt.

## Approach
Systematic enumeration of the operating system, running services, and web applications was performed from a low-privileged user context.

## Tools Used
- Linux command-line utilities
- curl
- Oracle VirtualBox
  
## Linux-Commands Used
This section lists all Linux commands used during the enumeration and analysis phase, along with brief one-line explanations.

### `whoami`
Displays the username of the currently logged-in user.

### `id`
Shows the user ID (UID), group ID (GID), and group memberships of the current user.

### `groups`
Lists all groups that the current user belongs to.

### `uname -a`
Displays detailed system information including kernel version and system architecture.

### `cat`
Reads and displays the contents of a file.

### `ls`
Lists files and directories in the current directory.

### `ls -l`
Lists files and directories with detailed information such as permissions, owner, and size.

### `ls -lt`
Lists files sorted by modification time, showing the most recent first.

### `pwd`
Displays the full path of the current working directory.

### `cd`
Changes the current working directory.

### `ss -tulnp`
Displays all listening network ports along with the associated processes.

### `netstat -tulnp`
Shows network connections and listening ports (legacy alternative to `ss`).

### `ip a`
Displays network interfaces and assigned IP addresses.

### `curl`
Sends HTTP requests to a server and prints the response.

### `curl -i`
Sends an HTTP request and includes response headers in the output.

### `curl -X METHOD`
Sends an HTTP request using a specified method such as GET or POST.

### `ps aux`
Displays all running processes along with their owners and resource usage.

### `grep`
Searches for a specific pattern within command output or files.

### `find`
Searches for files and directories based on specified conditions.

### `find / -perm -4000`
Finds files with the SUID (Set User ID) permission enabled.

### `getcap`
Displays Linux capabilities assigned to executable files.

### `env`
Displays all environment variables for the current session.

### `history`
Shows the list of previously executed commands by the user.

### `ls /var/www`
Lists files inside the default web server directory.

### `ls /opt`
Lists optional or third-party application directories.

### `ls /dev/shm`
Displays files in the shared memory filesystem used for inter-process communication.

### `ls /run/shm`
Shows the runtime shared memory mount point.

### `exit`
Terminates the current shell session.

