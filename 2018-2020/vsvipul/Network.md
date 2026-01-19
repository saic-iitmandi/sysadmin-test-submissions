# Networking

## 1. Information of all public facing hosts of IIT Mandi
For this task, i simply used a program called **nmap (Network Mapper)**, which is used to discover hosts and services on a network. I typed the following command in the terminal 

```bash
sudo nmap -O 14.139.34.0/24
```

, which then **gave me all the information about all the PCs, their ports open, and the OS version** they were running. I am just pasting the complete report here, which justifies all the requirements, of this task.


```txt
Nmap scan report for 14.139.34.2
Host is up (0.060s latency).
Not shown: 968 closed ports, 26 filtered ports
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
3000/tcp  open  ppp
5001/tcp  open  commplex-link
7001/tcp  open  afs3-callback
10000/tcp open  snet-sensor-mgmt
Device type: general purpose|printer
Running (JUST GUESSING): Linux 3.X|2.6.X|4.X (92%), Kyocera embedded (86%), FreeBSD 6.X (85%)
OS CPE: cpe:/o:linux:linux_kernel:3.0 cpe:/h:kyocera:cs-2560 cpe:/o:linux:linux_kernel:2.6.32 cpe:/o:linux:linux_kernel:4 cpe:/o:freebsd:freebsd:6.2
Aggressive OS guesses: Linux 3.0 (92%), Linux 3.8 (87%), Kyocera CopyStar CS-2560 printer (86%), Linux 2.6.32 (86%), Linux 3.11 - 4.1 (85%), Linux 3.0 or 3.5 (85%), FreeBSD 6.2-RELEASE (85%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for mail.students.iitmandi.ac.in (14.139.34.3)
Host is up (0.13s latency).
Not shown: 989 filtered ports
PORT     STATE  SERVICE
53/tcp   open   domain
80/tcp   open   http
110/tcp  open   pop3
143/tcp  open   imap
443/tcp  open   https
465/tcp  open   smtps
587/tcp  closed submission
993/tcp  open   imaps
995/tcp  open   pop3s
3306/tcp closed mysql
8000/tcp closed http-alt
Aggressive OS guesses: Linux 3.11 - 4.1 (99%), Linux 3.18 (98%), Linux 3.5 (96%), Linux 2.6.32 (96%), Linux 3.2 - 3.8 (96%), WatchGuard Fireware 11.8 (96%), IPFire 2.11 firewall (Linux 2.6.32) (96%), Linux 3.8 (95%), DD-WRT v24-sp1 (Linux 2.4) (95%), Linux 3.1 - 3.2 (95%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.4
Host is up (0.063s latency).
Not shown: 975 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
23/tcp    filtered telnet
25/tcp    filtered smtp
79/tcp    filtered finger
80/tcp    open     http
212/tcp   filtered anet
445/tcp   filtered microsoft-ds
513/tcp   filtered login
514/tcp   filtered shell
541/tcp   filtered uucp-rlogin
1054/tcp  filtered brvread
1073/tcp  filtered bridgecontrol
1248/tcp  filtered hermes
2144/tcp  filtered lv-ffx
2288/tcp  filtered netml
2301/tcp  filtered compaqdiag
2323/tcp  filtered 3d-nfsd
3005/tcp  filtered deslogin
3269/tcp  filtered globalcatLDAPssl
5555/tcp  filtered freeciv
6001/tcp  open     X11:1
6580/tcp  filtered parsec-master
8080/tcp  open     http-proxy
49156/tcp filtered unknown
65129/tcp filtered unknown
Device type: general purpose|firewall
Running (JUST GUESSING): Linux 3.X|4.X|2.6.X (93%), WatchGuard Fireware 11.X (86%), IPFire 2.X (86%)
OS CPE: cpe:/o:linux:linux_kernel:3.8 cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:2.6.32 cpe:/o:watchguard:fireware:11.8 cpe:/o:ipfire:ipfire:2.11
Aggressive OS guesses: Linux 3.8 (93%), Linux 3.11 - 4.1 (92%), Linux 3.13 (88%), Linux 3.0 (88%), Linux 3.16 (87%), Linux 2.6.32 (87%), Linux 3.10 - 3.12 (86%), Linux 4.4 (86%), Linux 3.2 - 3.8 (86%), WatchGuard Fireware 11.8 (86%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for mail.alumni.iitmandi.ac.in (14.139.34.7)
Host is up (0.053s latency).
Not shown: 969 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
23/tcp    filtered telnet
25/tcp    filtered smtp
53/tcp    open     domain
80/tcp    open     http
110/tcp   open     pop3
143/tcp   open     imap
445/tcp   filtered microsoft-ds
513/tcp   filtered login
514/tcp   filtered shell
587/tcp   open     submission
687/tcp   filtered asipregistry
993/tcp   open     imaps
995/tcp   open     pop3s
1084/tcp  filtered ansoft-lm-2
2040/tcp  filtered lam
2323/tcp  filtered 3d-nfsd
2869/tcp  filtered icslap
3003/tcp  filtered cgms
3005/tcp  filtered deslogin
3517/tcp  filtered 802-11-iapp
5555/tcp  filtered freeciv
6100/tcp  filtered synchronet-db
6101/tcp  filtered backupexec
7911/tcp  filtered unknown
9003/tcp  filtered unknown
9943/tcp  filtered unknown
10000/tcp open     snet-sensor-mgmt
14238/tcp filtered unknown
20000/tcp open     dnp
20222/tcp filtered ipulse-ics
Aggressive OS guesses: Vyatta router (Linux 2.6.26) (96%), Linux 2.6.18 (96%), Netgear ReadyNAS Duo NAS device (RAIDiator 4.1.4) (96%), Zhone 6211-I3 series ADSL2+ modem (96%), Linux 2.6.28 (94%), Linux 3.11 - 4.1 (92%), Linux 3.5 (91%), Linux 2.6.32 (91%), Linux 2.6.26 (91%), Linux 3.2 - 3.8 (91%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.8
Host is up (0.085s latency).
Not shown: 995 filtered ports
PORT      STATE  SERVICE
80/tcp    open   http
389/tcp   open   ldap
443/tcp   open   https
3306/tcp  closed mysql
10000/tcp open   snet-sensor-mgmt
Device type: general purpose|firewall
Running (JUST GUESSING): Linux 3.X|2.6.X (97%), WatchGuard Fireware 11.X (90%)
OS CPE: cpe:/o:linux:linux_kernel:3.8 cpe:/o:watchguard:fireware:11.8 cpe:/o:linux:linux_kernel:2.6
Aggressive OS guesses: Linux 3.8 (97%), Linux 3.0 (92%), Linux 3.2 - 3.8 (92%), Linux 3.5 (90%), WatchGuard Fireware 11.8 (90%), Linux 3.1 - 3.2 (89%), Linux 2.6.32 - 2.6.39 (89%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for mail.projects.iitmandi.ac.in (14.139.34.9)
Host is up (0.22s latency).
Not shown: 991 filtered ports
PORT      STATE  SERVICE
80/tcp    open   http
110/tcp   open   pop3
143/tcp   open   imap
389/tcp   closed ldap
443/tcp   open   https
465/tcp   open   smtps
587/tcp   closed submission
993/tcp   open   imaps
10000/tcp open   snet-sensor-mgmt
Device type: general purpose|firewall|WAP
Running (JUST GUESSING): Linux 3.X|4.X|2.6.X|2.4.X (93%), WatchGuard Fireware 11.X (86%), IPFire 2.X (86%)
OS CPE: cpe:/o:linux:linux_kernel:3.8 cpe:/o:linux:linux_kernel:4 cpe:/o:watchguard:fireware:11.8 cpe:/o:linux:linux_kernel:2.6.32 cpe:/o:ipfire:ipfire:2.11 cpe:/o:linux:linux_kernel:2.4
Aggressive OS guesses: Linux 3.8 (93%), Linux 3.11 - 4.1 (92%), Linux 3.13 (88%), Linux 3.0 (87%), Linux 4.4 (86%), Linux 3.16 (86%), Linux 3.2 - 3.8 (86%), WatchGuard Fireware 11.8 (86%), IPFire 2.11 firewall (Linux 2.6.32) (86%), Linux 2.6.32 (85%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.10
Host is up (0.20s latency).
Not shown: 959 filtered ports, 36 closed ports
PORT     STATE SERVICE
21/tcp   open  ftp
80/tcp   open  http
443/tcp  open  https
8000/tcp open  http-alt
8082/tcp open  blackice-alerts
Aggressive OS guesses: DD-WRT v23 (Linux 2.4.36) (96%), Netgear ReadyNAS Duo NAS device (RAIDiator 4.1.4) (96%), Lexmark Z2400 printer (94%), Linux 3.11 - 4.1 (92%), Linux 3.2 - 3.8 (92%), Linux 3.6 (92%), Ubiquiti EdgeSwitch (Linux 3.6) (92%), Linux 2.6.24 (91%), Linux 2.6.31 (91%), AXIS 205 Network Camera, Buffalo TeraStation NAS device, Linksys WAP54G WAP, or Sony SNC-RZ50N network camera (91%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.11
Host is up (0.054s latency).
Not shown: 979 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
23/tcp    filtered telnet
25/tcp    filtered smtp
53/tcp    open     domain
80/tcp    open     http
445/tcp   filtered microsoft-ds
513/tcp   filtered login
514/tcp   filtered shell
667/tcp   filtered disclose
1066/tcp  filtered fpo-fns
1641/tcp  filtered invision
2191/tcp  filtered tvbus
2323/tcp  filtered 3d-nfsd
3005/tcp  filtered deslogin
5555/tcp  filtered freeciv
6580/tcp  filtered parsec-master
7002/tcp  filtered afs3-prserver
8080/tcp  open     http-proxy
9898/tcp  filtered monkeycom
19842/tcp filtered unknown
51103/tcp filtered unknown
Aggressive OS guesses: Vyatta router (Linux 2.6.26) (96%), Linux 2.6.18 (96%), Netgear ReadyNAS Duo NAS device (RAIDiator 4.1.4) (96%), Zhone 6211-I3 series ADSL2+ modem (96%), Linux 2.6.28 (94%), Linux 3.11 - 4.1 (92%), Linux 2.6.26 (91%), Barracuda Web Filter (91%), Linux 3.5 (91%), Linux 2.6.32 (91%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.17
Host is up (0.052s latency).
Not shown: 980 closed ports
PORT      STATE    SERVICE
22/tcp    open     ssh
23/tcp    filtered telnet
25/tcp    filtered smtp
80/tcp    open     http
445/tcp   filtered microsoft-ds
513/tcp   filtered login
514/tcp   filtered shell
987/tcp   filtered unknown
2020/tcp  filtered xinupageserver
2323/tcp  filtered 3d-nfsd
2608/tcp  filtered wag-service
2869/tcp  filtered icslap
3005/tcp  filtered deslogin
5555/tcp  filtered freeciv
5800/tcp  filtered vnc-http
5900/tcp  open     vnc
8042/tcp  filtered fs-agent
15742/tcp filtered unknown
32775/tcp filtered sometimes-rpc13
51103/tcp filtered unknown
Device type: general purpose
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3.8
OS details: Linux 3.8

Nmap scan report for 14.139.34.24
Host is up (0.061s latency).
Not shown: 957 closed ports
PORT      STATE    SERVICE
23/tcp    filtered telnet
25/tcp    filtered smtp
80/tcp    open     http
111/tcp   filtered rpcbind
135/tcp   open     msrpc
139/tcp   open     netbios-ssn
445/tcp   filtered microsoft-ds
513/tcp   filtered login
514/tcp   filtered shell
1023/tcp  open     netvenuechat
1433/tcp  open     ms-sql-s
1720/tcp  filtered h323q931
1801/tcp  open     msmq
2103/tcp  open     zephyr-clt
2105/tcp  open     eklogin
2107/tcp  open     msmq-mgmt
2323/tcp  filtered 3d-nfsd
2383/tcp  open     ms-olap4
2605/tcp  filtered bgpd
2608/tcp  filtered wag-service
3001/tcp  open     nessus
3005/tcp  filtered deslogin
3306/tcp  open     mysql
3389/tcp  open     ms-wbt-server
3690/tcp  open     svn
4004/tcp  filtered pxc-roid
5440/tcp  filtered unknown
5555/tcp  filtered freeciv
7911/tcp  filtered unknown
7938/tcp  filtered lgtomapper
8080/tcp  open     http-proxy
8085/tcp  open     unknown
8086/tcp  open     d-s-n
8994/tcp  filtered unknown
9000/tcp  open     cslistener
10012/tcp filtered unknown
27715/tcp filtered unknown
49152/tcp open     unknown
49153/tcp open     unknown
49154/tcp open     unknown
49155/tcp open     unknown
49156/tcp open     unknown
49157/tcp open     unknown
Aggressive OS guesses: Microsoft Windows Server 2012 (99%), Microsoft Windows Server 2012 or Windows Server 2012 R2 (99%), Microsoft Windows Server 2012 R2 (97%), Linux 3.18 (94%), Microsoft Windows 7 Professional (93%), Oracle Solaris 11 (93%), Sun Solaris 10 (93%), Microsoft Windows Server 2008 R2 SP1 (93%), Microsoft Windows Server 2008 (92%), Microsoft Windows Server 2008 R2 (92%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.26
Host is up (0.069s latency).
Not shown: 967 closed ports
PORT      STATE    SERVICE
23/tcp    filtered telnet
25/tcp    filtered smtp
80/tcp    open     http
135/tcp   open     msrpc
139/tcp   open     netbios-ssn
445/tcp   filtered microsoft-ds
513/tcp   filtered login
514/tcp   filtered shell
648/tcp   filtered rrp
720/tcp   filtered unknown
1023/tcp  open     netvenuechat
1433/tcp  open     ms-sql-s
1801/tcp  open     msmq
1974/tcp  filtered drp
2103/tcp  open     zephyr-clt
2105/tcp  open     eklogin
2107/tcp  open     msmq-mgmt
2323/tcp  filtered 3d-nfsd
2383/tcp  open     ms-olap4
2605/tcp  filtered bgpd
3005/tcp  filtered deslogin
3389/tcp  open     ms-wbt-server
5555/tcp  filtered freeciv
9998/tcp  filtered distinct32
17877/tcp filtered unknown
49152/tcp open     unknown
49153/tcp open     unknown
49154/tcp open     unknown
49155/tcp open     unknown
49156/tcp open     unknown
49157/tcp open     unknown
49158/tcp open     unknown
49159/tcp open     unknown
Aggressive OS guesses: Microsoft Windows Vista Home Premium SP1 (96%), Vonage V-Portal VoIP adapter (94%), Sun OpenSolaris 2009.06 (94%), Microsoft Windows Vista SP0 or SP1, Windows Server 2008 SP1, or Windows 7 (91%), Microsoft Windows Server 2008 R2 SP1 (89%), Microsoft Windows Server 2008 R2 or Windows 8 (89%), Microsoft Windows Server 2008 (89%), Microsoft Windows Server 2008 R2 (89%), Microsoft Windows 7 SP1 (89%), Ambit U10C018 or Cisco EPC3925 cable modem, or Tandberg video conferencing system (89%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.27
Host is up (0.068s latency).
Not shown: 999 filtered ports
PORT   STATE SERVICE
22/tcp open  ssh
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.10 (98%), Linux 4.0 (98%), Linux 3.10 - 3.12 (98%), Linux 4.4 (98%), Linux 3.18 (98%), Linux 2.6.32 (97%), Linux 2.6.39 (97%), Dish Network Hopper media device (96%), Linux 2.6.32 - 2.6.35 (96%), Linux 2.6.32 or 3.10 (96%)
No exact OS matches for host (test conditions non-ideal).

Nmap scan report for 14.139.34.43
Host is up (0.059s latency).
Not shown: 976 closed ports
PORT      STATE    SERVICE
22/tcp    filtered ssh
23/tcp    filtered telnet
25/tcp    filtered smtp
80/tcp    open     http
139/tcp   open     netbios-ssn
425/tcp   filtered icad-el
427/tcp   filtered svrloc
445/tcp   filtered microsoft-ds
513/tcp   filtered login
514/tcp   filtered shell
726/tcp   filtered unknown
1500/tcp  filtered vlsi-lm
2323/tcp  filtered 3d-nfsd
3005/tcp  filtered deslogin
3071/tcp  filtered csd-mgmt-port
3306/tcp  open     mysql
5060/tcp  filtered sip
5555/tcp  filtered freeciv
8080/tcp  open     http-proxy
8081/tcp  open     blackice-icecap
8082/tcp  open     blackice-alerts
9003/tcp  filtered unknown
9593/tcp  filtered cba8
50500/tcp filtered unknown
Aggressive OS guesses: Linux 3.2 - 3.8 (99%), WatchGuard Fireware 11.8 (99%), Linux 3.8 (98%), Linux 3.11 - 4.1 (98%), Linux 3.5 (97%), Linux 3.18 (97%), Linux 2.6.32 (96%), IPFire 2.11 firewall (Linux 2.6.32) (96%), Linux 3.1 - 3.2 (96%), Linux 2.6.32 - 2.6.39 (95%)
No exact OS matches for host (test conditions non-ideal).
```

## 2. Domain Name
For this task, i used the **"Who is"** query command in terminal. Unfortunately, this command doesn't work for subdomains like <https://students.iitmandi.ac.in> and i used it like

```bash
whois iitmandi.ac.in
```

which gave the following output,

```txt
Domain ID:D4020030-AFIN
Domain Name:IITMANDI.AC.IN
Created On:02-Feb-2010 10:09:08 UTC
Last Updated On:23-Dec-2014 08:30:40 UTC
Expiration Date:02-Feb-2020 10:09:08 UTC
Sponsoring Registrar:ERNET India (R9-AFIN)
```

,which points out to the fact that <http://www.iitmandi.ac.in> was bought from **ERNET India**, which has been appointed as an exclusive domain registrar for the education and research domains registering the domains under the .in registry from 2005 It registers Domains at second and third level for ac.in, edu.in and res.in zones.

Also, i think that the company who registered the top level domain should have also registered the subdomain <https://students.iitmandi.ac.in> . So, **ERNET India** should have registered this subdomain also.

## 3. Location of DuckDuckGo Data Centres
For this task, i first searched a bit and first found out the IP address of <https://duckduckgo.com/> by using **host** command.

```bash
host duckduckgo.com
```

which gave the output

```text
duckduckgo.com has address 46.51.218.82
duckduckgo.com mail is handled by 10 in1-smtp.messagingengine.com.
duckduckgo.com mail is handled by 20 in2-smtp.messagingengine.com.
```

Then i used **geoiplookup** to track where this IP address was residing.

```bash
geoiplookup 46.51.218.82 
```

which gave the output.

```text
GeoIP Country Edition: SG, Singapore
```

So, the data centre from which i was receiving the packets was from **Singapore**.

Also, on the **Duck Cooperations** website, it is mentioned that **DuckDuckGo have servers on Amazon EC2 across the world**. [Here is the source](https://duck.co/help/company/architecture). **Amazon AWS Servers are located at 52 locations across the world**. I couldn't list them all here. You can go to <https://aws.amazon.com/about-aws/global-infrastructure/> to see all the data centres.