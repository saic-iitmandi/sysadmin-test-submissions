This is my attempt on the first question of Sysadmin 25-26

In this challenge we have been given a virtual machine with user level clearance to it. The objective was to find the flag in the present in the root/flag.txt.

So i start by importing the Virtual machine in my Virtual Box, Then the first thing i do is set up the network adapters. One to NAT and other to Host-only adapter.

Now i start the VM and enter the username and password given. Now what i have is a ubuntu system with user level access.

I open the terminal in the VM and give some basic commands like "whoami" and "groups".
Now i check if i have sudo access. We don't!

So,I find some ways in which i could move forward with this problem those being:
1.SUID Binary Abuse
2.Cron Job Hijacking
3.Writable System Files
4.Kernel Exploits


So i started with SUID enumeration.
I used the command "find / -perm -4000 -type f 2>/dev/null" to find all the suid binaries and "find / -perm -2000 -type f 2>/dev/null" to find SGID binaries.
Enumeration of SUID binaries revealed only standard Ubuntu system utilities.
No misconfigured SUID binaries capable of spawning a shell or executing arbitrary commands were present.




So I went forward to the cron job hacking
Direct access to /etc/crontab was restricted for non-privileged users

Therefore, cron-related enumeration was performed by inspecting cron execution directories such as /etc/cron.daily and /etc/cron.d, which may contain scripts executed with root privileges.”

The /etc/cron.daily directory was inspected for scripts executed by root.
Only a non-executable anacron file owned by root was present, with no writable permissions for unprivileged users.
Therefore, privilege escalation via cron.daily was ruled out.


Since i couldn't find any vulnerabilities i moved forward to World-writable root-owned files
I use commands "find / -type f -user root -perm -o+w 2>/dev/null" and "find / -type d -user root -perm -o+w 2>/dev/null"

The find command returned numerous entries under /proc, which is a virtual filesystem managed by the kernel.
These entries do not represent persistent files and cannot be exploited for privilege escalation.
Therefore, all /proc results were excluded from consideration.

So now i moved towards my last option kernel exploit.
The first thing to check the kernel version which turned out to be "4.4.0-148-generic" which was a old one and could be exploited
Since the kernel version on the VM was an older version in it I found a kernel exploit "https://www.exploit-db.com/exploits/39772" and downloaded it on the VM, and unzipped the file.
I went to the. file's Directory and untared the exploit and then went inside the exploit's directory and then i compile the script but that give me an error because the fuse package was not found.

Then i after a lot of time of searching on how to solve this problem i found that i do have the fuse files on the virtual but the compile was not showing them as they were at a non standard location
so now i gave the command
"gcc -I /usr/src/linux-headers-4.4.0-148/include/uapi \
    -I /usr/src/linux-headers-4.4.0-148/include \
    doubleput.c hello.c -o exploit_bin"

but it was still giving me an error so i decided to change the script of compile.sh using nano,
where i changed the first line to "gcc -o hello hello.c -Wall -std=gnu99 -I
/usr/include/Linux" and the second line to "gcc -o doubleput doubleput.c -Wall -I /usr/src/linux-headers-4.4.0-148/include/uapi" but it was still giving me the error.
So after repeating this same process for lot of time and trying to solve the error,changing the nano scripts I still couldn't find the solution to the problem.
Kernel exploit was my last option and i could not find any way to move forward so i gave up on this question







