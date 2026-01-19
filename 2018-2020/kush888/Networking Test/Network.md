## 1st Part 
I already knew about the nmap command so didnt spend much time on it. Nmap is used for exploring networks, perform security scans, network audit and finding open ports on remote machine. It scans for Live hosts, Operating systems, packet filters and open ports running on remote hosts. Some flags can be used along with nmap command to get the desired results. Adding -O flag gives information about the operating system. 

Command used :
```
sudo nmap -O 14.139.34.0/24
```
Output :
```
Nmap scan report for 14.139.34.2
Host is up (0.050s latency).
Not shown: 987 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
25/tcp    filtered smtp
53/tcp    open     domain
80/tcp    open     http
443/tcp   open     https
445/tcp   filtered microsoft-ds
3000/tcp  open     ppp
5001/tcp  open     commplex-link
5060/tcp  filtered sip
5061/tcp  filtered sip-tls
7001/tcp  open     afs3-callback
9000/tcp  filtered cslistener
10000/tcp open     snet-sensor-mgmt
Aggressive OS guesses: Linux 3.13 or 4.2 (96%), OpenWrt Kamikaze 7.09 (Linux 2.6.22) (94%), OpenWrt 0.9 - 7.09 (Linux 2.4.30 - 2.4.34) (93%), OpenWrt White Russian 0.9 (Linux 2.4.30) (93%), OpenWrt Chaos Calmer 15.05 (Linux 3.18) or Designated Driver (Linux 4.1) (93%), Asus RT-AC66U router (Linux 2.6) (92%), Asus RT-N16 WAP (Linux 2.6) (92%), Asus RT-N66U WAP (Linux 2.6) (92%), Tomato 1.28 (Linux 2.6.22) (92%), Linux 3.10 - 4.2 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 14 hops

Nmap scan report for mail.students.iitmandi.ac.in (14.139.34.3)
Host is up (0.053s latency).
Not shown: 986 filtered ports
PORT      STATE  SERVICE
53/tcp    open   domain
80/tcp    open   http
110/tcp   open   pop3
143/tcp   open   imap
389/tcp   closed ldap
443/tcp   open   https
465/tcp   open   smtps
587/tcp   closed submission
993/tcp   open   imaps
995/tcp   open   pop3s
3306/tcp  closed mysql
5000/tcp  closed upnp
8000/tcp  closed http-alt
10000/tcp open   snet-sensor-mgmt
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3.13 cpe:/o:linux:linux_kernel:4.2
OS details: Linux 3.13 or 4.2

Nmap scan report for 14.139.34.4
Host is up (0.056s latency).
Not shown: 992 closed ports
PORT     STATE    SERVICE
22/tcp   open     ssh
25/tcp   filtered smtp
80/tcp   open     http
445/tcp  filtered microsoft-ds
5060/tcp filtered sip
5061/tcp filtered sip-tls
6001/tcp open     X11:1
8080/tcp open     http-proxy
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3.13 cpe:/o:linux:linux_kernel:4.2
OS details: Linux 3.13 or 4.2
Network Distance: 14 hops

Nmap scan report for mail.alumni.iitmandi.ac.in (14.139.34.7)
Host is up (0.051s latency).
Not shown: 986 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
25/tcp    filtered smtp
53/tcp    open     domain
80/tcp    open     http
110/tcp   open     pop3
143/tcp   open     imap
445/tcp   filtered microsoft-ds
587/tcp   open     submission
993/tcp   open     imaps
995/tcp   open     pop3s
5060/tcp  filtered sip
5061/tcp  filtered sip-tls
10000/tcp open     snet-sensor-mgmt
20000/tcp open     dnp
Aggressive OS guesses: Linux 3.2 (95%), OpenWrt 12.09-rc1 Attitude Adjustment (Linux 3.3 - 3.7) (95%), Linux 2.6.32 - 3.13 (95%), Linux 2.6.32 - 3.1 (94%), Linux 2.6.32 (94%), Linux 3.5 (94%), Linux 3.13 or 4.2 (94%), Linux 2.6.32 - 2.6.39 (94%), Linux 3.2 - 3.8 (94%), HP P2000 G3 NAS device (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 14 hops

Nmap scan report for 14.139.34.8
Host is up (0.053s latency).
Not shown: 994 filtered ports
PORT      STATE  SERVICE
53/tcp    closed domain
80/tcp    open   http
389/tcp   open   ldap
443/tcp   open   https
3306/tcp  closed mysql
10000/tcp open   snet-sensor-mgmt
Aggressive OS guesses: OpenWrt 12.09-rc1 Attitude Adjustment (Linux 3.3 - 3.7) (97%), Linux 3.13 or 4.2 (95%), XBMCbuntu Frodo v12.2 (Linux 3.X) (95%), Linux 3.2 - 3.8 (94%), Linux 2.6.32 - 3.1 (92%), Linux 3.2 (92%), Linux 2.6.32 - 3.13 (92%), Linux 3.8 (91%), Linux 3.2 - 3.10 (91%), Linux 3.2 - 3.16 (91%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for mail.projects.iitmandi.ac.in (14.139.34.9)
Host is up (0.054s latency).
Not shown: 990 filtered ports
PORT      STATE  SERVICE
53/tcp    closed domain
80/tcp    open   http
110/tcp   open   pop3
143/tcp   open   imap
389/tcp   closed ldap
443/tcp   open   https
465/tcp   open   smtps
587/tcp   closed submission
993/tcp   open   imaps
10000/tcp open   snet-sensor-mgmt
Device type: general purpose|broadband router|media device|specialized|WAP|storage-misc
Running (JUST GUESSING): Linux 3.X|4.X (98%), Crestron 2-Series (89%), Asus embedded (89%), HP embedded (89%)
OS CPE: cpe:/o:linux:linux_kernel:3.13 cpe:/o:linux:linux_kernel:4.2 cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:3.x cpe:/o:crestron:2_series cpe:/o:linux:linux_kernel cpe:/h:asus:rt-ac66u cpe:/h:hp:p2000_g3
Aggressive OS guesses: Linux 3.13 or 4.2 (98%), Linux 3.10 - 4.2 (94%), Linux 3.13 (94%), Linux 3.16 (93%), Linux 4.4 (93%), OpenWrt 12.09-rc1 Attitude Adjustment (Linux 3.3 - 3.7) (92%), Linux 3.8 (92%), Linux 3.16 - 4.6 (91%), XBMCbuntu Frodo v12.2 (Linux 3.X) (91%), Linux 3.2 - 4.6 (91%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.10
Host is up (0.054s latency).
Not shown: 959 filtered ports, 36 closed ports
PORT     STATE SERVICE
21/tcp   open  ftp
80/tcp   open  http
443/tcp  open  https
8000/tcp open  http-alt
8082/tcp open  blackice-alerts
Device type: general purpose|broadband router|media device|specialized|WAP|storage-misc
Running (JUST GUESSING): Linux 3.X|4.X (98%), Crestron 2-Series (89%), Asus embedded (89%), HP embedded (89%)
OS CPE: cpe:/o:linux:linux_kernel:3.13 cpe:/o:linux:linux_kernel:4.2 cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:3.x cpe:/o:crestron:2_series cpe:/o:linux:linux_kernel cpe:/h:asus:rt-ac66u cpe:/h:hp:p2000_g3
Aggressive OS guesses: Linux 3.13 or 4.2 (98%), Linux 3.10 - 4.2 (94%), Linux 3.13 (94%), Linux 4.4 (94%), OpenWrt 12.09-rc1 Attitude Adjustment (Linux 3.3 - 3.7) (93%), Linux 3.16 (93%), Linux 3.16 - 4.6 (91%), Linux 3.8 (91%), XBMCbuntu Frodo v12.2 (Linux 3.X) (91%), Linux 3.2 - 4.6 (91%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.11
Host is up (0.059s latency).
Not shown: 992 closed ports
PORT     STATE    SERVICE
22/tcp   open     ssh
25/tcp   filtered smtp
53/tcp   open     domain
80/tcp   open     http
445/tcp  filtered microsoft-ds
5060/tcp filtered sip
5061/tcp filtered sip-tls
8080/tcp open     http-proxy
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3.13 cpe:/o:linux:linux_kernel:4.2
OS details: Linux 3.13 or 4.2
Network Distance: 14 hops

Nmap scan report for 14.139.34.17
Host is up (0.055s latency).
Not shown: 992 closed ports
PORT     STATE    SERVICE
22/tcp   open     ssh
25/tcp   filtered smtp
80/tcp   open     http
445/tcp  filtered microsoft-ds
5060/tcp filtered sip
5061/tcp filtered sip-tls
5800/tcp open     vnc-http
5900/tcp open     vnc
Aggressive OS guesses: OpenWrt 12.09-rc1 Attitude Adjustment (Linux 3.3 - 3.7) (96%), XBMCbuntu Frodo v12.2 (Linux 3.X) (96%), Linux 3.2 - 3.8 (95%), Linux 3.13 or 4.2 (95%), Linux 3.13 (94%), Linux 2.6.32 - 3.13 (93%), Linux 3.2 (93%), Linux 3.8 (93%), Linux 3.2 - 3.16 (93%), Linux 2.6.32 - 2.6.39 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 14 hops

Nmap scan report for 14.139.34.24
Host is up (0.055s latency).
Not shown: 973 closed ports
PORT      STATE    SERVICE
25/tcp    filtered smtp
80/tcp    open     http
135/tcp   open     msrpc
139/tcp   open     netbios-ssn
445/tcp   filtered microsoft-ds
1023/tcp  open     netvenuechat
1433/tcp  open     ms-sql-s
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
5061/tcp  filtered sip-tls
8080/tcp  open     http-proxy
8085/tcp  open     unknown
8086/tcp  open     d-s-n
49152/tcp open     unknown
49153/tcp open     unknown
49154/tcp open     unknown
49155/tcp open     unknown
49156/tcp open     unknown
49157/tcp open     unknown
Device type: general purpose|specialized
Running (JUST GUESSING): Microsoft Windows 7|2012|2008|8.1|Vista|10 (96%)
OS CPE: cpe:/o:microsoft:windows_7:::ultimate cpe:/o:microsoft:windows_server_2012 cpe:/o:microsoft:windows_server_2008 cpe:/o:microsoft:windows_8.1 cpe:/o:microsoft:windows_vista::sp1 cpe:/o:microsoft:windows_8 cpe:/o:microsoft:windows_10
Aggressive OS guesses: Microsoft Windows 7 Ultimate (96%), Microsoft Windows Server 2012 Data Center (94%), Microsoft Windows Server 2012 R2 (94%), Microsoft Windows 7 SP1 or Windows Server 2008 (92%), Microsoft Windows 8.1 (92%), Microsoft Windows 7 SP1 or Windows Server 2008 SP2 (91%), Microsoft Windows Vista SP1 (91%), Microsoft Windows Windows 7 SP1 (91%), Microsoft Windows Vista Home Premium SP1, Windows 7, or Windows Server 2008 (91%), Microsoft Windows 7 SP1 (90%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 14 hops

Nmap scan report for 14.139.34.26
Host is up (0.056s latency).
Not shown: 977 closed ports
PORT      STATE    SERVICE
25/tcp    filtered smtp
80/tcp    open     http
135/tcp   open     msrpc
139/tcp   open     netbios-ssn
445/tcp   filtered microsoft-ds
1023/tcp  open     netvenuechat
1024/tcp  open     kdm
1433/tcp  open     ms-sql-s
1801/tcp  open     msmq
2103/tcp  open     zephyr-clt
2105/tcp  open     eklogin
2107/tcp  open     msmq-mgmt
2383/tcp  open     ms-olap4
3389/tcp  open     ms-wbt-server
5060/tcp  filtered sip
5061/tcp  filtered sip-tls
49152/tcp open     unknown
49153/tcp open     unknown
49154/tcp open     unknown
49155/tcp open     unknown
49156/tcp open     unknown
49159/tcp open     unknown
49167/tcp open     unknown
Device type: general purpose|specialized
Running (JUST GUESSING): Microsoft Windows 7|2012|2008|8.1|Vista|10 (96%)
OS CPE: cpe:/o:microsoft:windows_7:::ultimate cpe:/o:microsoft:windows_server_2012:r2 cpe:/o:microsoft:windows_server_2008 cpe:/o:microsoft:windows_8.1 cpe:/o:microsoft:windows_vista::sp1:home_premium cpe:/o:microsoft:windows_8 cpe:/o:microsoft:windows_10
Aggressive OS guesses: Microsoft Windows 7 Ultimate (96%), Microsoft Windows Server 2012 R2 (95%), Microsoft Windows Server 2012 Data Center (94%), Microsoft Windows 7 SP1 or Windows Server 2008 (92%), Microsoft Windows 8.1 (92%), Microsoft Windows 7 SP1 or Windows Server 2008 SP2 (91%), Microsoft Windows Windows 7 SP1 (91%), Microsoft Windows Vista Home Premium SP1, Windows 7, or Windows Server 2008 (91%), Microsoft Windows Vista SP1 (91%), Microsoft Windows 7 SP1 (90%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 14 hops

Nmap scan report for 14.139.34.27
Host is up (0.056s latency).
Not shown: 999 filtered ports
PORT   STATE SERVICE
22/tcp open  ssh
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.13 or 4.2 (94%), Linux 3.10 - 4.2 (92%), Linux 3.2 - 4.6 (92%), Linux 3.18 (90%), Crestron XPanel control system (90%), Linux 3.16 (89%), OpenWrt 12.09-rc1 Attitude Adjustment (Linux 3.3 - 3.7) (88%), XBMCbuntu Frodo v12.2 (Linux 3.X) (88%), ASUS RT-N56U WAP (Linux 3.4) (87%), Linux 3.1 (87%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.43
Host is up (0.054s latency).
Not shown: 989 closed ports
PORT     STATE    SERVICE
22/tcp   open     ssh
25/tcp   filtered smtp
80/tcp   open     http
139/tcp  open     netbios-ssn
445/tcp  filtered microsoft-ds
3306/tcp open     mysql
5060/tcp filtered sip
5061/tcp filtered sip-tls
8080/tcp open     http-proxy
8081/tcp open     blackice-icecap
8082/tcp open     blackice-alerts
Device type: broadband router
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3
OS details: OpenWrt 12.09-rc1 Attitude Adjustment (Linux 3.3 - 3.7)
Network Distance: 14 hops
```


## 2nd Part 
### Findings
1. Whois lookup is a search which provides us with significant information about a domain name.  It may include information, such as domain ownership, where and when registered, expiration date, etc.
2.However, whois could not find students.iitmandi.ac.in as it is subdomain and we need to lookup for the root part for subdomain.
3. After lots of googling, found out that ERNET India has been appointed as an exclusive domain registrar for the education and research domains registering the domains under the .in registry from 2005. 
4. One can buy a new domain under the .in registry at following site: https://www.registry.ernet.in/tariff.aspx

### Answer
The domain name students.iitmandi.ac.in is owned by the ERNET.


## 3rd Part 

### Findings
1. Found the basic information at http://highscalability.com/blog/2013/1/28/duckduckgo-architecture-1-million-deep-searches-a-day-and-gr.html
2. Got to know about various facts related to duckduckgo. 
3. Most components, including all front-end components, are now on amazon's AWS.
4. However this article is quite old and may have outdated information.
5. So used traceroute command to find out about the datacenters.
6. The results were almost same except that one more datacenter was added after 2013 in Illinois,US State.  

### Answer
In total there are 5 datacenters running at California, Virginia, Singapore, Ireland and Illinois. 


