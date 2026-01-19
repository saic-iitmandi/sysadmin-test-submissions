
# Sahil Yadav, B15130

# Networking Assignment

****

1.	I did an [nmap](https://en.wikipedia.org/wiki/Nmap) on `14.139.34.0/24` which helped me discover hosts and services on the IIT Mandi network.The detailed findings are [here](https://github.com/me-ydv-5/sys-admin/blob/master/nmap.txt) and [here](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt)(verbose version including OS guessing).

	Coming to the question, all the PCs which were public facing had the following IPs and other details :

	Total no. of Public facing systems(at the time of running the test) = 12

	|  Serial No. | 	IP Address | Ports Opened(Service)   |  Suggested OS  |		Uptime Guess	|
	|	---	|	--------   |	--------	|	-----------	 |	----------		|
	|   	1	|	14.139.34.2| 53(domain), 80(http), 443(https), 3000(ppp), 5001(complex-link), 7001(afs3-callback), 10000(snet-sensor-mgmt) |[Linux](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L570)	| 54.880 days (since Wed Dec 13 19:12:07 2017) ||
	|	   2	|	14.139.34.3| 22(ssh), 80(http), 6001(X11:1), 8080(http-proxy)| [Linux](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L594)	| 55.101 days (since Wed Dec 13 13:54:01 2017) 	||
	|		3	|	14.139.34.4	| 22(ssh), 80(http), 6001(X11:1), 8080(http-proxy)	|	[Linux](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L618)	|	55.547 days (since Wed Dec 13 03:12:04 2017)	||
	|		4	| 	14.139.34.7| 22(ssh), 53(domain), 80(http), 110(pop3), 143(imap), 587(submission), 993(imaps), 995(pop3s), 10000(snet-sensor-mgmt), 20000(dnp)| [Linux](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L647)	| 54.728 days (since Wed Dec 13 22:50:42 2017) ||
	|		5	| 	14.139.34.8| 80(http), 389(ldap), 443(https)| [Linux](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L664)	| 55.260 days (since Wed Dec 13 10:04:38 2017) ||
	|		6	|	14.139.34.9| 80(http), 110(pop3), 443(https), 465(smtps), 993(imaps), 10000(snet-sensor-mgmt) | [Linux](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L681) 	| 56.233 days (since Tue Dec 12 10:44:38 2017) ||
	|		7	|	14.139.34.10| 21(ftp), 22(ssh), 80(http), 443(https), 8000(http-alt), 8082(blackice-alerts)	| [Linux](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L699) 	| 55.080 days (since Wed Dec 13 14:24:20 2017) ||
	|		8	|	14.139.34.11| 22(tcp), 53(domain), 80(tcp), 8080(http-proxy)| [Linux](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L721)	| 55.855 days (since Tue Dec 12 19:48:52 2017)	||
	|		9	|	14.139.34.17| 22(ssh), 80(http), 5800(vnc-http), 5900(vnc) | [Linux](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L744)	| 56.227 days (since Tue Dec 12 10:52:28 2017) 	||
	|		10	|	14.139.34.24| 80(http), 135(msrpc), 139(netbios-ssn), 1023(netvenuechat), 1433(ms-sql-s), 1801(msmq), 2103(zephyr-clt), 2105(eklogin), 2107(msmq-mgmt),etc ...	| [Windows](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L788) 	| 7.331 days (since Tue Jan 30 08:23:28 2018)	||
	|		11	|	14.139.34.26| 80(http), 135(msrpc), 139(netbios-ssn),1023(netvenuechat), 1433(ms-sql-s), 1801(msmq), 2103(zephyr-clt), 2105(eklogin), 2107(msmq-mgmt),etc... | [Windows](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L828)	| 54.884 days (since Wed Dec 13 19:06:55 2017)	||
	|		12	|	14.139.34.43| 22(ssh), 80(http), 139(netbios-ssn), 3306(mysql), 8080(http-proxy), 8081(blackice-icecap), 8082(blackice-alerts)	| [Linux](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L867)	| 5.293 days (since Thu Feb  1 09:17:34 2018)	||


	Note that the **Suggested OS** column states the _most probable_ guess of the OS and **NOT** the _exact_ one.

	**Other Details**:

	* All of the machines were `11 hops` away, which is obvious.
	* All of the machines had `TCP prediction sequence` in the enumerated range of `"Good luck!"` , i.e, it's pretty difficult for hackers to spoof the IPs of the machines and take advantage.
	* Since the uptime is guessed by checking the counter, it is probable that the actual uptime is around a week long. (because the counter generally resets itself in around 50 days.)
	* One other observation was, `nmap` doesn't [operate efficiently](https://security.stackexchange.com/questions/21544/nmap-scan-produces-all-unknown?answertab=votes#tab-top) on Windows machine. It lists many ports' status as `unknown` (For example, see [this](https://github.com/me-ydv-5/sys-admin/blob/master/nmap2.txt#L820))

	One query that I would like the examiner to answer (if possible) is the machine with IP `14.139.34.10` issues the [following](https://github.com/me-ydv-5/sys-admin/blob/master/nmap.txt#L2) warning:

	`Warning: 14.139.34.10 giving up on port because retransmission cap hit (10).`

	I tried searching online, but couldn't find something satisfactory because I [didn't even use -T flag](https://stackoverflow.com/questions/14736530/nmap-warning-giving-up-on-port-because-retransmission-cap-hit-2?answertab=active#tab-top) in the first place.

	This [site](https://nmap.org/book/osdetect-usage.html) helped me in detecting and understanding other details on the devices that were up.

****

2. 	students.iitmandi.ac.in works on the servers hosted by **National Knowledge Network, India**.
To find this : I ran the command `dig students.iitmandi.ac.in` and noted down that the A records IP is *14.139.34.3*.
After this, I ran `whois 14.139.34.3` to find about the associated organisation and other things, in which I observed NKN as
the network administrator. Generally the hosting organisation is called as a 'Registrar', I didn't see anything explicit as such. Moreover, since students.iitmandi.ac.in is a subdomain for iitmandi.ac.in, I did `whois iitmandi.ac.in` where I found `Sponsoring Registrar:ERNET India (R9-AFIN)`, which inturn looks after the NKN network.
Therefore, to cross verify I went up on looking on internet where I came up to a [website](https://bgp.he.net/dns/students.iitmandi.ac.in) that shows DNS and IP info. Hence, I verified the same from the IP info on the given link.

****

3.	Duckduckgo doesn't own any servers of its own. All of them are hosted on AWS(Amazon Web Services).
I did `dig duckduckgo.com` and it showed me the following hosts:

		;; ANSWER SECTION:
		duckduckgo.com.		57	IN	A	176.34.155.20

		duckduckgo.com.		57	IN	A	54.229.105.92

		duckduckgo.com.		57	IN	A	54.229.105.203

		duckduckgo.com.		57	IN	A	176.34.131.233

		duckduckgo.com.		57	IN	A	46.51.197.89

		duckduckgo.com.		57	IN	A	176.34.135.167

	I ran `whois` on each one of the above IPs and got to know the geographical locations and hosting information as:

| IP Address 		|		Geographical locations 		|		IP Address Owner 							|
|-------------------|:---------------------------------:|:-------------------------------------------------:|
| 176.34.155.20		|	Dublin, Ireland					|	Amazon Data Services Ireland (Cloudfront DUB3)	|
| 54.229.105.92		|	Seattle, Washington, USA		|	Amazon.com, Inc.								|
| 54.229.105.203	|	Seattle, Washington, USA		|	Amazon Technologies Inc.						|
| 176.34.131.233	|	Dublin, Ireland					|	Amazon Data Services Ireland (CloudFront DUB6)	|
| 46.51.197.89		|	Seattle, Washington, USA		|	Amazon Web Services, Elastic Compute Cloud, EC2	(originates from a dynamic hosting env)		|

Also,I got to know from an [interview](http://highscalability.com/blog/2013/1/28/duckduckgo-architecture-1-million-deep-searches-a-day-and-gr.html) of DDG's founder Gabriel Weinberg that the datacenters are located in California, Virginia, Singapore, Ireland but since we saw above that all of them are hosted in USA or Ireland, the datacenters mentioned in the post might have been used back in 2012 and have been discontinued now.
I also confirmed my claim using [this link](http://www.viewdns.info/iphistory/?domain=duckduckgo.com) which shows the complete IP history for the domain.

****

[End of Report]

&copy; Sahil Yadav.
All Rights Reserved.
