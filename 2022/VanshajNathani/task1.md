# SAIC SysAdmin Test 
## Task 1. Gain Access to a Remote Server

After booting the machine we want a way to communicate with it. 
An obvious way is via SSH/HTTP ports being open on the machine. To find such ports we perform an nmap scan.

`nmap 192.168.43.0/24`
This scan through all the 256 IPs and finds any open ports on these IPs.

~~~
Starting Nmap 7.92 ( https://nmap.org ) at 2022-11-09 21:11 IST
Nmap scan report for 192.168.43.151
Host is up (0.017s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
53/tcp open  domain

Nmap scan report for 192.168.43.203
Host is up (0.000063s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
21/tcp open  ftp

Nmap scan report for 192.168.43.230
Host is up (0.000085s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
80/tcp open  http
~~~

The IP `192.168.43.203` is the  IP of my machine. Therefore, the IP address `192.168.43.230` must be the IP of our target machine. Our target machine has an open http port.

Hmm! Interesting. Heading to our browser and trying to visit the IP of our machine, we land at a login page. 
Since, no prior login was provided, I created a new login and logged into the site. 
As soon as we login into the local site, we see an alert displaying "**There is a newer version with important security fixes, Please Update CuteNews!**"

After a little bit of googling, I found out that CuteNews had an older version with allowed users to get a reverse shell on the host.

Now we had to find out a way by which we can upload the php script into the server. The website after logging in has options to edit personal options. In this,  there is a place, where we can upload our avatar. Well, here's the key to getting into the machine.

I found a PHP reverse shell code on github by pentestmonkey (https://github.com/pentestmonkey/).
I copied the code into a file named "perfectly\_safe\_avatar.**PHP**", changed the IP to make it same as my machine's and uploaded this file in the avatar box. To my surprise, the website didn't check for the extension of the avatar and just allowed me to upload it.

After uploading the reverse shell script, I needed to know the url from where I could access the file. 
Inspecting the webpage revealed some IP and within it was my script. Its url was <targetmachineIP>/uploads/avatar\_saic\_perfectly\_safe\_avatar.PHP.

So now I had found out a way to get into the machine.

Using netcat, I got a reverse a shell on the target machine. 
Executing the command 'netcap -lvnp 4444' in my terminal and the going to the url "<targetmachineIP>/uploads/avatar\_saic\_perfectly\_safe\_avatar.PHP" gave me a reverse shell on the target machine. 
YEAHH!!

Firtly, I made sure to get an interactive terminal. So I used python for it. Below is the command used.
`/usr/bin/python -c 'import pty; pty.spawn("/bin/bash")'`

## VM1

So, initially when the questions were send to us, the original machine had an issue. It's /etc/passwd file was set to read/write for all users.

All I had to do was to change the contents of this file and remove the password for root.

Ecexuting the following command erased all the content of the /etc/passwd file and added the line in quotes.
`echo "root::0:0::/root:/bin/bash"`

This removed the password from root but had also deleted all other users on the machine.
So I went back to the VM, tried to login as **root** and sure enough I was able to do it. I found out the flag which was in the `/root/fl4g.txt` file.

The contents of the fl4g file were
~~~
***************************
***** You found me !! *****
********** S41C ***********
***************************
~~~
But this was not intended way to get into the machine.

## VM2

The patched machine. 
So this was the patched machine with proper read write permissions on the `/etc/passwd` file

To check for velnerabilities on the machine I checked for exploitable SUIDs using a python script by Syed Umar Arfeen (https://github.com/Anon-Exploiter/SUID3NUM).

Found out that a binary `/usr/sbin/uuidd` had a `-s` tag. My dumbass thought it was a binary which had set uid rights. **DUH!!**

After struggling for around 3hrs I realized there isn't much I could do with the binary

The next day, I checked for the OS and version running on the machine using the `/bin/cat /etc/os-release` command.
The result was:
~~~
NAME="Ubuntu"
VERSION="14.04.2 LTS, Trusty Tahr"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 14.04.2 LTS"
VERSION_ID="14.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
~~~

I googled the following **Ubuntu 14.04.2 root escalation**. The very first result was https://www.exploit-db.com/exploits/37088
It required my to execute this c code on the target machine. I downloaded the code, saved it in a file, hosted a simple python http.server and used wget into my target machine. Compiled the code and executed it.
After a few seconds, I got a shell running as root. **HECK YEA!!** 
The exploit used a race condition to steal the uid from root.
Since I already knew what the flag was, I didn't bother to open the txt file.
