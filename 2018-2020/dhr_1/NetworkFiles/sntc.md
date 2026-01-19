
Starting Nmap 7.60 ( https://nmap.org ) at 2018-01-31 22:01 IST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 22:01
Completed NSE at 22:01, 0.00s elapsed
Initiating NSE at 22:01
Completed NSE at 22:01, 0.00s elapsed
Initiating Ping Scan at 22:01
Scanning 14.139.34.11 [4 ports]
Completed Ping Scan at 22:01, 0.22s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 22:01
Completed Parallel DNS resolution of 1 host. at 22:01, 13.00s elapsed
Initiating SYN Stealth Scan at 22:01
Scanning 14.139.34.11 [1000 ports]
Discovered open port 22/tcp on 14.139.34.11
Discovered open port 53/tcp on 14.139.34.11
Discovered open port 8080/tcp on 14.139.34.11
Discovered open port 80/tcp on 14.139.34.11
Increasing send delay for 14.139.34.11 from 0 to 5 due to 12 out of 38 dropped probes since last increase.
Increasing send delay for 14.139.34.11 from 5 to 10 due to 19 out of 62 dropped probes since last increase.
Increasing send delay for 14.139.34.11 from 10 to 20 due to 13 out of 43 dropped probes since last increase.
Increasing send delay for 14.139.34.11 from 20 to 40 due to 11 out of 25 dropped probes since last increase.
Increasing send delay for 14.139.34.11 from 40 to 80 due to max_successful_tryno increase to 4
Increasing send delay for 14.139.34.11 from 80 to 160 due to 11 out of 35 dropped probes since last increase.
Increasing send delay for 14.139.34.11 from 160 to 320 due to 11 out of 23 dropped probes since last increase.
SYN Stealth Scan Timing: About 18.10% done; ETC: 22:04 (0:02:20 remaining)
SYN Stealth Scan Timing: About 27.32% done; ETC: 22:05 (0:02:42 remaining)
SYN Stealth Scan Timing: About 43.97% done; ETC: 22:06 (0:02:27 remaining)
SYN Stealth Scan Timing: About 53.37% done; ETC: 22:06 (0:02:07 remaining)
SYN Stealth Scan Timing: About 62.75% done; ETC: 22:06 (0:01:44 remaining)
SYN Stealth Scan Timing: About 71.98% done; ETC: 22:06 (0:01:20 remaining)
SYN Stealth Scan Timing: About 81.28% done; ETC: 22:06 (0:00:54 remaining)
Completed SYN Stealth Scan at 22:06, 307.14s elapsed (1000 total ports)
Initiating Service scan at 22:06
Scanning 4 services on 14.139.34.11
Completed Service scan at 22:06, 7.71s elapsed (4 services on 1 host)
Initiating OS detection (try #1) against 14.139.34.11
Retrying OS detection (try #2) against 14.139.34.11
Initiating Traceroute at 22:07
Completed Traceroute at 22:07, 3.08s elapsed
Initiating Parallel DNS resolution of 9 hosts. at 22:07
Completed Parallel DNS resolution of 9 hosts. at 22:07, 13.00s elapsed
NSE: Script scanning 14.139.34.11.
Initiating NSE at 22:07
Completed NSE at 22:07, 9.27s elapsed
Initiating NSE at 22:07
Completed NSE at 22:07, 0.00s elapsed
Nmap scan report for 14.139.34.11
Host is up (0.18s latency).
Not shown: 994 closed ports
PORT     STATE    SERVICE      VERSION
22/tcp   open     ssh          OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 5b:ab:3b:5a:f7:f8:d6:14:35:f4:a2:33:23:4c:14:d5 (RSA)
|   256 da:0d:d4:18:e8:ba:6f:5c:5f:e7:74:d7:43:6a:a5:7d (ECDSA)
|_  256 b3:73:da:f5:1c:7f:8d:35:9e:68:d4:af:4c:c5:19:18 (EdDSA)
53/tcp   open     domain       ISC BIND 9.10.3-P4-Ubuntu
| dns-nsid: 
|_  bind.version: 9.10.3-P4-Ubuntu
80/tcp   open     http         nginx 1.10.3 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: nginx/1.10.3 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
8080/tcp open     http         Apache httpd 2.4.10 ((Debian))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Did not follow redirect to http://sntc.iitmandi.ac.in:8080/index.php/Main_Page
Aggressive OS guesses: Linux 3.11 - 4.1 (91%), Linux 3.13 (89%), Linux 3.16 (88%), Linux 4.4 (87%), Linux 2.6.32 (87%), Linux 3.2 - 3.8 (87%), Linux 3.8 (87%), WatchGuard Fireware 11.8 (87%), IPFire 2.11 firewall (Linux 2.6.32) (87%), Linux 3.10 - 3.12 (87%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 48.339 days (since Thu Dec 14 13:59:23 2017)
Network Distance: 14 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 443/tcp)
HOP RTT      ADDRESS
1   2.00 ms  gateway (192.168.43.1)
2   ... 3
4   38.87 ms 10.206.30.229
5   51.96 ms 125.21.210.61
6   52.28 ms 182.79.190.73
7   64.72 ms 218.100.48.28
8   65.02 ms 182.19.110.54
9   53.47 ms 118.185.99.33
10  ... 12
13  59.20 ms 14.139.34.1
14  54.34 ms 14.139.34.11

NSE: Script Post-scanning.
Initiating NSE at 22:07
Completed NSE at 22:07, 0.00s elapsed
Initiating NSE at 22:07
Completed NSE at 22:07, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 373.07 seconds
           Raw packets sent: 1248 (56.808KB) | Rcvd: 1214 (52.244KB)
