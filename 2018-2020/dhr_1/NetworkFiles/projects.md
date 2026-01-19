
Starting Nmap 7.60 ( https://nmap.org ) at 2018-01-31 14:33 IST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:33
Completed NSE at 14:33, 0.00s elapsed
Initiating NSE at 14:33
Completed NSE at 14:33, 0.00s elapsed
Initiating Ping Scan at 14:33
Scanning 14.139.34.9 [4 ports]
Completed Ping Scan at 14:33, 0.22s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:33
Completed Parallel DNS resolution of 1 host. at 14:33, 0.04s elapsed
Initiating SYN Stealth Scan at 14:33
Scanning mail.projects.iitmandi.ac.in (14.139.34.9) [1000 ports]
Discovered open port 25/tcp on 14.139.34.9
Discovered open port 110/tcp on 14.139.34.9
Discovered open port 80/tcp on 14.139.34.9
Discovered open port 993/tcp on 14.139.34.9
Discovered open port 443/tcp on 14.139.34.9
Discovered open port 143/tcp on 14.139.34.9
Increasing send delay for 14.139.34.9 from 0 to 5 due to 11 out of 27 dropped probes since last increase.
Increasing send delay for 14.139.34.9 from 5 to 10 due to 11 out of 22 dropped probes since last increase.
SYN Stealth Scan Timing: About 15.02% done; ETC: 14:37 (0:02:55 remaining)
Increasing send delay for 14.139.34.9 from 10 to 20 due to 11 out of 22 dropped probes since last increase.
Discovered open port 465/tcp on 14.139.34.9
Increasing send delay for 14.139.34.9 from 20 to 40 due to 11 out of 21 dropped probes since last increase.
SYN Stealth Scan Timing: About 23.06% done; ETC: 14:38 (0:03:24 remaining)
Increasing send delay for 14.139.34.9 from 40 to 80 due to 11 out of 36 dropped probes since last increase.
SYN Stealth Scan Timing: About 35.26% done; ETC: 14:38 (0:02:47 remaining)
Increasing send delay for 14.139.34.9 from 80 to 160 due to 11 out of 33 dropped probes since last increase.
SYN Stealth Scan Timing: About 45.32% done; ETC: 14:39 (0:03:02 remaining)
Increasing send delay for 14.139.34.9 from 160 to 320 due to 11 out of 35 dropped probes since last increase.
SYN Stealth Scan Timing: About 47.60% done; ETC: 14:40 (0:03:19 remaining)
SYN Stealth Scan Timing: About 49.46% done; ETC: 14:41 (0:03:39 remaining)
SYN Stealth Scan Timing: About 52.38% done; ETC: 14:42 (0:04:01 remaining)
SYN Stealth Scan Timing: About 60.20% done; ETC: 14:45 (0:04:26 remaining)
SYN Stealth Scan Timing: About 73.04% done; ETC: 14:48 (0:03:52 remaining)
SYN Stealth Scan Timing: About 79.86% done; ETC: 14:49 (0:03:09 remaining)
SYN Stealth Scan Timing: About 85.80% done; ETC: 14:50 (0:02:21 remaining)
Discovered open port 10000/tcp on 14.139.34.9
SYN Stealth Scan Timing: About 91.34% done; ETC: 14:51 (0:01:30 remaining)
SYN Stealth Scan Timing: About 96.62% done; ETC: 14:51 (0:00:36 remaining)
Completed SYN Stealth Scan at 14:52, 1104.06s elapsed (1000 total ports)
Initiating Service scan at 14:52
Scanning 8 services on mail.projects.iitmandi.ac.in (14.139.34.9)
Completed Service scan at 14:52, 20.16s elapsed (8 services on 1 host)
Initiating OS detection (try #1) against mail.projects.iitmandi.ac.in (14.139.34.9)
Retrying OS detection (try #2) against mail.projects.iitmandi.ac.in (14.139.34.9)
Initiating Traceroute at 14:52
Completed Traceroute at 14:52, 3.06s elapsed
Initiating Parallel DNS resolution of 10 hosts. at 14:52
Completed Parallel DNS resolution of 10 hosts. at 14:52, 13.00s elapsed
NSE: Script scanning 14.139.34.9.
Initiating NSE at 14:52
Completed NSE at 14:53, 30.18s elapsed
Initiating NSE at 14:53
Completed NSE at 14:53, 0.01s elapsed
Nmap scan report for mail.projects.iitmandi.ac.in (14.139.34.9)
Host is up (0.051s latency).
Not shown: 989 filtered ports
PORT      STATE  SERVICE    VERSION
25/tcp    open   smtp       Postfix smtpd
|_smtp-commands: mail.projects.iitmandi.ac.in, PIPELINING, SIZE 31457280, VRFY, ETRN, STARTTLS, AUTH PLAIN LOGIN, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, 
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
53/tcp    closed domain
80/tcp    open   http       Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
110/tcp   open   pop3       Dovecot pop3d
|_pop3-capabilities: RESP-CODES STLS PIPELINING UIDL CAPA USER TOP SASL(PLAIN LOGIN) AUTH-RESP-CODE
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
143/tcp   open   imap       Dovecot imapd
|_imap-capabilities: Pre-login IMAP4rev1 ID more ENABLE have IDLE post-login OK AUTH=PLAIN AUTH=LOGINA0001 LITERAL+ listed capabilities STARTTLS SASL-IR LOGIN-REFERRALS
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
389/tcp   closed ldap
443/tcp   open   ssl/http   Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
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
465/tcp   open   ssl/smtp   Postfix smtpd
|_smtp-commands: mail.projects.iitmandi.ac.in, PIPELINING, SIZE 31457280, VRFY, ETRN, AUTH PLAIN LOGIN, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, 
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
587/tcp   closed submission
993/tcp   open   ssl/imap   Dovecot imapd
|_imap-capabilities: more AUTH=PLAIN IDLE have IMAP4rev1 post-login ID OK listed AUTH=LOGINA0001 LITERAL+ capabilities Pre-login LOGIN-REFERRALS SASL-IR ENABLE
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
10000/tcp open   http       MiniServ 1.820 (Webmin httpd)
|_http-favicon: Unknown favicon MD5: E0442EDA7361E86A63B4A44C6126B0D4
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Site doesn't have a title (text/html; Charset=iso-8859-1).
Aggressive OS guesses: Linux 3.11 - 4.1 (93%), Linux 3.13 (89%), Linux 3.16 (88%), Linux 2.6.32 (88%), Linux 3.2 - 3.8 (88%), Linux 3.8 (88%), IPFire 2.11 firewall (Linux 2.6.32) (87%), Linux 3.10 - 3.12 (87%), Linux 4.4 (87%), WatchGuard Fireware 11.8 (87%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 53.534 days (since Sat Dec  9 02:04:49 2017)
Network Distance: 14 hops
TCP Sequence Prediction: Difficulty=264 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 53/tcp)
HOP RTT       ADDRESS
1   3.78 ms   gateway (192.168.43.1)
2   ...
3   29.84 ms  10.206.31.26
4   28.21 ms  10.206.30.213
5   151.68 ms 125.21.210.61
6   34.47 ms  182.79.190.73
7   53.51 ms  218.100.48.28
8   53.91 ms  182.19.110.54
9   29.06 ms  118.185.99.33
10  ... 12
13  45.48 ms  14.139.34.1
14  46.44 ms  mail.projects.iitmandi.ac.in (14.139.34.9)

NSE: Script Post-scanning.
Initiating NSE at 14:53
Completed NSE at 14:53, 0.00s elapsed
Initiating NSE at 14:53
Completed NSE at 14:53, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 1176.13 seconds
           Raw packets sent: 5455 (244.154KB) | Rcvd: 548 (29.974KB)
