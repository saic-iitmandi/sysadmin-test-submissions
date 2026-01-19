
Starting Nmap 7.60 ( https://nmap.org ) at 2018-01-31 14:16 IST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:16
Completed NSE at 14:16, 0.00s elapsed
Initiating NSE at 14:16
Completed NSE at 14:16, 0.00s elapsed
Initiating Ping Scan at 14:16
Scanning 14.139.34.4 [4 ports]
Completed Ping Scan at 14:16, 0.23s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:16
Completed Parallel DNS resolution of 1 host. at 14:16, 13.00s elapsed
Initiating SYN Stealth Scan at 14:16
Scanning 14.139.34.4 [1000 ports]
Discovered open port 8080/tcp on 14.139.34.4
Discovered open port 22/tcp on 14.139.34.4
Discovered open port 25/tcp on 14.139.34.4
Discovered open port 80/tcp on 14.139.34.4
Increasing send delay for 14.139.34.4 from 0 to 5 due to 16 out of 51 dropped probes since last increase.
Increasing send delay for 14.139.34.4 from 5 to 10 due to 83 out of 276 dropped probes since last increase.
Increasing send delay for 14.139.34.4 from 10 to 20 due to max_successful_tryno increase to 4
Increasing send delay for 14.139.34.4 from 20 to 40 due to 11 out of 30 dropped probes since last increase.
Increasing send delay for 14.139.34.4 from 40 to 80 due to max_successful_tryno increase to 5
Increasing send delay for 14.139.34.4 from 80 to 160 due to 11 out of 32 dropped probes since last increase.
Increasing send delay for 14.139.34.4 from 160 to 320 due to 11 out of 25 dropped probes since last increase.
SYN Stealth Scan Timing: About 28.74% done; ETC: 14:18 (0:01:17 remaining)
SYN Stealth Scan Timing: About 38.06% done; ETC: 14:19 (0:01:39 remaining)
SYN Stealth Scan Timing: About 62.93% done; ETC: 14:20 (0:01:24 remaining)
SYN Stealth Scan Timing: About 72.07% done; ETC: 14:20 (0:01:07 remaining)
Discovered open port 6001/tcp on 14.139.34.4
SYN Stealth Scan Timing: About 81.11% done; ETC: 14:20 (0:00:47 remaining)
Completed SYN Stealth Scan at 14:21, 272.22s elapsed (1000 total ports)
Initiating Service scan at 14:21
Scanning 5 services on 14.139.34.4
Completed Service scan at 14:23, 150.10s elapsed (5 services on 1 host)
Initiating OS detection (try #1) against 14.139.34.4
Retrying OS detection (try #2) against 14.139.34.4
Initiating Traceroute at 14:23
Completed Traceroute at 14:23, 3.09s elapsed
Initiating Parallel DNS resolution of 9 hosts. at 14:23
Completed Parallel DNS resolution of 9 hosts. at 14:24, 13.00s elapsed
NSE: Script scanning 14.139.34.4.
Initiating NSE at 14:24
Completed NSE at 14:24, 30.30s elapsed
Initiating NSE at 14:24
Completed NSE at 14:24, 1.12s elapsed
Nmap scan report for 14.139.34.4
Host is up (0.058s latency).
Not shown: 993 closed ports
PORT     STATE    SERVICE      VERSION
22/tcp   open     ssh          OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 7d:c3:f1:16:c5:6a:6f:56:7e:9e:db:c4:45:d6:bf:72 (DSA)
|   2048 7f:4e:74:07:37:07:31:1f:e1:e6:e5:26:f2:94:93:ed (RSA)
|   256 b4:08:1e:28:28:91:b5:b1:de:4a:61:a4:14:87:1a:0f (ECDSA)
|_  256 05:a4:20:2b:70:a1:e7:4a:ca:c7:20:47:14:fc:0c:6c (EdDSA)
25/tcp   open     smtp         Postfix smtpd
|_smtp-commands: Library.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, ENHANCEDSTATUSCODES, 8BITMIME, DSN, 
80/tcp   open     http         Apache httpd 2.4.7 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: B8957B00882C0B3CA1F7B1B28E2C69FB
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Library-IIT Mandi
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
6001/tcp open     X11:1?
|_x11-access: ERROR: Script execution failed (use -d to debug)
8080/tcp open     http         Apache httpd 2.4.7 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Koha &rsaquo;                     Log in to Koha
Aggressive OS guesses: Linux 3.11 - 4.1 (91%), Linux 3.13 (88%), Linux 3.16 (88%), Linux 3.10 - 3.12 (87%), Linux 4.4 (87%), Linux 2.6.32 (87%), Linux 3.2 - 3.8 (87%), Linux 3.8 (87%), WatchGuard Fireware 11.8 (87%), IPFire 2.11 firewall (Linux 2.6.32) (86%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 50.206 days (since Tue Dec 12 09:27:46 2017)
Network Distance: 14 hops
TCP Sequence Prediction: Difficulty=257 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: Host:  Library.localdomain; OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 111/tcp)
HOP RTT       ADDRESS
1   3.80 ms   gateway (192.168.43.1)
2   ... 3
4   27.61 ms  10.206.30.213
5   46.87 ms  125.21.210.61
6   47.26 ms  182.79.188.229
7   72.24 ms  218.100.48.28
8   178.27 ms 182.19.110.54
9   59.81 ms  118.185.99.33
10  ... 12
13  60.25 ms  14.139.34.1
14  67.68 ms  14.139.34.4

NSE: Script Post-scanning.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 488.57 seconds
           Raw packets sent: 1355 (63.622KB) | Rcvd: 1407 (68.246KB)
