Nmap scan report for 14.139.34.2
Host is up (0.036s latency).
Not shown: 65490 closed ports, 36 filtered ports
PORT      STATE SERVICE   VERSION
22/tcp    open  ssh       OpenSSH 6.6p1 Ubuntu 2ubuntu1 (Ubuntu Linux; protocol 2.0)
53/tcp    open  domain
80/tcp    open  http      Apache httpd 2.4.7 ((Ubuntu))
443/tcp   open  ssl/http  Apache httpd 2.4.7 ((Ubuntu))
1344/tcp  open  icap      C-ICAP 0.3.2
3000/tcp  open  ntop-http Ntop web interface 5.0.1
5001/tcp  open  ssh       OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
7001/tcp  open  ssh       OpenSSH 6.0p1 Debian 4+deb7u2 (protocol 2.0)
10000/tcp open  http      MiniServ 1.690 (Webmin httpd)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for mail.students.iitmandi.ac.in (14.139.34.3)
Host is up (0.036s latency).
Not shown: 65521 filtered ports
PORT      STATE  SERVICE    VERSION
25/tcp    open   smtp       Postfix smtpd
53/tcp    open   domain     ISC BIND 9.10.3-P4-Ubuntu
80/tcp    open   http       Apache httpd 2.4.18 ((Ubuntu))
110/tcp   open   pop3       Dovecot pop3d
143/tcp   open   imap       Dovecot imapd
389/tcp   closed ldap
443/tcp   open   ssl/http   Apache httpd 2.4.18 ((Ubuntu))
465/tcp   open   ssl/smtp   Postfix smtpd
587/tcp   closed submission
993/tcp   open   ssl/imap   Dovecot imapd
995/tcp   open   ssl/pop3   Dovecot pop3d
3306/tcp  closed mysql
5000/tcp  closed upnp
10000/tcp open   http       MiniServ 1.850 (Webmin httpd)

Nmap scan report for 14.139.34.4
Host is up (0.074s latency).
Not shown: 65501 closed ports, 28 filtered ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.6 (Ubuntu Linux; protocol 2.0)
25/tcp   open  smtp    Postfix smtpd
80/tcp   open  http    Apache httpd 2.4.7 ((Ubuntu))
6001/tcp open  X11:1?
8023/tcp open  unknown
8080/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))

Nmap scan report for mail.alumni.iitmandi.ac.in (14.139.34.7)
Host is up (0.032s latency).
Not shown: 65494 closed ports, 29 filtered ports
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 5.9p1 Debian 5ubuntu1.1 (Ubuntu Linux; protocol 2.0)
25/tcp    open  smtp     Postfix smtpd
53/tcp    open  domain   ISC BIND 9.8.1-P1
80/tcp    open  http     Apache httpd 2.2.22 ((Ubuntu))
110/tcp   open  pop3     Dovecot pop3d
143/tcp   open  imap     Dovecot imapd
587/tcp   open  smtp     Postfix smtpd
993/tcp   open  ssl/imap Dovecot imapd
995/tcp   open  ssl/pop3 Dovecot pop3d
4190/tcp  open  sieve    Dovecot Pigeonhole sieve 1.0
10000/tcp open  ssl/http MiniServ 1.650 (Webmin httpd)
20000/tcp open  http     MiniServ 1.560 (Webmin httpd)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


OS detection nmap

Nmap scan report for 14.139.34.2
Host is up (0.048s latency).
Not shown: 986 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
53/tcp    open     domain
80/tcp    open     http
139/tcp   filtered netbios-ssn
443/tcp   open     https
445/tcp   filtered microsoft-ds
1720/tcp  filtered h323q931
3000/tcp  open     ppp
5001/tcp  open     commplex-link
5060/tcp  filtered sip
7001/tcp  open     afs3-callback
9000/tcp  filtered cslistener
9001/tcp  filtered tor-orport
10000/tcp open     snet-sensor-mgmt
Aggressive OS guesses: Linux 3.11 - 4.1 (87%), Barracuda Web Filter (86%), Linux 2.6.22 (86%), Linux 2.6.26 (86%), Linux 3.0 (86%), Linux 3.0 or 3.5 (86%), OpenBSD 4.0 (86%), OpenBSD 4.3 (85%), Linux 2.6.24 (Debian) (85%), Canon imageRUNNER ADVANCE C5051 printer (85%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 23.486 days (since Mon Jan 15 11:48:49 2018)
TCP Sequence Prediction: Difficulty=253 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for mail.students.iitmandi.ac.in (14.139.34.3)
Host is up (0.033s latency).
Not shown: 986 filtered ports
PORT     STATE  SERVICE
25/tcp   open   smtp
53/tcp   open   domain
80/tcp   open   http
110/tcp  open   pop3
143/tcp  open   imap
389/tcp  closed ldap
443/tcp  open   https
465/tcp  open   smtps
587/tcp  closed submission
993/tcp  open   imaps
995/tcp  open   pop3s
3306/tcp closed mysql
5000/tcp closed upnp
8000/tcp closed http-alt
Aggressive OS guesses: Linux 3.11 - 4.1 (93%), Linux 3.13 (89%), Linux 3.16 (88%), Linux 4.4 (87%), Linux 2.6.32 (87%), Linux 3.2 - 3.8 (87%), Linux 3.8 (87%), WatchGuard Fireware 11.8 (87%), IPFire 2.11 firewall (Linux 2.6.32) (87%), Linux 3.10 - 3.12 (86%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 41.799 days (since Thu Dec 28 04:17:10 2017)
TCP Sequence Prediction: Difficulty=264 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for 14.139.34.4
Host is up (0.034s latency).
Not shown: 990 closed ports
PORT     STATE    SERVICE
22/tcp   open     ssh
25/tcp   open     smtp
80/tcp   open     http
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
1720/tcp filtered h323q931
5060/tcp filtered sip
6001/tcp open     X11:1
8008/tcp filtered http
8080/tcp open     http-proxy
Aggressive OS guesses: Linux 3.11 - 4.1 (93%), Linux 3.13 (89%), Linux 3.10 - 3.12 (87%), Linux 4.4 (87%), Linux 3.16 (87%), Linux 3.2 - 3.8 (87%), Linux 3.8 (87%), WatchGuard Fireware 11.8 (87%), IPFire 2.11 firewall (Linux 2.6.32) (87%), Linux 2.6.32 (86%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 23.486 days (since Mon Jan 15 11:48:43 2018)
TCP Sequence Prediction: Difficulty=257 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for mail.alumni.iitmandi.ac.in (14.139.34.7)
Host is up (0.033s latency).
Not shown: 985 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
25/tcp    open     smtp
53/tcp    open     domain
80/tcp    open     http
110/tcp   open     pop3
139/tcp   filtered netbios-ssn
143/tcp   open     imap
445/tcp   filtered microsoft-ds
587/tcp   open     submission
993/tcp   open     imaps
995/tcp   open     pop3s
1720/tcp  filtered h323q931
5060/tcp  filtered sip
10000/tcp open     snet-sensor-mgmt
20000/tcp open     dnp
Aggressive OS guesses: Linux 3.2 - 3.8 (93%), Linux 3.8 (93%), WatchGuard Fireware 11.8 (93%), Linux 3.5 (90%), Linux 3.1 - 3.2 (90%), Linux 2.6.32 - 2.6.39 (90%), Linux 3.0 - 3.2 (89%), Linux 2.6.32 (87%), Linux 3.0 (87%), Linux 3.0 or 3.5 (87%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 46.478 days (since Sat Dec 23 11:59:16 2017)
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for 14.139.34.8
Host is up (0.033s latency).
Not shown: 994 filtered ports
PORT      STATE  SERVICE
53/tcp    closed domain
80/tcp    open   http
389/tcp   open   ldap
443/tcp   open   https
3306/tcp  closed mysql
10000/tcp open   snet-sensor-mgmt
Aggressive OS guesses: Linux 3.2 - 3.8 (93%), Linux 3.8 (93%), WatchGuard Fireware 11.8 (93%), Linux 3.5 (90%), Linux 3.1 - 3.2 (90%), Linux 2.6.32 - 2.6.39 (90%), Linux 3.0 - 3.2 (89%), Linux 2.6.32 (87%), Linux 3.0 (87%), Linux 3.11 - 4.1 (87%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 27.838 days (since Thu Jan 11 03:21:52 2018)
TCP Sequence Prediction: Difficulty=252 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for mail.projects.iitmandi.ac.in (14.139.34.9)
Host is up (0.032s latency).
Not shown: 992 filtered ports
PORT    STATE  SERVICE
25/tcp  open   smtp
53/tcp  closed domain
80/tcp  open   http
110/tcp open   pop3
143/tcp open   imap
443/tcp open   https
587/tcp closed submission
993/tcp open   imaps
Aggressive OS guesses: Linux 3.11 - 4.1 (93%), Linux 3.13 (89%), Linux 4.4 (87%), Linux 3.2 - 3.8 (87%), Linux 3.8 (87%), WatchGuard Fireware 11.8 (87%), Linux 3.16 (87%), IPFire 2.11 firewall (Linux 2.6.32) (87%), Linux 3.10 - 3.12 (86%), DD-WRT v24-sp1 (Linux 2.4) (86%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 40.593 days (since Fri Dec 29 09:14:17 2017)
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for 14.139.34.10
Host is up (0.033s latency).
Not shown: 985 filtered ports
PORT      STATE  SERVICE
20/tcp    closed ftp-data
21/tcp    open   ftp
25/tcp    closed smtp
53/tcp    closed domain
80/tcp    open   http
143/tcp   closed imap
443/tcp   open   https
993/tcp   closed imaps
3306/tcp  closed mysql
5000/tcp  closed upnp
49152/tcp closed unknown
49155/tcp closed unknown
49160/tcp closed unknown
49161/tcp closed unknown
49175/tcp closed unknown
Device type: general purpose|firewall|WAP|terminal
Running (JUST GUESSING): Linux 3.X|4.X|2.6.X (93%), WatchGuard Fireware 11.X (86%), HP embedded (85%), IGEL embedded (85%)
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4 cpe:/o:watchguard:fireware:11.8 cpe:/o:linux:linux_kernel:2.6.32 cpe:/h:hp:msm410 cpe:/o:linux:linux_kernel:2.6 cpe:/h:igel:ud3
Aggressive OS guesses: Linux 3.11 - 4.1 (93%), Linux 3.2 - 3.8 (87%), Linux 3.13 (87%), Linux 3.5 (86%), Linux 4.4 (86%), Linux 3.8 (86%), WatchGuard Fireware 11.8 (86%), Linux 3.16 (86%), Linux 2.6.32 (86%), Linux 3.18 (86%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 40.364 days (since Fri Dec 29 14:44:51 2017)
TCP Sequence Prediction: Difficulty=256 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for 14.139.34.11
Host is up (0.031s latency).
Not shown: 992 closed ports
PORT     STATE    SERVICE
22/tcp   open     ssh
53/tcp   open     domain
80/tcp   open     http
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
1720/tcp filtered h323q931
5060/tcp filtered sip
8080/tcp open     http-proxy
Device type: general purpose|firewall|WAP|terminal
Running (JUST GUESSING): Linux 3.X|4.X|2.6.X (93%), WatchGuard Fireware 11.X (87%), IPFire 2.X (87%), HP embedded (85%), IGEL embedded (85%)
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4 cpe:/o:watchguard:fireware:11.8 cpe:/o:linux:linux_kernel:2.6.32 cpe:/o:ipfire:ipfire:2.11 cpe:/h:hp:msm410 cpe:/o:linux:linux_kernel:2.6 cpe:/h:igel:ud3
Aggressive OS guesses: Linux 3.11 - 4.1 (93%), Linux 3.13 (89%), Linux 3.16 (88%), Linux 4.4 (87%), Linux 3.2 - 3.8 (87%), Linux 3.8 (87%), WatchGuard Fireware 11.8 (87%), IPFire 2.11 firewall (Linux 2.6.32) (87%), Linux 3.10 - 3.12 (86%), Linux 2.6.32 (86%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 39.820 days (since Sat Dec 30 03:47:46 2017)
TCP Sequence Prediction: Difficulty=265 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for 14.139.34.17
Host is up (0.038s latency).
Not shown: 992 closed ports
PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   open     http
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
1720/tcp filtered h323q931
5060/tcp filtered sip
5800/tcp open     vnc-http
5900/tcp open     vnc
Aggressive OS guesses: Linux 3.2 - 3.8 (93%), Linux 3.5 (92%), Linux 3.8 (91%), WatchGuard Fireware 11.8 (91%), Linux 3.1 - 3.2 (90%), Linux 2.6.32 - 2.6.39 (90%), Linux 3.0 - 3.2 (88%), Linux 2.6.32 (87%), Linux 2.6.32 or 3.10 (87%), Linux 3.11 - 4.1 (87%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 23.485 days (since Mon Jan 15 11:50:20 2018)
TCP Sequence Prediction: Difficulty=260 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for 14.139.34.24
Host is up (0.030s latency).
Not shown: 973 closed ports
PORT      STATE    SERVICE
80/tcp    open     http
135/tcp   open     msrpc
139/tcp   filtered netbios-ssn
445/tcp   filtered microsoft-ds
1023/tcp  open     netvenuechat
1433/tcp  open     ms-sql-s
1720/tcp  filtered h323q931
1801/tcp  open     msmq
2103/tcp  open     zephyr-clt
2105/tcp  open     eklogin
2107/tcp  open     msmq-mgmt
2383/tcp  open     ms-olap4
3001/tcp  open     nessus
3306/tcp  open     mysql
3389/tcp  open     ms-wbt-server
3690/tcp  open     svn
5060/tcp  filtered sip
8080/tcp  open     http-proxy
8085/tcp  open     unknown
8086/tcp  open     d-s-n
9000/tcp  open     cslistener
49152/tcp open     unknown
49153/tcp open     unknown
49154/tcp open     unknown
49155/tcp open     unknown
49156/tcp open     unknown
49157/tcp open     unknown
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2012|Vista|2008|7 (92%)
OS CPE: cpe:/o:microsoft:windows_server_2012:r2 cpe:/o:microsoft:windows_vista::- cpe:/o:microsoft:windows_vista::sp1 cpe:/o:microsoft:windows_server_2008::sp1 cpe:/o:microsoft:windows_7
Aggressive OS guesses: Microsoft Windows Server 2012 or Windows Server 2012 R2 (92%), Microsoft Windows Server 2012 (91%), Microsoft Windows Server 2012 R2 (89%), Microsoft Windows Vista SP0 or SP1, Windows Server 2008 SP1, or Windows 7 (86%), Microsoft Windows 7 Professional (86%), Microsoft Windows Server 2008 R2 SP1 (86%), Microsoft Windows Server 2008 (85%), Microsoft Windows Server 2008 R2 (85%), Microsoft Windows 7 SP1 (85%), Microsoft Windows Server 2008 or 2008 Beta 3 (85%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 39.124 days (since Sat Dec 30 20:29:58 2017)
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: Incremental

Nmap scan report for 14.139.34.26
Host is up (0.038s latency).
Not shown: 978 closed ports
PORT      STATE    SERVICE
80/tcp    open     http
135/tcp   open     msrpc
139/tcp   filtered netbios-ssn
445/tcp   filtered microsoft-ds
1023/tcp  open     netvenuechat
1024/tcp  open     kdm
1433/tcp  open     ms-sql-s
1720/tcp  filtered h323q931
1801/tcp  open     msmq
2103/tcp  open     zephyr-clt
2105/tcp  open     eklogin
2107/tcp  open     msmq-mgmt
2383/tcp  open     ms-olap4
3389/tcp  open     ms-wbt-server
5060/tcp  filtered sip
49152/tcp open     unknown
49153/tcp open     unknown
49154/tcp open     unknown
49155/tcp open     unknown
49156/tcp open     unknown
49159/tcp open     unknown
49167/tcp open     unknown
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2012|7|Vista|2008 (92%)
OS CPE: cpe:/o:microsoft:windows_server_2012:r2 cpe:/o:microsoft:windows_7 cpe:/o:microsoft:windows_vista::- cpe:/o:microsoft:windows_vista::sp1 cpe:/o:microsoft:windows_server_2008::sp1
Aggressive OS guesses: Microsoft Windows Server 2012 or Windows Server 2012 R2 (92%), Microsoft Windows Server 2012 (91%), Microsoft Windows Server 2012 R2 (91%), Microsoft Windows 7 (86%), Microsoft Windows Vista SP0 or SP1, Windows Server 2008 SP1, or Windows 7 (86%), Microsoft Windows Server 2008 R2 SP1 (86%), Microsoft Windows Server 2008 R2 (85%), Microsoft Windows 7 SP1 or Windows Server 2008 SP2 or 2008 R2 SP1 (85%), Microsoft Windows Vista SP2, Windows 7 SP1, or Windows Server 2008 (85%), Microsoft Windows 7 Professional (85%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 0.496 days (since Wed Feb  7 11:34:34 2018)
TCP Sequence Prediction: Difficulty=258 (Good luck!)
IP ID Sequence Generation: Incremental

Nmap scan report for 14.139.34.27
Host is up (0.029s latency).
Not shown: 999 filtered ports
PORT   STATE SERVICE
22/tcp open  ssh
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Linux 3.X|4.X|2.6.X (89%)
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4.4 cpe:/o:linux:linux_kernel:2.6
Aggressive OS guesses: Linux 3.10 - 3.12 (89%), Linux 4.4 (89%), Linux 2.6.18 - 2.6.22 (86%), Linux 4.0 (86%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 0.404 days (since Wed Feb  7 13:46:29 2018)
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros

Nmap scan report for 14.139.34.43
Host is up (0.038s latency).
Not shown: 990 closed ports
PORT     STATE    SERVICE
22/tcp   open     ssh
80/tcp   open     http
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
1720/tcp filtered h323q931
3306/tcp open     mysql
5060/tcp filtered sip
8080/tcp open     http-proxy
8081/tcp open     blackice-icecap
8082/tcp open     blackice-alerts
Aggressive OS guesses: Linux 3.2 - 3.8 (93%), WatchGuard Fireware 11.8 (93%), Linux 3.5 (92%), Linux 3.8 (91%), Linux 3.1 - 3.2 (90%), Linux 2.6.32 - 2.6.39 (90%), Linux 3.0 - 3.2 (89%), Linux 2.6.32 (87%), Linux 2.6.32 or 3.10 (87%), Linux 3.6 (87%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 2.585 days (since Mon Feb  5 09:25:28 2018)
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: All zeros

