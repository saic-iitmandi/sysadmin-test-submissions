
Starting Nmap 7.60 ( https://nmap.org ) at 2018-01-31 14:34 IST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:34
Completed NSE at 14:34, 0.00s elapsed
Initiating NSE at 14:34
Completed NSE at 14:34, 0.00s elapsed
Initiating Ping Scan at 14:34
Scanning 14.139.34.10 [4 ports]
Completed Ping Scan at 14:34, 0.23s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:34
Completed Parallel DNS resolution of 1 host. at 14:34, 13.00s elapsed
Initiating SYN Stealth Scan at 14:34
Scanning 14.139.34.10 [1000 ports]
Discovered open port 21/tcp on 14.139.34.10
Discovered open port 22/tcp on 14.139.34.10
Discovered open port 443/tcp on 14.139.34.10
Discovered open port 80/tcp on 14.139.34.10
Increasing send delay for 14.139.34.10 from 0 to 5 due to 12 out of 38 dropped probes since last increase.
Increasing send delay for 14.139.34.10 from 5 to 10 due to 30 out of 98 dropped probes since last increase.
Increasing send delay for 14.139.34.10 from 10 to 20 due to 11 out of 24 dropped probes since last increase.
Increasing send delay for 14.139.34.10 from 20 to 40 due to 11 out of 26 dropped probes since last increase.
Increasing send delay for 14.139.34.10 from 40 to 80 due to 11 out of 24 dropped probes since last increase.
SYN Stealth Scan Timing: About 32.52% done; ETC: 14:36 (0:01:04 remaining)
Increasing send delay for 14.139.34.10 from 80 to 160 due to 70 out of 233 dropped probes since last increase.
Increasing send delay for 14.139.34.10 from 160 to 320 due to 11 out of 30 dropped probes since last increase.
SYN Stealth Scan Timing: About 45.70% done; ETC: 14:37 (0:01:20 remaining)
Discovered open port 8000/tcp on 14.139.34.10
Discovered open port 8082/tcp on 14.139.34.10
SYN Stealth Scan Timing: About 68.73% done; ETC: 14:38 (0:01:05 remaining)
SYN Stealth Scan Timing: About 78.12% done; ETC: 14:38 (0:00:48 remaining)
Completed SYN Stealth Scan at 14:39, 274.03s elapsed (1000 total ports)
Initiating Service scan at 14:39
Scanning 6 services on 14.139.34.10
Completed Service scan at 14:39, 12.41s elapsed (6 services on 1 host)
Initiating OS detection (try #1) against 14.139.34.10
Retrying OS detection (try #2) against 14.139.34.10
Initiating Traceroute at 14:39
Completed Traceroute at 14:39, 3.06s elapsed
Initiating Parallel DNS resolution of 9 hosts. at 14:39
Completed Parallel DNS resolution of 9 hosts. at 14:39, 13.00s elapsed
NSE: Script scanning 14.139.34.10.
Initiating NSE at 14:39
Completed NSE at 14:40, 61.16s elapsed
Initiating NSE at 14:40
Completed NSE at 14:40, 0.01s elapsed
Nmap scan report for 14.139.34.10
Host is up (0.047s latency).
Not shown: 992 closed ports
PORT     STATE    SERVICE      VERSION
21/tcp   open     ftp          vsftpd 3.0.3
| ssl-cert: Subject: commonName=*.iitmandi.ac.in
| Subject Alternative Name: DNS:*.iitmandi.ac.in, DNS:iitmandi.ac.in
| Issuer: commonName=Go Daddy Secure Certificate Authority - G2/organizationName=GoDaddy.com, Inc./stateOrProvinceName=Arizona/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2016-12-05T07:00:00
| Not valid after:  2019-12-05T07:00:00
| MD5:   7da5 f55b 913d 3a93 456b 0a32 7dcd 1cd8
|_SHA-1: 0e2e fb1d fb42 5df8 4c47 4095 9a84 527a df34 5592
|_ssl-date: TLS randomness does not represent time
22/tcp   open     tcpwrapped
80/tcp   open     http         Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
139/tcp  filtered netbios-ssn
443/tcp  open     ssl/http     Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=*.iitmandi.ac.in
| Subject Alternative Name: DNS:*.iitmandi.ac.in, DNS:iitmandi.ac.in
| Issuer: commonName=Go Daddy Secure Certificate Authority - G2/organizationName=GoDaddy.com, Inc./stateOrProvinceName=Arizona/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2016-12-05T07:00:00
| Not valid after:  2019-12-05T07:00:00
| MD5:   7da5 f55b 913d 3a93 456b 0a32 7dcd 1cd8
|_SHA-1: 0e2e fb1d fb42 5df8 4c47 4095 9a84 527a df34 5592
|_ssl-date: TLS randomness does not represent time
445/tcp  filtered microsoft-ds
8000/tcp open     http         Gunicorn 19.4.5
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
|_http-open-proxy: Proxy might be redirecting requests
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: gunicorn/19.4.5
| http-title: Log In - IIT-Mandi-Cloud
|_Requested resource was http://14.139.34.10:8000/accounts/login/?next=/
8082/tcp open     http         Octoshape P2P streaming web service
|_http-title: Site doesn't have a title.
Aggressive OS guesses: Linux 3.11 - 4.1 (93%), Linux 3.13 (90%), Linux 3.16 (88%), Linux 3.10 - 3.12 (88%), Linux 4.4 (88%), Linux 2.6.32 (88%), Linux 3.2 - 3.8 (88%), Linux 3.8 (88%), WatchGuard Fireware 11.8 (88%), IPFire 2.11 firewall (Linux 2.6.32) (87%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 48.269 days (since Thu Dec 14 08:13:49 2017)
Network Distance: 14 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Unix

TRACEROUTE (using port 23/tcp)
HOP RTT      ADDRESS
1   2.62 ms  gateway (192.168.43.1)
2   ... 3
4   40.44 ms 10.206.30.213
5   40.85 ms 125.21.210.61
6   42.00 ms 182.79.188.40
7   65.67 ms 218.100.48.28
8   67.19 ms 182.19.110.54
9   39.53 ms 118.185.99.33
10  ... 12
13  42.96 ms 14.139.34.1
14  40.15 ms 14.139.34.10

NSE: Script Post-scanning.
Initiating NSE at 14:40
Completed NSE at 14:40, 0.00s elapsed
Initiating NSE at 14:40
Completed NSE at 14:40, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 382.34 seconds
           Raw packets sent: 1519 (71.342KB) | Rcvd: 1242 (51.778KB)
