
Starting Nmap 7.60 ( https://nmap.org ) at 2018-01-31 14:33 IST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:33
Completed NSE at 14:33, 0.00s elapsed
Initiating NSE at 14:33
Completed NSE at 14:33, 0.00s elapsed
Initiating Ping Scan at 14:33
Scanning 14.139.34.8 [4 ports]
Completed Ping Scan at 14:33, 0.43s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:33
Completed Parallel DNS resolution of 1 host. at 14:33, 13.00s elapsed
Initiating SYN Stealth Scan at 14:33
Scanning 14.139.34.8 [1000 ports]
Discovered open port 80/tcp on 14.139.34.8
Discovered open port 443/tcp on 14.139.34.8
Discovered open port 10000/tcp on 14.139.34.8
Discovered open port 389/tcp on 14.139.34.8
Completed SYN Stealth Scan at 14:33, 15.06s elapsed (1000 total ports)
Initiating Service scan at 14:34
Scanning 4 services on 14.139.34.8
Completed Service scan at 14:34, 12.39s elapsed (4 services on 1 host)
Initiating OS detection (try #1) against 14.139.34.8
Retrying OS detection (try #2) against 14.139.34.8
Initiating Traceroute at 14:34
Completed Traceroute at 14:34, 3.07s elapsed
Initiating Parallel DNS resolution of 9 hosts. at 14:34
Completed Parallel DNS resolution of 9 hosts. at 14:34, 13.00s elapsed
NSE: Script scanning 14.139.34.8.
Initiating NSE at 14:34
Completed NSE at 14:35, 30.74s elapsed
Initiating NSE at 14:35
Completed NSE at 14:35, 0.00s elapsed
Nmap scan report for 14.139.34.8
Host is up (0.066s latency).
Not shown: 994 filtered ports
PORT      STATE  SERVICE  VERSION
53/tcp    closed domain
80/tcp    open   http     Apache httpd 2.2.22 ((Debian))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.2.22 (Debian)
|_http-title: Site doesn't have a title (text/html).
389/tcp   open   ldap     OpenLDAP 2.2.X - 2.3.X
443/tcp   open   ssl/http Apache httpd 2.2.22 ((Debian))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.2.22 (Debian)
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
|_ssl-date: 2018-01-31T09:04:29+00:00; -4s from scanner time.
3306/tcp  closed mysql
10000/tcp open   http     MiniServ 1.850 (Webmin httpd)
|_http-favicon: Unknown favicon MD5: C4B82D3EFFE87461927A756B404A54E5
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
Aggressive OS guesses: Linux 3.2 - 3.8 (93%), Linux 3.8 (93%), WatchGuard Fireware 11.8 (93%), Linux 3.5 (91%), Linux 3.1 - 3.2 (90%), Linux 2.6.32 - 2.6.39 (90%), Linux 3.0 - 3.2 (90%), Linux 2.6.32 (88%), Linux 2.6.32 or 3.10 (88%), Linux 3.0 or 3.5 (88%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 47.891 days (since Thu Dec 14 17:11:59 2017)
Network Distance: 14 hops
TCP Sequence Prediction: Difficulty=257 (Good luck!)
IP ID Sequence Generation: All zeros

Host script results:
|_clock-skew: mean: -4s, deviation: 0s, median: -4s

TRACEROUTE (using port 3306/tcp)
HOP RTT       ADDRESS
1   2.31 ms   gateway (192.168.43.1)
2   ... 3
4   28.60 ms  10.206.30.213
5   179.79 ms 125.21.210.61
6   38.40 ms  182.79.234.58
7   58.85 ms  218.100.48.28
8   58.91 ms  182.19.110.54
9   33.76 ms  118.185.99.33
10  ... 12
13  41.50 ms  14.139.34.1
14  144.60 ms 14.139.34.8

NSE: Script Post-scanning.
Initiating NSE at 14:35
Completed NSE at 14:35, 0.00s elapsed
Initiating NSE at 14:35
Completed NSE at 14:35, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 93.16 seconds
           Raw packets sent: 2119 (97.658KB) | Rcvd: 70 (4.642KB)
