
Starting Nmap 7.60 ( https://nmap.org ) at 2018-01-31 14:13 IST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:13
Completed NSE at 14:13, 0.00s elapsed
Initiating NSE at 14:13
Completed NSE at 14:13, 0.00s elapsed
Initiating Ping Scan at 14:13
Scanning 14.139.34.2 [4 ports]
Completed Ping Scan at 14:13, 0.22s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:13
Completed Parallel DNS resolution of 1 host. at 14:13, 13.00s elapsed
Initiating SYN Stealth Scan at 14:13
Scanning 14.139.34.2 [1000 ports]
Discovered open port 80/tcp on 14.139.34.2
Discovered open port 22/tcp on 14.139.34.2
Discovered open port 53/tcp on 14.139.34.2
Discovered open port 443/tcp on 14.139.34.2
Discovered open port 5001/tcp on 14.139.34.2
Increasing send delay for 14.139.34.2 from 0 to 5 due to 31 out of 101 dropped probes since last increase.
Increasing send delay for 14.139.34.2 from 5 to 10 due to 43 out of 143 dropped probes since last increase.
Increasing send delay for 14.139.34.2 from 10 to 20 due to 11 out of 30 dropped probes since last increase.
Increasing send delay for 14.139.34.2 from 20 to 40 due to max_successful_tryno increase to 4
Increasing send delay for 14.139.34.2 from 40 to 80 due to 11 out of 27 dropped probes since last increase.
Increasing send delay for 14.139.34.2 from 80 to 160 due to 11 out of 26 dropped probes since last increase.
Increasing send delay for 14.139.34.2 from 160 to 320 due to 11 out of 22 dropped probes since last increase.
SYN Stealth Scan Timing: About 26.95% done; ETC: 14:15 (0:01:24 remaining)
SYN Stealth Scan Timing: About 36.35% done; ETC: 14:16 (0:01:47 remaining)
Discovered open port 7001/tcp on 14.139.34.2
SYN Stealth Scan Timing: About 60.42% done; ETC: 14:17 (0:01:31 remaining)
Discovered open port 10000/tcp on 14.139.34.2
SYN Stealth Scan Timing: About 69.55% done; ETC: 14:17 (0:01:14 remaining)
SYN Stealth Scan Timing: About 78.70% done; ETC: 14:17 (0:00:54 remaining)
Discovered open port 3000/tcp on 14.139.34.2
SYN Stealth Scan Timing: About 88.10% done; ETC: 14:17 (0:00:31 remaining)
Completed SYN Stealth Scan at 14:18, 278.74s elapsed (1000 total ports)
Initiating Service scan at 14:18
Scanning 8 services on 14.139.34.2
Completed Service scan at 14:18, 12.68s elapsed (8 services on 1 host)
Initiating OS detection (try #1) against 14.139.34.2
Retrying OS detection (try #2) against 14.139.34.2
Initiating Traceroute at 14:18
Completed Traceroute at 14:18, 3.10s elapsed
Initiating Parallel DNS resolution of 8 hosts. at 14:18
Completed Parallel DNS resolution of 8 hosts. at 14:18, 13.00s elapsed
NSE: Script scanning 14.139.34.2.
Initiating NSE at 14:18
Completed NSE at 14:19, 31.89s elapsed
Initiating NSE at 14:19
Completed NSE at 14:19, 0.01s elapsed
Nmap scan report for 14.139.34.2
Host is up (0.056s latency).
Not shown: 989 closed ports
PORT      STATE    SERVICE      VERSION
22/tcp    open     ssh          OpenSSH 6.6p1 Ubuntu 2ubuntu1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 6a:04:05:a7:e6:54:02:d6:b5:e0:ea:0f:be:62:c7:e4 (DSA)
|   2048 6c:a7:f9:89:f3:a0:70:4e:bb:6d:40:2e:67:fb:86:b9 (RSA)
|   256 65:f6:1c:f0:c9:2e:6f:e7:de:43:b8:1c:52:ab:43:04 (ECDSA)
|_  256 1e:e7:c1:94:09:91:fc:ea:0e:fc:96:1c:db:81:91:b0 (EdDSA)
53/tcp    open     domain
| dns-nsid: 
|_  bind.version: 9.9.5-3ubuntu0.6-Ubuntu
80/tcp    open     http         Apache httpd 2.4.7 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
139/tcp   filtered netbios-ssn
443/tcp   open     ssl/http     Apache httpd 2.4.7 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: IIT Mandi|VPN Access
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
445/tcp   filtered microsoft-ds
3000/tcp  open     ntop-http    Ntop web interface 5.0.1
5001/tcp  open     ssh          OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8f:fe:72:c6:29:af:a1:b1:b1:38:c5:17:5d:e8:75:00 (RSA)
|   256 30:b5:28:55:d5:51:22:c3:c3:8e:48:6c:36:8c:54:06 (ECDSA)
|_  256 a1:8b:88:5b:d7:bc:1d:da:09:b9:b0:7a:66:cc:59:92 (EdDSA)
7001/tcp  open     ssh          OpenSSH 6.0p1 Debian 4+deb7u2 (protocol 2.0)
| ssh-hostkey: 
|   1024 48:51:85:e6:c0:2b:38:98:8a:0d:01:f4:13:e6:0c:00 (DSA)
|   2048 77:d3:25:da:63:64:c0:53:30:c6:da:ee:71:52:b9:b4 (RSA)
|_  256 ba:dd:66:bf:e7:9b:05:13:fe:b2:4a:6b:e1:88:ea:44 (ECDSA)
9000/tcp  filtered cslistener
10000/tcp open     http         MiniServ 1.690 (Webmin httpd)
|_http-favicon: Unknown favicon MD5: 49CEDF9798CBC700D74AB5A0E6066A13
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
Device type: general purpose|printer|security-misc|broadband router|WAP|switch|VoIP phone
Running (JUST GUESSING): Linux 3.X|4.X|2.6.X (87%), Kyocera embedded (87%), Barracuda Networks embedded (85%), Canon embedded (85%), D-Link embedded (85%), Extreme Networks ExtremeXOS 12.X (85%), Thomson embedded (85%)
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4 cpe:/h:kyocera:cs-2560 cpe:/o:linux:linux_kernel:2.6.32 cpe:/h:canon:imagerunner_advance_c5051 cpe:/h:dlink:dsl-2540b cpe:/h:dlink:dir-300 cpe:/o:extremenetworks:extremexos:12.5.4
Aggressive OS guesses: Linux 3.11 - 4.1 (87%), Kyocera CopyStar CS-2560 printer (87%), Linux 3.0 (87%), Linux 3.0 or 3.5 (87%), Linux 2.6.32 (86%), Linux 2.6.26 (86%), Linux 2.6.18 (86%), Barracuda Web Filter (85%), Linux 2.6.22 (85%), Canon imageRUNNER ADVANCE C5051 printer (85%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 49.590 days (since Wed Dec 13 00:09:34 2017)
Network Distance: 14 hops
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 21/tcp)
HOP RTT      ADDRESS
1   53.21 ms gateway (192.168.43.1)
2   ... 4
5   48.28 ms 125.21.210.61
6   48.35 ms 182.79.234.58
7   72.30 ms 218.100.48.28
8   72.35 ms 182.19.110.54
9   54.22 ms 118.185.99.33
10  ... 12
13  79.50 ms 14.139.34.1
14  55.53 ms 14.139.34.2

NSE: Script Post-scanning.
Initiating NSE at 14:19
Completed NSE at 14:19, 0.00s elapsed
Initiating NSE at 14:19
Completed NSE at 14:19, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 358.20 seconds
           Raw packets sent: 1317 (61.950KB) | Rcvd: 1377 (65.490KB)
