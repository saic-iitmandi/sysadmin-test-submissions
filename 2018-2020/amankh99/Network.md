By **public facing** I think you mean public ip's so all the ip's which you listed are public ip's.
Private IP Addresses have the following ranges:
10.0.0.0    - 10.255.255.255
172.16.0.0  - 172.31.255.255
192.168.0.0 - 192.168.255.255 

For the information you asked I looked whatismyipaddress.com and pentest-tools.com
I learnt that by the help of the nmap above sites manages to retrieve the information like we can find all the tcp ports opened and other operating system on which system is working.

I scanned 100 common ports by using this - 'https://pentest-tools.com/network-vulnerability-scanning/tcp-port-scanner-online-nmap?run' where you can scan all ports from 1 to 65535 too. Here is the list of common open ports with the services using them.

**Port** 	**State**	**Service name**

25 		open 	smtp 		

53 		open 	domain		

80 		open	http  	

110 	open 	pop3 		

143 	open 	imap		

389 	closed 	ldap 		

443 	open	https

465 	open 	smtp			

587 	closed 	submission 	

993 	open 	imap 	

995 	open 	pop3

3306 	closed 	mysql 				

5000 	closed 	upnp 		

8000 	closed 	http 	

10000 	open	http


**Operating system**

Linux 3.11 - 3.14 

**Extra information**

IP:	14.139.34.3

Decimal:	243999235

Hostname:	mail.students.iitmandi.ac.in

ASN(Autonomous System numbers):	55824

ISP:	National Informatics Centre

Organization:	NKN Core Network

**Company name** from whom the domain name is brought -
ERNET India R9-AFIN

For this above imformation I visited the https://mydomain.com/whois and looked up for the domain iitmandi.ac.in and then at the sponsoring registrant for company name.


For the datacenters of the **duckduckgo** I looked up and found the answer on the **reddit** that duckduckgo.com run on Amazon EC2 servers. Quoting the answer provided-"We both run our own servers and have servers on Amazon EC2 across the world. Your connection generally goes to the closest regional server available to your area. We use PostgreSQL+bucardo, CDB, Solr, Berkeley DB, Amazon S3 and flat files for data."

**Resources** - whatismyip.com, reddit, pentest-tools.com, mydomain.com

**Learning** -
1. how to find which ip is public or private.

2. Which ports corresponds to which service.
               
3. I also learnt about information we can retrieve from ip address and I though not used but find some terminal used for finding above information.
