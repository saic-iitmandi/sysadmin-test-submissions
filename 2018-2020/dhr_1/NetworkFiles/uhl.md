
Starting Nmap 7.60 ( https://nmap.org ) at 2018-01-31 22:02 IST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 22:02
Completed NSE at 22:02, 0.00s elapsed
Initiating NSE at 22:02
Completed NSE at 22:02, 0.00s elapsed
Initiating Ping Scan at 22:02
Scanning 14.139.34.17 [4 ports]
Completed Ping Scan at 22:02, 0.23s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 22:02
Completed Parallel DNS resolution of 1 host. at 22:02, 13.00s elapsed
Initiating SYN Stealth Scan at 22:02
Scanning 14.139.34.17 [1000 ports]
Discovered open port 80/tcp on 14.139.34.17
Discovered open port 22/tcp on 14.139.34.17
Discovered open port 5900/tcp on 14.139.34.17
Increasing send delay for 14.139.34.17 from 0 to 5 due to 29 out of 96 dropped probes since last increase.
Increasing send delay for 14.139.34.17 from 5 to 10 due to max_successful_tryno increase to 4
Increasing send delay for 14.139.34.17 from 10 to 20 due to 13 out of 41 dropped probes since last increase.
Increasing send delay for 14.139.34.17 from 20 to 40 due to max_successful_tryno increase to 5
Increasing send delay for 14.139.34.17 from 40 to 80 due to 11 out of 26 dropped probes since last increase.
Increasing send delay for 14.139.34.17 from 80 to 160 due to 11 out of 27 dropped probes since last increase.
SYN Stealth Scan Timing: About 38.00% done; ETC: 22:04 (0:00:51 remaining)
Increasing send delay for 14.139.34.17 from 160 to 320 due to 56 out of 186 dropped probes since last increase.
SYN Stealth Scan Timing: About 49.06% done; ETC: 22:04 (0:01:06 remaining)
Discovered open port 5800/tcp on 14.139.34.17
SYN Stealth Scan Timing: About 69.66% done; ETC: 22:05 (0:00:57 remaining)
SYN Stealth Scan Timing: About 79.79% done; ETC: 22:06 (0:00:41 remaining)
Completed SYN Stealth Scan at 22:06, 244.66s elapsed (1000 total ports)
Initiating Service scan at 22:06
Scanning 4 services on 14.139.34.17
Completed Service scan at 22:06, 8.06s elapsed (4 services on 1 host)
Initiating OS detection (try #1) against 14.139.34.17
Retrying OS detection (try #2) against 14.139.34.17
Initiating Traceroute at 22:07
Completed Traceroute at 22:07, 3.07s elapsed
Initiating Parallel DNS resolution of 9 hosts. at 22:07
Completed Parallel DNS resolution of 9 hosts. at 22:07, 13.00s elapsed
NSE: Script scanning 14.139.34.17.
Initiating NSE at 22:07
Completed NSE at 22:08, 38.67s elapsed
Initiating NSE at 22:08
Completed NSE at 22:08, 0.00s elapsed
Nmap scan report for 14.139.34.17
Host is up (0.23s latency).
Not shown: 994 closed ports
PORT     STATE    SERVICE      VERSION
22/tcp   open     ssh          OpenSSH 5.9p1 Debian 5ubuntu1.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 67:ff:5b:e6:47:21:2a:fe:11:75:38:97:87:bc:fa:3b (DSA)
|   2048 01:af:06:2f:7b:d9:11:5f:9a:38:05:63:dd:cd:0d:b1 (RSA)
|_  256 29:d2:ce:a2:28:38:ce:0a:6a:0b:62:b5:f4:64:c8:08 (ECDSA)
80/tcp   open     http         Apache httpd 2.2.22 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
5800/tcp open     vnc-http     x11vnc
| http-methods: 
|_  Supported Methods: HEAD POST OPTIONS
5900/tcp open     vnc          VNC (protocol 3.7)
Aggressive OS guesses: Linux 3.2 - 3.8 (91%), Linux 3.8 (91%), WatchGuard Fireware 11.8 (91%), Linux 3.1 - 3.2 (90%), Linux 2.6.32 - 2.6.39 (89%), Linux 3.5 (89%), Linux 3.0 - 3.2 (88%), Linux 2.6.32 (87%), Linux 3.0 (87%), Linux 3.0 or 3.5 (87%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 49.120 days (since Wed Dec 13 19:15:16 2017)
Network Distance: 14 hops
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 143/tcp)
HOP RTT      ADDRESS
1   98.78 ms gateway (192.168.43.1)
2   ... 3
4   39.05 ms 10.206.30.197
5   37.87 ms 125.21.170.189
6   40.44 ms 182.79.201.85
7   65.91 ms 218.100.48.28
8   63.67 ms 182.19.110.54
9   48.61 ms 118.185.99.33
10  ... 12
13  62.72 ms 14.139.34.1
14  63.31 ms 14.139.34.17

NSE: Script Post-scanning.
Initiating NSE at 22:08
Completed NSE at 22:08, 0.00s elapsed
Initiating NSE at 22:08
Completed NSE at 22:08, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 336.56 seconds
           Raw packets sent: 1445 (65.464KB) | Rcvd: 1396 (58.962KB)
