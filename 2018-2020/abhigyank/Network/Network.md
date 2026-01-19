# Networking 

## Solutions

### Problem 1
#### Problem Statement-
We need maximum information of all the PCs in the `iitmandi.ac.in` network, i.e. `14.139.34.0/24` which are exposed to the internet. You need to find out all the PCs which are public facing and all their ports open and what kind of operating system they are running on. Any other information would be a bonus.

#### Solution

IP - `14.139.34.0` : Not exposed to the internet. `179/tcp`, `646/tcp` are closed, others are filtered.<br>
IP - `14.139.34.1` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.2` : This is the IITMandi, internet gateway, that we use at 10.8.0.1. Open ports: 22, 53, 80, 3000, 5001, 7001, 10000. OS Details: Linux 2.6.28<br>
IP - `14.139.34.3` : Open Ports: 25, 53, 80, 110, 143, 443, 465, 993, 995, 10000. OS details: Linux 3.11 - 4.1<br>
IP - `14.139.34.4` : Open Ports: 22, 25, 80, 6001, 8080. OS guess: Linux 3.11 - 4.1<br>
IP - `14.139.34.5` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.6` : IIT Mandi faculty website. Open Ports: 80, 139, 443. OS details: Linux 3.2 - 3.8<br>
IP - `14.139.34.7` : IIT Alumni mail. Open Ports: 22, 25, 53, 80, 110, 143, 587, 993, 995, 10000, 20000. OS guess: Linux 3.2 - 3.8<br>
IP - `14.139.34.8` : Open Ports: 80, 389, 443. OS details: Linux 3.2 - 3.8<br>
IP - `14.139.34.9` : Project staff webmail. Open Ports: 25, 80, 110, 143, 389, 443, 465, 993, 10000. OS details: Linux 3.11 - 4.1<br>
IP - `14.139.34.10` : Open Ports: 21, 80, 443, 8000, 8082. OS details: Linux 3.11 - 4.1<br>
IP - `14.139.34.11` : SNTC server. Open Ports: 22, 53, 80, 8080. OS details: Linux 3.11 - 4.1 (Ubuntu 16.04)<br>
IP - `14.139.34.12` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.13` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.14` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.15` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.16` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.17` : Open Ports: 22, 80, 5800, 5900. OS guess: Linux 3.2 - 3.8 <br>
IP - `14.139.34.18` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.19` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.20` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.21` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.22` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.23` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.24` : Old OAS IIT Mandi. Open Ports: 80, 135, 139, 1023, 1433, 1801, 2103, 2105, 2107, 2383, 3001, 3306, 3389, 3690, 8080, 8085, 8086. OS guess: Microsoft Windows Server 2012<br>
IP - `14.139.34.25` : Not exposed to the internet. All ports are filtered as per `nmap`.<br>
IP - `14.139.34.26` : OAS IIT Mandi. Open Ports: 80, 135, 139, 1023, 1433, 1801, 2103, 2105, 2107, 2383, 3389, 49152-49159. OS Guess: Microsoft Windows Server 2012 (96%) / Microsoft Windows Server 2008 or 2008 Beta 3 (92%) 
<br>
The above are the details of all the PCs in the `iitmandi.ac.in` network, with open ports and OS.
These can be found by using [`nmap`](https://nmap.org/), an open source utility for network discovery and security auditing. `nmap` can be used to make requests to the web servers and find all the open ports, along with the operating system running on them using a `-O` flag in the command line.
This problem statement really made me explore internet protocols, network testing, tools for network exploitation. The learning about ports for a webserver was immense, which I felt is very important for network admins. 

### Problem 2
#### Problem Statement-
For `students.iitmandi.ac.in`, you need to find out from what company the domain has been bought. For instance, I bought `sahilarora535.me` domain name from Namecheap.me. You need to find out from where did the institute buy the domain `students.iitmandi.ac.in.`

#### Solution
`students.iitmandi.ac.in.` is a subdomain of `iitmandi.ac.in`, which is an `.ac.in` domain type. In India, [ERNET India](https://www.registry.ernet.in) is the exclusive registrar for this domain. Hence, the institute bought the domain from [ERNET India](https://www.registry.ernet.in).
This can be verified from `whois lookups` as well. [DomainTools](http://whois.domaintools.com/iitmandi.ac.in) `whois lookup` revealed the same, along with further details of `nameservers` and server IP. 
`Dns records` of all types can also be viewed [here](https://who.is/dns/students.iitmandi.ac.in). It is hosted on a `Apache/2.4.18 (Ubuntu)` server.

### Problem 3
#### Problem Statement-
Most of the search engines have their own data-centres, for instance Google's data centres can be found [here](https://www.google.com/about/datacenters/inside/locations/index.html). You need to find out how many data centres does DuckDuckGo OWN, and what are their locations.

#### Solution
Duckduckgo used to run their own servers (in their founders basement, Awesome isn't it?) but now run servers on [Amazon EC2](https://duck.co/redir/?u=http%3A%2F%2Faws.amazon.com%2Fec2%2F) across the world. They are running in 4 AWS datacenters in California, Virginia, Singapore, Ireland. They also use Linode to host some community functionality, like translations. So technically, they don't OWN any datacenter.
Details about their architecture can be found [here](https://duck.co/help/company/architecture), it also has a [link](http://highscalability.com/blog/2013/1/28/duckduckgo-architecture-1-million-deep-searches-a-day-and-gr.html) to an aricle of an interview with Gabriel(DDG's founder), which has details of the AWS servers and their location. 
This is an interesting task, to learn about datacenters and how search engine handle the traffic and large amount of data at the same time keeping up a tremenduos speed. 

