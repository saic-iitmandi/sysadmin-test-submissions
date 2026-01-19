
Starting Nmap 7.60 ( https://nmap.org ) at 2018-01-31 14:36 IST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:36
Completed NSE at 14:36, 0.00s elapsed
Initiating NSE at 14:36
Completed NSE at 14:36, 0.00s elapsed
Initiating Ping Scan at 14:36
Scanning 204.197.248.190 [4 ports]
Completed Ping Scan at 14:36, 0.43s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:36
Completed Parallel DNS resolution of 1 host. at 14:37, 13.00s elapsed
Initiating SYN Stealth Scan at 14:37
Scanning 204.197.248.190 [1000 ports]
Discovered open port 143/tcp on 204.197.248.190
Discovered open port 443/tcp on 204.197.248.190
Discovered open port 587/tcp on 204.197.248.190
Discovered open port 995/tcp on 204.197.248.190
Discovered open port 993/tcp on 204.197.248.190
Discovered open port 80/tcp on 204.197.248.190
Discovered open port 25/tcp on 204.197.248.190
Discovered open port 53/tcp on 204.197.248.190
Discovered open port 21/tcp on 204.197.248.190
Discovered open port 110/tcp on 204.197.248.190
SYN Stealth Scan Timing: About 36.63% done; ETC: 14:38 (0:00:54 remaining)
Discovered open port 26/tcp on 204.197.248.190
Discovered open port 2200/tcp on 204.197.248.190
Discovered open port 465/tcp on 204.197.248.190
Completed SYN Stealth Scan at 14:38, 67.06s elapsed (1000 total ports)
Initiating Service scan at 14:38
Scanning 13 services on 204.197.248.190
Completed Service scan at 14:40, 163.76s elapsed (13 services on 1 host)
Initiating OS detection (try #1) against 204.197.248.190
Retrying OS detection (try #2) against 204.197.248.190
Initiating Traceroute at 14:41
Completed Traceroute at 14:41, 3.02s elapsed
Initiating Parallel DNS resolution of 16 hosts. at 14:41
Completed Parallel DNS resolution of 16 hosts. at 14:41, 13.08s elapsed
NSE: Script scanning 204.197.248.190.
Initiating NSE at 14:41
Completed NSE at 14:41, 37.40s elapsed
Initiating NSE at 14:41
Completed NSE at 14:41, 1.36s elapsed
Nmap scan report for 204.197.248.190
Host is up (0.34s latency).
Not shown: 985 filtered ports
PORT      STATE  SERVICE  VERSION
20/tcp    closed ftp-data
21/tcp    open   ftp      Pure-FTPd
| ssl-cert: Subject: commonName=host.iitmandi.net.in
| Subject Alternative Name: DNS:host.iitmandi.net.in, DNS:www.host.iitmandi.net.in
| Issuer: commonName=cPanel, Inc. Certification Authority/organizationName=cPanel, Inc./stateOrProvinceName=TX/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2017-05-10T00:00:00
| Not valid after:  2018-05-10T23:59:59
| MD5:   d3e7 dc70 2478 9588 566b aea1 2364 8112
|_SHA-1: 5e35 73ad f3de 9591 d6cb 783c e238 61db 6f17 000c
|_ssl-date: TLS randomness does not represent time
25/tcp    open   smtp?
|_smtp-commands: Couldn't establish connection on port 25
26/tcp    open   smtp     Exim smtpd 4.89_1
| smtp-commands: host.iitmandi.net.in Hello nmap.scanme.org [106.223.114.228], SIZE 52428800, 8BITMIME, PIPELINING, AUTH PLAIN LOGIN, STARTTLS, HELP, 
|_ Commands supported: AUTH STARTTLS HELO EHLO MAIL RCPT DATA BDAT NOOP QUIT RSET HELP 
| ssl-cert: Subject: commonName=host.iitmandi.net.in
| Subject Alternative Name: DNS:host.iitmandi.net.in, DNS:www.host.iitmandi.net.in
| Issuer: commonName=cPanel, Inc. Certification Authority/organizationName=cPanel, Inc./stateOrProvinceName=TX/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2017-05-10T00:00:00
| Not valid after:  2018-05-10T23:59:59
| MD5:   d3e7 dc70 2478 9588 566b aea1 2364 8112
|_SHA-1: 5e35 73ad f3de 9591 d6cb 783c e238 61db 6f17 000c
|_ssl-date: TLS randomness does not represent time
53/tcp    open   domain   ISC BIND 9.9.4
| dns-nsid: 
|_  bind.version: 9.9.4-RedHat-9.9.4-51.el7_4.2
80/tcp    open   http     Apache httpd
|_http-favicon: Unknown favicon MD5: B8957B00882C0B3CA1F7B1B28E2C69FB
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-server-header: Apache
|_http-title: IIT Mandi
110/tcp   open   pop3     Dovecot pop3d
|_pop3-capabilities: UIDL AUTH-RESP-CODE PIPELINING CAPA RESP-CODES USER SASL(PLAIN LOGIN) STLS TOP
| ssl-cert: Subject: commonName=host.iitmandi.net.in
| Subject Alternative Name: DNS:host.iitmandi.net.in, DNS:www.host.iitmandi.net.in
| Issuer: commonName=cPanel, Inc. Certification Authority/organizationName=cPanel, Inc./stateOrProvinceName=TX/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2017-05-10T00:00:00
| Not valid after:  2018-05-10T23:59:59
| MD5:   d3e7 dc70 2478 9588 566b aea1 2364 8112
|_SHA-1: 5e35 73ad f3de 9591 d6cb 783c e238 61db 6f17 000c
|_ssl-date: TLS randomness does not represent time
143/tcp   open   imap     Dovecot imapd
|_imap-capabilities: NAMESPACE AUTH=LOGINA0001 OK Pre-login AUTH=PLAIN IMAP4rev1 have capabilities LOGIN-REFERRALS more IDLE post-login ID LITERAL+ ENABLE listed STARTTLS SASL-IR
| ssl-cert: Subject: commonName=host.iitmandi.net.in
| Subject Alternative Name: DNS:host.iitmandi.net.in, DNS:www.host.iitmandi.net.in
| Issuer: commonName=cPanel, Inc. Certification Authority/organizationName=cPanel, Inc./stateOrProvinceName=TX/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2017-05-10T00:00:00
| Not valid after:  2018-05-10T23:59:59
| MD5:   d3e7 dc70 2478 9588 566b aea1 2364 8112
|_SHA-1: 5e35 73ad f3de 9591 d6cb 783c e238 61db 6f17 000c
|_ssl-date: TLS randomness does not represent time
443/tcp   open   ssl/http Apache httpd
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache
|_http-title: 400 Bad Request
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
465/tcp   open   ssl/smtp Exim smtpd 4.89_1
|_smtp-commands: Couldn't establish connection on port 465
| ssl-cert: Subject: commonName=host.iitmandi.net.in
| Subject Alternative Name: DNS:host.iitmandi.net.in, DNS:www.host.iitmandi.net.in
| Issuer: commonName=cPanel, Inc. Certification Authority/organizationName=cPanel, Inc./stateOrProvinceName=TX/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2017-05-10T00:00:00
| Not valid after:  2018-05-10T23:59:59
| MD5:   d3e7 dc70 2478 9588 566b aea1 2364 8112
|_SHA-1: 5e35 73ad f3de 9591 d6cb 783c e238 61db 6f17 000c
|_ssl-date: TLS randomness does not represent time
587/tcp   open   smtp     Exim smtpd 4.89_1
| smtp-commands: host.iitmandi.net.in Hello nmap.scanme.org [106.223.114.228], SIZE 52428800, 8BITMIME, PIPELINING, AUTH PLAIN LOGIN, STARTTLS, HELP, 
|_ Commands supported: AUTH STARTTLS HELO EHLO MAIL RCPT DATA BDAT NOOP QUIT RSET HELP 
| ssl-cert: Subject: commonName=host.iitmandi.net.in
| Subject Alternative Name: DNS:host.iitmandi.net.in, DNS:www.host.iitmandi.net.in
| Issuer: commonName=cPanel, Inc. Certification Authority/organizationName=cPanel, Inc./stateOrProvinceName=TX/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2017-05-10T00:00:00
| Not valid after:  2018-05-10T23:59:59
| MD5:   d3e7 dc70 2478 9588 566b aea1 2364 8112
|_SHA-1: 5e35 73ad f3de 9591 d6cb 783c e238 61db 6f17 000c
|_ssl-date: TLS randomness does not represent time
993/tcp   open   ssl/imap Dovecot imapd
| ssl-cert: Subject: commonName=host.iitmandi.net.in
| Subject Alternative Name: DNS:host.iitmandi.net.in, DNS:www.host.iitmandi.net.in
| Issuer: commonName=cPanel, Inc. Certification Authority/organizationName=cPanel, Inc./stateOrProvinceName=TX/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2017-05-10T00:00:00
| Not valid after:  2018-05-10T23:59:59
| MD5:   d3e7 dc70 2478 9588 566b aea1 2364 8112
|_SHA-1: 5e35 73ad f3de 9591 d6cb 783c e238 61db 6f17 000c
|_ssl-date: TLS randomness does not represent time
995/tcp   open   ssl/pop3 Dovecot pop3d
| ssl-cert: Subject: commonName=host.iitmandi.net.in
| Subject Alternative Name: DNS:host.iitmandi.net.in, DNS:www.host.iitmandi.net.in
| Issuer: commonName=cPanel, Inc. Certification Authority/organizationName=cPanel, Inc./stateOrProvinceName=TX/countryName=US
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2017-05-10T00:00:00
| Not valid after:  2018-05-10T23:59:59
| MD5:   d3e7 dc70 2478 9588 566b aea1 2364 8112
|_SHA-1: 5e35 73ad f3de 9591 d6cb 783c e238 61db 6f17 000c
|_ssl-date: TLS randomness does not represent time
2200/tcp  open   ssh      OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 fc:de:fc:01:c3:63:99:25:3b:46:f6:23:34:72:93:86 (RSA)
|   256 3d:7e:23:d6:25:3c:87:5e:42:ce:2b:8b:59:b9:b4:30 (ECDSA)
|_  256 3d:16:13:a1:10:ee:56:5b:89:6f:07:13:91:60:80:f4 (EdDSA)
30000/tcp closed ndmps
Aggressive OS guesses: Linux 2.6.32 (88%), Linux 2.6.32 or 3.10 (88%), Linux 2.6.39 (88%), Linux 3.10 - 3.12 (88%), Linux 4.4 (88%), WatchGuard Fireware 11.8 (88%), Synology DiskStation Manager 5.1 (87%), Linux 2.6.35 (87%), Linux 3.4 (87%), Linux 3.5 (87%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 4.687 days (since Fri Jan 26 22:13:20 2018)
Network Distance: 18 hops
TCP Sequence Prediction: Difficulty=253 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: Host: host.iitmandi.net.in; OS: Red Hat Enterprise Linux 7; CPE: cpe:/o:redhat:enterprise_linux:7

TRACEROUTE (using port 30000/tcp)
HOP RTT       ADDRESS
1   3.29 ms   gateway (192.168.43.1)
2   ... 3
4   35.78 ms  10.206.30.213
5   36.20 ms  125.21.210.61
6   139.80 ms aes-static-118.36.144.59.airtel.in (59.144.36.118)
7   140.17 ms 129.250.12.229
8   140.24 ms ae-1.r20.sngpsi05.sg.bb.gin.ntt.net (129.250.3.146)
9   316.95 ms ae-8.r22.snjsca04.us.bb.gin.ntt.net (129.250.3.48)
10  305.75 ms ae-0.r23.snjsca04.us.bb.gin.ntt.net (129.250.2.183)
11  330.48 ms ae-7.r23.dllstx09.us.bb.gin.ntt.net (129.250.4.155)
12  336.45 ms ae-6.r10.dllstx09.us.bb.gin.ntt.net (129.250.5.4)
13  336.36 ms ae-0.a00.dllstx04.us.bb.gin.ntt.net (129.250.4.170)
14  355.69 ms xe-0-0-22-3.a00.dllstx04.us.ce.gin.ntt.net (129.250.202.254)
15  310.58 ms Jcore4.0.dal.colo4.com (206.123.64.222)
16  331.85 ms 72.249.129.125
17  330.16 ms vz138-tx.privatesystems.net (72.249.97.138)
18  365.49 ms 204.197.248.190

NSE: Script Post-scanning.
Initiating NSE at 14:41
Completed NSE at 14:41, 0.00s elapsed
Initiating NSE at 14:41
Completed NSE at 14:41, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 307.17 seconds
           Raw packets sent: 3113 (140.608KB) | Rcvd: 173 (12.605KB)
