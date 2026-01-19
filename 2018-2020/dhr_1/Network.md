Problem 1: 

First task was to find subdomains of iitmandi.ac.in . So using the website pentest-tools.com . I got the following list:

Subdomain 						IP address 			Netname (whois) 	Country (whois) 
gateway.iitmandi.ac.in 			14.139.34.2 		NKN-IIT-MANDI 		IN 	
vpn.iitmandi.ac.in 				14.139.34.2 		NKN-IIT-MANDI 		IN 	
students.iitmandi.ac.in 		14.139.34.3 		NKN-IIT-MANDI 		IN 	
library.iitmandi.ac.in 			14.139.34.4 		NKN-IIT-MANDI 		IN 	
www.faculty.iitmandi.ac.in 		14.139.34.6 		NKN-IIT-MANDI 		IN 	
staff.iitmandi.ac.in 			14.139.34.6 		NKN-IIT-MANDI 		IN 	
faculty.iitmandi.ac.in 			14.139.34.6 		NKN-IIT-MANDI 		IN 	
se.iitmandi.ac.in 				14.139.34.8 		NKN-IIT-MANDI 		IN 	
projects.iitmandi.ac.in 		14.139.34.9 		NKN-IIT-MANDI 		IN 	
ncvpripg.iitmandi.ac.in 		14.139.34.10 		NKN-IIT-MANDI 		IN 	
www.rinai.iitmandi.ac.in 		14.139.34.10 		NKN-IIT-MANDI 		IN 	
localhost.iitmandi.ac.in 		127.0.0.1 			SPECIAL-IPV4-LOOPBACK-IANA-RESERVED 	US 	
webmail.iitmandi.ac.in 			204.197.248.190 	PRIVATE-TX-6 		US 	
ftp.iitmandi.ac.in 				204.197.248.190 	PRIVATE-TX-6 		US 	
iitmandi.ac.in 					204.197.248.190 	PRIVATE-TX-6 		US 	
www.iitmandi.ac.in 				204.197.248.190 	PRIVATE-TX-6 		US 	
mail.iitmandi.ac.in 			204.197.248.190 	PRIVATE-TX-6 		US	 	
cpanel.iitmandi.ac.in 			204.197.248.190 	PRIVATE-TX-6 	    US

I also found 2 other ip's:
    14.139.34.11
    14.139.34.17 uhl.iitmandi.ac.in

I already knew how to get all the open ports using nmap. So I used nmap. In nmap man page i found that i can also get os using nmap.
So, work done.
Synopsis of the findings is given below:

Complete information of the tests are in the folder NetworkFile.
Synopsis:

gateway.iitmandi.ac.in/vpn.iitmandi.ac.in
    Discovered open port 80/tcp on 14.139.34.2
    Discovered open port 22/tcp on 14.139.34.2
    Discovered open port 53/tcp on 14.139.34.2
    Discovered open port 443/tcp on 14.139.34.2
    Discovered open port 5001/tcp on 14.139.34.2
    
    OS: Linux(Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel)
    
    For complete information please refer to Nmap result file : NetworkFiles/gateway.md

students.iitmandi.ac.in
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
    
    On port 10000 webmin is running.
    Aggressive OS guesses: Linux 3.11 - 4.1 (93%), Linux 3.13 (89%), Linux 4.4 (87%), Linux 3.2 - 3.8 (87%), WatchGuard Fireware 11.8 (87%), 
                            Linux 3.16 (87%), IPFire 2.11 firewall (Linux 2.6.32) (87%), Linux 3.10 - 3.12 (86%), Linux 2.6.32 (86%), Linux 3.8 (86%)
    
    For Complete information please refer to Nmap result file : NetworkFiles/students.md
    
library.iitmandi.ac.in
    Discovered open port 8080/tcp on 14.139.34.4
    Discovered open port 22/tcp on 14.139.34.4
    Discovered open port 25/tcp on 14.139.34.4
    Discovered open port 80/tcp on 14.139.34.4
    Discovered open port 6001/tcp on 14.139.34.4
    
    Koha is used for Library managment.
    
    OS: Linux

    Full report in: NetworkFiles/library.md
    
faculty.iitmandi.ac.in/staff.iitmandi.ac.in
    Discovered open port 80/tcp on 14.139.34.6
    Discovered open port 443/tcp on 14.139.34.6
    
    Aggressive OS guesses: Linux 3.2 - 3.8 (93%), Linux 3.8 (93%), WatchGuard Fireware 11.8 (93%), Linux 3.1 - 3.2 (91%), 
                        Linux 3.5 (90%), Linux 2.6.32 - 2.6.39 (90%), Linux 3.0 - 3.2 (89%), Linux 2.6.32 - 3.0 (88%), Linux 2.6.32 (87%), Linux 2.6.32 or 3.10 (87%)

    For Complete Information: NetworkFiles/faculty.md
    
se.iitmandi.ac.in
    Discovered open port 80/tcp on 14.139.34.8
    Discovered open port 443/tcp on 14.139.34.8
    Discovered open port 10000/tcp on 14.139.34.8
    Discovered open port 389/tcp on 14.139.34.8

    Aggressive OS guesses: Linux 3.2 - 3.8 (93%), Linux 3.8 (93%), WatchGuard Fireware 11.8 (93%), Linux 3.5 (91%), Linux 3.1 - 3.2 (90%), 
                            Linux 2.6.32 - 2.6.39 (90%), Linux 3.0 - 3.2 (90%), Linux 2.6.32 (88%), Linux 2.6.32 or 3.10 (88%), Linux 3.0 or 3.5 (88%)

    Full report in : NetworkFiles/se.md
    
projects.iitmandi.ac.in
    Discovered open port 25/tcp on 14.139.34.9
    Discovered open port 110/tcp on 14.139.34.9
    Discovered open port 80/tcp on 14.139.34.9
    Discovered open port 993/tcp on 14.139.34.9
    Discovered open port 443/tcp on 14.139.34.9
    Discovered open port 143/tcp on 14.139.34.9
    Discovered open port 465/tcp on 14.139.34.9
    Discovered open port 10000/tcp on 14.139.34.9
    
    This one is also using webmin.
    
    Aggressive OS guesses: Linux 3.11 - 4.1 (93%), Linux 3.13 (89%), Linux 3.16 (88%), Linux 2.6.32 (88%), Linux 3.2 - 3.8 (88%), Linux 3.8 (88%), 
                            IPFire 2.11 firewall (Linux 2.6.32) (87%), Linux 3.10 - 3.12 (87%), Linux 4.4 (87%), WatchGuard Fireware 11.8 (87%)
                            
    Complete information in: NetworkFiles/projects.md

rinai.iitmandi.ac.in
    Discovered open port 21/tcp on 14.139.34.10
    Discovered open port 22/tcp on 14.139.34.10
    Discovered open port 443/tcp on 14.139.34.10
    Discovered open port 80/tcp on 14.139.34.10
    Discovered open port 8000/tcp on 14.139.34.10
    Discovered open port 8082/tcp on 14.139.34.10

    OS: Unix

    Complete information in: NetworkFiles/rinai.md
    
webmail/ftp/cpanel.iitmandi.ac.in
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
    Discovered open port 26/tcp on 204.197.248.190
    Discovered open port 2200/tcp on 204.197.248.190
    Discovered open port 465/tcp on 204.197.248.190

 	OS: Red Hat Enterprise Linux 7

 14.139.34.11:
    Discovered open port 22/tcp on 14.139.34.11
    Discovered open port 53/tcp on 14.139.34.11
    Discovered open port 8080/tcp on 14.139.34.11
    Discovered open port 80/tcp on 14.139.34.11

    OS: Linux

    More Info in: NetworkFiles/sntc.md
    
uhl.iitmandi.ac.in:
    Discovered open port 80/tcp on 14.139.34.17
    Discovered open port 22/tcp on 14.139.34.17
    Discovered open port 5900/tcp on 14.139.34.17
    Discovered open port 5800/tcp on 14.139.34.17

    OS: Linux

    More info in: NetworkFiles/uhl.md

Problem 2:
    
ERNET is the official registrar for .ac.in domain names. Thus, iitmandi.ac.in was registered by IIT Mandi(address in the registration is of roorkee campus).
Ingormation here: https://www.whois.com/whois/iitmandi.ac.in .We can set up our own subdomains once we have a domain.
Source: https://www.quora.com/Do-you-have-to-purchase-a-sub-domain-if-you-already-have-the-domain 
Comment: IIT Mandi probably have to renew their domain by next year(Maximum lease period is 10 years).


Problem 3:

Duck Duck Go have only one datacenter(Gabriel Weinsberg's basement, not sure if i can call it a datacenter).
Duck Duck Go have their own servers and they also use Amazon EC2 servers. 
Source: https://duck.co/help/company/architecture
According to post(https://duck.co/redir/?u=http%3A%2F%2Fhighscalability.com%2Fblog%2F2013%2F1%2F28%2Fduckduckgo-architecture-1-million-deep-searches-a-day-and-gr.html):
    
    "DuckDuckGo used to run out of Gabriel’s basement. Most components, including all front-end components, are now on AWS." 
    Gabriel is founder and owner of DDG. 
    DDG is running in four AWS datacenters i.e. California, Virginia, Singapore, Ireland.
    Some components are still running from Gabriel Weinsberg's Basement.(like Git repository, crawling, and the real-time Wikipedia index that updates zero-click connects).

    So, DDG operates from 5 datacenters - 4 of AWS(California, Virginia, Singapore, Ireland) and Gabriel Weinsberg's Basement. 
    


    