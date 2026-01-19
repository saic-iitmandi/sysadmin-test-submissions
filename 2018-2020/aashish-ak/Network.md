# sysadmin-test Network

In this all the answers to the questions stated in the Networking section of the sysadmin-test are listed.

## Q-1

In this question the task was to find out (1) all the
PCs of `students.iitmandi.ac.in` which are public, facing and (2) all the ports open and (3) what kind of OS they're running on. So first i found this amazing [blog](https://blog.securitycompass.com/what-is-an-easy-way-to-discover-all-of-my-external-facing-systems-db1ef3ab87c5) and came to know about `nmap` a powerful tool to perform port mapping and thus in order to get which of the ports are open i ran the command below which would have gave me the open ports their OS and which host is up and what services are the ports for:
```bash
sudo nmap -sSU -O students.iitmandi.ac.in
```
which gave me the following output:
```bash
Starting Nmap 7.01 ( https://nmap.org ) at 2018-02-04 20:52 IST
Nmap scan report for students.iitmandi.ac.in (14.139.34.3)
Host is up (0.076s latency).
rDNS record for 14.139.34.3: mail.students.iitmandi.ac.in
Not shown: 998 open|filtered ports, 986 filtered ports
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
53/udp    open   domain
123/udp   closed ntp
Device type: general purpose
Running (JUST GUESSING): Linux 3.X|4.X|2.6.X (87%)
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:2.6.32
Aggressive OS guesses: Linux 3.11 - 4.1 (87%), Linux 3.10 - 3.19 (86%), Linux 3.13 (86%), Linux 2.6.32 (86%), Linux 2.6.18 - 2.6.22 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 14 hops

OS detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 95.22 seconds

```
Now from this i came to know that there are 16 ports which are public facing and the closed ones are `123` which is a udp port and `3306`, `5000`, `8000`,`587` and `389`all being tcp ports, rest all other 10 ports are open and the OS they're operating on are all different versions of linux, but i'm confused about the PCs which are public facing and then i discovered this [site](https://centralops.net/co/domaindossier.aspx) where when i input the domain name as `students.iitmandi.ac.in` then got a similar output but the OS it mentioned there was Ubuntu.

 ## Q-2
The `domain registrar and registry sponsor`of `students.iitmandi.ac.in` which i found using WhoIs [here](https://www.whois.com/whois/iitmandi.ac.in) and [here](https://whois.easycounter.com/iitmandi.ac.in)   are  **INRegistry and ERNET India (R9-AFIN)** respectively , it has `ns1.iitmandi.net.in`, `ns2.iitmandi.net.in` as it's name servers, it's **Web Hosting Provider**  is `NKN-SUPERCORE-SEGMENT-2 `  and it is expiring on **02/02/2020** and was registered and last updated on **02/02/2010** and **23/12/2014** respectively. I learned about domain registration and domain host in this. Also i went to `WhoIs` from [here](https://hostadvice.com/tools/whois/#students.iitmandi.ac.in).

## Q-3

In this question we needed to find the data centers owned by [DuckDuckGo](https://duckduckgo.com) , so when i browsed through the internet and after asking on reddit, i ended up [here](https://duck.co/help/company/architecture), which is the official help website of DuckDuckGO, and i found link to an [article](http://highscalability.com/blog/2013/1/28/duckduckgo-architecture-1-million-deep-searches-a-day-and-gr.html) there, where it was mentioned that DuckDuckGo **does not own any data centers** but is hosted by **Amazon Web Services (AWS)** and runs on four AWS data centers, that are located in **California, Virginia, Singapore and Ireland**.

---------
By: Aashish Kumar (B16001)
GitHub: [aashish-ak](https://github.com/aashish-ak/)
---------
