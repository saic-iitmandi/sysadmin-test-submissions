# Findings

## IIT Mandi Network Ports and Computers

I am using Nmap to find out the open ports and the operating system running.

For `iitmandi.ac.in` (IP: 204.197.248.190) 

1. 20/tcp   closed ftp-data
2. 21/tcp    open   ftp
3. 26/tcp    open   rsftp
4. 53/tcp    open   domain
5. 80/tcp    open   http
6. 110/tcp   open   pop3
7. 143/tcp   open   imap
8. 443/tcp   open   https
9. 465/tcp   open   smtps
10. 587/tcp   open   submission
11. 993/tcp   open   imaps
12. 995/tcp   open   pop3s
13. 2200/tcp  open   ici

Nmap guesses the OS to be based on Linux 2.6 kernel.

According to `14.139.34.11` the SNTC server runs on `Apache2` on `Ubuntu`. Also Nmap guesses OS to be based on Linux 3.11 - 4.1.

Public facing computers:

1. http://14.139.34.2/ - Internet Gateway
2. http://14.139.34.3/ - IIT Mandi Students page
3. http://14.139.34.4/ - Library
4. http://14.139.34.7/ - Alumni Login
5. http://14.139.34.8/ - Defaut webpage for server
6. http://14.139.34.9/ - Staff Webmail
7. http://14.139.34.10/ - Link to www.research.iitmandi.ac.in
8. http://14.139.34.11/ - Apache2 Ubuntu Default Page
9. http://14.139.34.17/ - CITHR
10. http://14.139.34.24/ - OAS
11. http://14.139.34.26/ - new OAS page

NOTE: Only open ports are mentioned.

For `students.iitmandi.ac.in` open ports are (IP: 14.139.34.3)

1. 53/tcp    open   domain
2. 80/tcp    open   http
3. 110/tcp   open   pop3
4. 143/tcp   open   imap
5. 443/tcp   open   https
6. 465/tcp   open   smtps
7. 993/tcp   open   imaps
8. 995/tcp   open   pop3s
9. 10000/tcp open   snet-sensor-mgmt

Open ports for `14.139.34.2`

1. 22/tcp    open     ssh
2. 53/tcp    open     domain
3. 80/tcp    open     http
4. 443/tcp   open     https
5. 3000/tcp  open     ppp
6. 5001/tcp  open     commplex-link
7. 7001/tcp  open     afs3-callback
8. 10000/tcp open     snet-sensor-mgmt

Open ports for `14.139.34.4`

1. 22/tcp   open     ssh
2. 80/tcp   open     http
3. 6001/tcp open     X11:1
4. 8080/tcp open     http-proxy

Open ports for `14.139.34.7`

1. 22/tcp    open     ssh
2. 53/tcp    open     domain
3. 80/tcp    open     http
4. 110/tcp   open     pop3
5. 143/tcp   open     imap
6. 587/tcp   open     submission
7. 993/tcp   open     imaps
8. 995/tcp   open     pop3s
9. 10000/tcp open     snet-sensor-mgmt
10. 20000/tcp open     dnp

This file would be too long if I include port information for every PC on the network.

## Domain Provider for IIT Mandi

`students.iitmandi.ac.in` is a subdomain of `iitmandi.ac.in` which was given to the institute by `ERNET India`.
I found this information by this [Whois lookup](https://www.whois.com/whois/iitmandi.ac.in).


## Location of DuckDuckGo's data centres

DuckDuckGo is hosted by Amazon Web Services (AWS). It runs on 4 AWS datacenters (California, Virginia, Singapore, Ireland).

Source: http://highscalability.com/blog/2013/1/28/duckduckgo-architecture-1-million-deep-searches-a-day-and-gr.html

(Unfortunately, I could not find a more recent source despite all attempts to search.)

`nslookup duckduckgo.com` and `ping duckduckgo.com` yield the following IP addresses, and using https://www.iplocation.net/ I found which datacentre each IP corresponds to

1. `176.34.131.233` `176.34.155.20` `176.34.135.167` `46.51.197.89` `54.229.105.203` `54.229.105.92` - Dublin, Ireland
2. `46.51.218.82` - Singapore

I can't find any other way to find out IP addresses for any other datacentre.

# What I learnt

1. Usage of `Nmap` to know open ports, and operating system (-O flag).
2. Basic usage of `nslookup`

