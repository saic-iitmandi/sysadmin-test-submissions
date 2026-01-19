
Starting Nmap 7.60 ( https://nmap.org ) at 2018-01-31 14:24 IST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
Initiating Ping Scan at 14:24
Scanning 14.139.34.3 [4 ports]
Completed Ping Scan at 14:24, 0.22s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:24
Completed Parallel DNS resolution of 1 host. at 14:24, 0.00s elapsed
Initiating SYN Stealth Scan at 14:24
Scanning mail.students.iitmandi.ac.in (14.139.34.3) [1000 ports]
Discovered open port 143/tcp on 14.139.34.3
Discovered open port 993/tcp on 14.139.34.3
Discovered open port 80/tcp on 14.139.34.3
Discovered open port 443/tcp on 14.139.34.3
Discovered open port 25/tcp on 14.139.34.3
Discovered open port 995/tcp on 14.139.34.3
Discovered open port 53/tcp on 14.139.34.3
Discovered open port 110/tcp on 14.139.34.3
Discovered open port 10000/tcp on 14.139.34.3
Discovered open port 465/tcp on 14.139.34.3
Increasing send delay for 14.139.34.3 from 0 to 5 due to 11 out of 36 dropped probes since last increase.
Increasing send delay for 14.139.34.3 from 5 to 10 due to 11 out of 23 dropped probes since last increase.
Increasing send delay for 14.139.34.3 from 10 to 20 due to 11 out of 22 dropped probes since last increase.
Increasing send delay for 14.139.34.3 from 20 to 40 due to 11 out of 24 dropped probes since last increase.
Increasing send delay for 14.139.34.3 from 40 to 80 due to 11 out of 22 dropped probes since last increase.
Completed SYN Stealth Scan at 14:26, 89.44s elapsed (1000 total ports)
Initiating Service scan at 14:26
Scanning 10 services on mail.students.iitmandi.ac.in (14.139.34.3)
Completed Service scan at 14:26, 20.45s elapsed (10 services on 1 host)
Initiating OS detection (try #1) against mail.students.iitmandi.ac.in (14.139.34.3)
Retrying OS detection (try #2) against mail.students.iitmandi.ac.in (14.139.34.3)
Initiating Traceroute at 14:26
Completed Traceroute at 14:26, 3.07s elapsed
Initiating Parallel DNS resolution of 9 hosts. at 14:26
Completed Parallel DNS resolution of 9 hosts. at 14:26, 13.00s elapsed
NSE: Script scanning 14.139.34.3.
Initiating NSE at 14:26
Completed NSE at 14:27, 32.96s elapsed
Initiating NSE at 14:27
Completed NSE at 14:27, 0.00s elapsed
Nmap scan report for mail.students.iitmandi.ac.in (14.139.34.3)
Host is up (0.046s latency).
Not shown: 985 filtered ports
PORT      STATE  SERVICE    VERSION
25/tcp    open   smtp       Postfix smtpd
|_smtp-commands: mail.students.iitmandi.ac.in, PIPELINING, SIZE 10485760, VRFY, ETRN, STARTTLS, AUTH PLAIN LOGIN, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8, 
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
53/tcp    open   domain     ISC BIND 9.10.3-P4-Ubuntu
| dns-nsid: 
|_  bind.version: 9.10.3-P4-Ubuntu
80/tcp    open   http       Apache httpd 2.4.18 ((Ubuntu))
|_http-favicon: Unknown favicon MD5: B8957B00882C0B3CA1F7B1B28E2C69FB
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Students
110/tcp   open   pop3       Dovecot pop3d
|_pop3-capabilities: AUTH-RESP-CODE CAPA USER SASL(PLAIN LOGIN) RESP-CODES TOP PIPELINING UIDL STLS
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
|_imap-capabilities: more capabilities LOGIN-REFERRALS IMAP4rev1 OK ENABLE AUTH=PLAIN LITERAL+ Pre-login STARTTLS have post-login listed AUTH=LOGINA0001 IDLE SASL-IR ID
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
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Students
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
|_smtp-commands: SMTP EHLO mail.students.iitmandi.ac.in: failed to receive data: failed to receive data
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
995/tcp   open   ssl/pop3   Dovecot pop3d
|_pop3-capabilities: AUTH-RESP-CODE CAPA TOP SASL(PLAIN LOGIN) PIPELINING USER UIDL RESP-CODES
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
3306/tcp  closed mysql
5000/tcp  closed upnp
8000/tcp  closed http-alt
10000/tcp open   http       MiniServ 1.850 (Webmin httpd)
|_http-favicon: Unknown favicon MD5: 3508F53B8789E65560C690C057719A08
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
| http-robots.txt: 1 disallowed entry 
|_/
|_http-title: Login to Webmin
Aggressive OS guesses: Linux 3.11 - 4.1 (93%), Linux 3.13 (89%), Linux 4.4 (87%), Linux 3.2 - 3.8 (87%), WatchGuard Fireware 11.8 (87%), Linux 3.16 (87%), IPFire 2.11 firewall (Linux 2.6.32) (87%), Linux 3.10 - 3.12 (86%), Linux 2.6.32 (86%), Linux 3.8 (86%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 53.512 days (since Sat Dec  9 02:10:31 2017)
Network Distance: 14 hops
TCP Sequence Prediction: Difficulty=254 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 3306/tcp)
HOP RTT       ADDRESS
1   3.17 ms   gateway (192.168.43.1)
2   ... 3
4   157.24 ms 10.206.30.213
5   44.55 ms  125.21.210.61
6   47.78 ms  182.79.190.73
7   71.39 ms  218.100.48.28
8   71.43 ms  182.19.110.54
9   42.26 ms  118.185.99.33
10  ... 12
13  51.85 ms  14.139.34.1
14  51.85 ms  mail.students.iitmandi.ac.in (14.139.34.3)

NSE: Script Post-scanning.
Initiating NSE at 14:27
Completed NSE at 14:27, 0.00s elapsed
Initiating NSE at 14:27
Completed NSE at 14:27, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 164.80 seconds
           Raw packets sent: 5143 (231.548KB) | Rcvd: 158 (9.250KB)
