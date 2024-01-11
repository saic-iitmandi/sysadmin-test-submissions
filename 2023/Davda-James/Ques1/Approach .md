* After downloading ova file and virtualbox I imported ova file into virtualbox and machine boots.
* Then I logged in as Guest User into Ubuntu machine.
* I tried easy passwd for root user access like root,admin,ubuntu,kali etc. but I know that I will failed and obviously no doubt I did.
* Then after I run the command `ip addr` command in terminal then I got the ip address of the machine. 
* Also I am not able to see any page or login that I have to crack ..
~~~
Nmap scan report for 192.168.29.45
Host is up (0.020s latency).
All 1000 scanned ports on 192.168.29.45 are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Nmap scan report for 192.168.29.47
Host is up (0.0086s latency).
All 1000 scanned ports on 192.168.29.47 are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Nmap scan report for 192.168.29.64
Host is up (0.00022s latency).
All 1000 scanned ports on 192.168.29.64 are in ignored states.
Not shown: 1000 closed tcp ports (conn-refused)

Nmap scan report for 192.168.29.72
Host is up (0.0040s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 256 IP addresses (5 hosts up) scanned in 155.74 seconds
~~~

* This is the ip address of target machine `192.168.29.72`  with http port 80 open.
* I search it in browser with http port 80, I found a page about Xenia which is mascot for linux.
* Also I am not able to see any page or login that I have to crack ..
