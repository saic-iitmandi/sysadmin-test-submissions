
Starting Nmap 7.60 ( https://nmap.org ) at 2018-01-31 14:17 IST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:17
Completed NSE at 14:17, 0.00s elapsed
Initiating NSE at 14:17
Completed NSE at 14:17, 0.00s elapsed
Initiating Ping Scan at 14:17
Scanning 14.139.34.6 [4 ports]
Completed Ping Scan at 14:17, 0.23s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:17
Completed Parallel DNS resolution of 1 host. at 14:17, 13.00s elapsed
Initiating SYN Stealth Scan at 14:17
Scanning 14.139.34.6 [1000 ports]
Discovered open port 80/tcp on 14.139.34.6
Discovered open port 443/tcp on 14.139.34.6
Completed SYN Stealth Scan at 14:17, 26.90s elapsed (1000 total ports)
Initiating Service scan at 14:17
Scanning 2 services on 14.139.34.6
Completed Service scan at 14:17, 12.45s elapsed (2 services on 1 host)
Initiating OS detection (try #1) against 14.139.34.6
Retrying OS detection (try #2) against 14.139.34.6
Initiating Traceroute at 14:18
Completed Traceroute at 14:18, 3.06s elapsed
Initiating Parallel DNS resolution of 9 hosts. at 14:18
Completed Parallel DNS resolution of 9 hosts. at 14:18, 13.00s elapsed
NSE: Script scanning 14.139.34.6.
Initiating NSE at 14:18
Completed NSE at 14:18, 3.43s elapsed
Initiating NSE at 14:18
Completed NSE at 14:18, 0.00s elapsed
Nmap scan report for 14.139.34.6
Host is up (0.054s latency).
Not shown: 991 filtered ports
PORT     STATE  SERVICE       VERSION
53/tcp   closed domain
80/tcp   open   http          Apache httpd 2.2.22 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
135/tcp  closed msrpc
143/tcp  closed imap
389/tcp  closed ldap
443/tcp  open   ssl/http      Apache httpd 2.2.22 ((Ubuntu))
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
|_http-server-header: Apache/2.2.22 (Ubuntu)
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
|_ssl-date: 2018-01-31T08:48:17+00:00; -4s from scanner time.
3389/tcp closed ms-wbt-server
5900/tcp closed vnc
5901/tcp closed vnc-1
Aggressive OS guesses: Linux 3.2 - 3.8 (93%), Linux 3.8 (93%), WatchGuard Fireware 11.8 (93%), Linux 3.1 - 3.2 (91%), Linux 3.5 (90%), Linux 2.6.32 - 2.6.39 (90%), Linux 3.0 - 3.2 (89%), Linux 2.6.32 - 3.0 (88%), Linux 2.6.32 (87%), Linux 2.6.32 or 3.10 (87%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 48.792 days (since Wed Dec 13 19:18:10 2017)
Network Distance: 14 hops
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: All zeros

Host script results:
|_clock-skew: mean: -4s, deviation: 0s, median: -4s

TRACEROUTE (using port 143/tcp)
HOP RTT       ADDRESS
1   3.16 ms   gateway (192.168.43.1)
2   ... 3
4   36.97 ms  10.206.30.213
5   44.98 ms  125.21.210.61
6   45.36 ms  182.79.188.43
7   176.90 ms 218.100.48.28
8   75.45 ms  182.19.110.54
9   54.29 ms  118.185.99.33
10  ... 12
13  111.66 ms 14.139.34.1
14  50.01 ms  14.139.34.6

NSE: Script Post-scanning.
Initiating NSE at 14:18
Completed NSE at 14:18, 0.00s elapsed
Initiating NSE at 14:18
Completed NSE at 14:18, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 77.43 seconds
           Raw packets sent: 3122 (142.110KB) | Rcvd: 104 (6.322KB)
