### 1. Information about 14.139.34.0/24 

I used `nmap` to get information about open ports and operating system.
The command used was : `sudo nmap -O 14.139.34.0/24`

**14.139.34.2** :
| PORT        | STATE           | SERVICE  |
| ------------- |-------------| -----|
|22/tcp    |open     |ssh
|25/tcp    |filtered |smtp
|53/tcp    |open     |domain
|80/tcp    |open     |http
|443/tcp   |open     |https
|445/tcp   |filtered |microsoft-ds
|3000/tcp  |open     |ppp
|5001/tcp  |open     |commplex-link
|5060/tcp  |filtered |sip
|5061/tcp  |filtered |sip-tls
|7001/tcp  |open     |afs3-callback
|9000/tcp  |filtered |cslistener
|10000/tcp |open     |snet-sensor-mgmt

**mail.students.iitmandi.ac.in (14.139.34.3)** :
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3.13 cpe:/o:linux:linux_kernel:4.2
OS details: Linux 3.13 or 4.2

| PORT        | STATE           | SERVICE  |
| ------------- |-------------| -----|
| 53/tcp   | open   | domain
| 80/tcp   | open   | http
| 110/tcp  | open   | pop3
| 143/tcp  | open   | imap
| 389/tcp  | closed | ldap
| 443/tcp  | open   | https
| 465/tcp  | open   | smtps
| 587/tcp  | closed | submission
| 993/tcp  | open   | imaps
| 995/tcp  | open   | pop3s
| 3306/tcp | closed | mysql
| 5000/tcp | closed | upnp
| 8000/tcp | closed | http-alt
| 10000/tcp| open   | snet-sensor-mgmt

**14.139.34.4** :
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3.13 cpe:/o:linux:linux_kernel:4.2
OS details: Linux 3.13 or 4.2

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
| 22/tcp   | open     | ssh
| 25/tcp   | filtered | smtp
| 80/tcp   | open     | http
| 445/tcp  | filtered | microsoft-ds
| 5060/tcp | filtered | sip
| 5061/tcp | filtered | sip-tls
| 6001/tcp | open     | X11:1
| 8080/tcp | open     | http-proxy

**mail.alumni.iitmandi.ac.in (14.139.34.7)** :

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
| 22/tcp   | open     | ssh
| 25/tcp   | filtered | smtp
| 53/tcp   | open     | domain
| 80/tcp   | open     | http
| 110/tcp  | open     | pop3
| 143/tcp  | open     | imap
| 445/tcp  | filtered | microsoft-ds
| 587/tcp  | open     | submission
| 993/tcp  | open     | imaps
| 995/tcp  | open     | pop3s
| 5060/tcp | filtered | sip
| 5061/tcp | filtered | sip-tls
| 10000/tcp| open     | snet-sensor-mgmt
| 20000/tcp| open     | dnp

**14.139.34.8** :

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
| 53/tcp    | closed | domain
| 80/tcp    | open   | http
| 389/tcp   | open   | ldap
| 443/tcp   | open   | https
| 3306/tcp  | closed | mysql
| 10000/tcp | open   | snet-sensor-mgmt

**mail.projects.iitmandi.ac.in (14.139.34.9)** :

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
| 53/tcp    | closed | domain
| 80/tcp    | open   | http
| 110/tcp   | open   | pop3
| 143/tcp   | open   | imap
| 389/tcp   | closed | ldap
| 443/tcp   | open   | https
| 465/tcp   | open   | smtps
| 587/tcp   | closed | submission
| 993/tcp   | open   | imaps
| 10000/tcp | open   | snet-sensor-mgmt

**14.139.34.10** :

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
| 21/tcp   | open | ftp
| 80/tcp   | open | http
| 443/tcp  | open | https
| 8000/tcp | open | http-alt
| 8082/tcp | open | blackice-alerts

**14.139.34.11** :
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3.13 cpe:/o:linux:linux_kernel:4.2
OS details: Linux 3.13 or 4.2

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
| 22/tcp   | open     | ssh
| 25/tcp   | filtered | smtp
| 53/tcp   | open     | domain
| 80/tcp   | open     | http
| 445/tcp  | filtered | microsoft-ds
| 5060/tcp | filtered | sip
| 5061/tcp | filtered | sip-tls
| 8080/tcp | open     | http-proxy

**14.139.34.17** :

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
| 22/tcp   | open     | ssh
| 25/tcp   | filtered | smtp
| 80/tcp   | open     | http
| 445/tcp  | filtered | microsoft-ds
| 5060/tcp | filtered | sip
| 5061/tcp | filtered | sip-tls
| 5800/tcp | open     | vnc-http
| 5900/tcp | open     | vnc

**14.139.34.24** :

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
|25/tcp    | filtered | smtp
|80/tcp    | open     | http
|135/tcp   | open     | msrpc
|139/tcp   | open     | netbios-ssn
|445/tcp   | filtered | microsoft-ds
|1023/tcp  | open     | netvenuechat
|1433/tcp  | open     | ms-sql-s
|1801/tcp  | open     | msmq
|2103/tcp  | open     | zephyr-clt
|2105/tcp  | open     | eklogin
|2107/tcp  | open     | msmq-mgmt
|2383/tcp  | open     | ms-olap4
|3001/tcp  | open     | nessus
|3306/tcp  | open     | mysql
|3389/tcp  | open     | ms-wbt-server
|3690/tcp  | open     | svn
|5060/tcp  | filtered | sip
|5061/tcp  | filtered | sip-tls
|8080/tcp  | open     | http-proxy
|8085/tcp  | open     | unknown
|8086/tcp  | open     | d-s-n
|49152/tcp | open     | unknown
|49153/tcp | open     | unknown
|49154/tcp | open     | unknown
|49155/tcp | open     | unknown
|49156/tcp | open     | unknown
|49157/tcp | open     | unknown

**14.139.34.26** :

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
| 25/tcp    | filtered | smtp
| 80/tcp    | open     | http
| 135/tcp   | open     | msrpc
| 139/tcp   | open     | netbios-ssn
| 445/tcp   | filtered | microsoft-ds
| 1023/tcp  | open     | netvenuechat
| 1024/tcp  | open     | kdm
| 1433/tcp  | open     | ms-sql-s
| 1801/tcp  | open     | msmq
| 2103/tcp  | open     | zephyr-clt
| 2105/tcp  | open     | eklogin
| 2107/tcp  | open     | msmq-mgmt
| 2383/tcp  | open     | ms-olap4
| 3389/tcp  | open     | ms-wbt-server
| 5060/tcp  | filtered | sip
| 5061/tcp  | filtered | sip-tls
| 49152/tcp | open     | unknown
| 49153/tcp | open     | unknown
| 49154/tcp | open     | unknown
| 49155/tcp | open     | unknown
| 49156/tcp | open     | unknown
| 49159/tcp | open     | unknown
| 49167/tcp | open     | unknown

**14.139.34.27** :

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
| 22/tcp | open | ssh

**14.139.34.43** :
Device type: broadband router
Running: Linux 3.X
OS CPE: cpe:/o:linux:linux_kernel:3
OS details: OpenWrt 12.09-rc1 Attitude Adjustment (Linux 3.3 - 3.7)

| PORT     | STATE    | SERVICE |
|----------| ---------| --------|
| 22/tcp   | open     | ssh
| 25/tcp   | filtered | smtp
| 80/tcp   | open     | http
| 139/tcp  | open     | netbios-ssn
| 445/tcp  | filtered | microsoft-ds
| 3306/tcp | open     | mysql
| 5060/tcp | filtered | sip
| 5061/tcp | filtered | sip-tls
| 8080/tcp | open     | http-proxy
| 8081/tcp | open     | blackice-icecap
| 8082/tcp | open     | blackice-alerts

### 2. For students.iitmandi.ac.in, you need to find out from what company the domain has been bought

From **ERNET - Education and Research Network, India**. 

I first tried at whois.net but couldn't find the answer. So I googled from where does `ac.in` type domain are purchased and got to the answer.

### 3. Find data centers of duckduckgo

I have so far found 5 data centers - 
California, Virginia, Singapore, Ireland, Illinois

I googled and found out that it's datacenters are on Amazon AWS.
I used VPN which was routing in New York. Then I used `traceroute` to find the path of packet. I found each Amazon's datacenter in between and kept note of it. I am not sure it this is the correct way to find it. Hence, I didn't VPN into other countries to check it. 