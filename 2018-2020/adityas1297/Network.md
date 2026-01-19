Task 1 - 
Learned about nmap, furthur investigaton required.
Edit 1- 
   1.  nmap 14.139.34.0/24
      Output-
        Starting Nmap 7.01 ( https://nmap.org ) at 2018-02-01 19:49 IST
        Warning: 14.139.34.10 giving up on port because retransmission cap hit (10).
      The command ran for some time but sort of timed-out without giving any results.
   2. nmap -F 14.139.34.0/24
        "-F (Fast (limited port) scan) .
             Specifies that you wish to scan fewer ports than the default.
             Normally Nmap scans the most common 1,000 ports for each scanned
             protocol. With -F, this is reduced to 100."(From the man page of nmap).
      It showed ports of 9 hosts in 14 seconds
      "Nmap done: 256 IP addresses (9 hosts up) scanned in 14.32 seconds"
    3. sudo nmap -F -O 14.139.34.0/24
          The '-O' is to find the OS on the systems.
          It showed the ports all ips in 14.139.34.0/24 and guessed their OS.OS fingerprint was not ideal in most cases due       to various resoans.It took around 10 mins.
          "Nmap done: 256 IP addresses (256 hosts up) scanned in 668.06 seconds".
          Results uploaded in file named Ports_and_OS_of_PCs.
   Edit 2-
      1. "nmap -sP 14.139.34.0/24" can be used to scan a network and find out which servers and devices are up and running.It took 6 seconds.
            The online host are-
                14.139.34.2(INTERNET GATEWAY IIT MANDI),
                mail.students.iitmandi.ac.in (14.139.34.3),
                14.139.34.4(Central Library, IIT Mandi),
                14.139.34.8,
                mail.projects.iitmandi.ac.in (14.139.34.9),
                14.139.34.10(www.research.iitmandi.ac.in),
                14.139.34.11(SNTC server),
                14.139.34.26(OAS),
                14.139.34.43(DSpace JSPUI).
                Nmap done: 256 IP addresses (9 hosts up) scanned in 6.76 seconds.
                
        2. When I used sudo nmap -F -O 14.139.34.0/24 to find the OS of all online machines it scanned all 256 IP addresses, but most of them where either filtered ports (maybe protected by a firewall) or closed port.So to get the OS of online devics took alot of time(over 11 mins).So I found it more efficent to find the online hosts using -sP and then using "sudo nmap -O -F -sSU IP" for individual IPs.Each took around 10 secs,and there was no significant loss of information while using "-F" option and it saved a lot of time.

         
              >>>>>>  Their ports,OS and other infomation in the file "ports_and_os_final" . >>>>>>>
                
                Conclusion so far-
                 1. Nmap is a great tool to find information about ports and OS of devices connected to a network.
                 2. nmap -sP 14.139.34.0/24 was the fastest way I could find to find online hosts(6.76 seconds).
                 3. nmap -F 14.139.34.0/24 was the fastest way I could find to find ports used by online hosts(14.32 seconds).
                 4. "sudo nmap -O -F -sSU IP" was the fastest way I could find to find operating system of a IP(~15seconds).
                 
                 
     
          
          Will keep diging...
          What I learned so far -
            1. About nmap.
            2. About ports,different porrts are used for different things.
            
          
          Resources-
             1. https://askubuntu.com/questions/377787/how-to-scan-an-entire-network-using-nmap
             2. https://unix.stackexchange.com/questions/178424/nmap-sn-lists-all-active-hosts-on-my-network-but-nmap-sl-does-not
             3. https://nmap.org/book/man-os-detection.html
             4. https://nmap.org/
      
   



Task 2 - It was bought on http://www.ernet.in
  
  How did I find it-
  Used WHOIS to find about the website.  
  
  Resources - 
  http://whois.domaintools.com/iitmandi.ac.in - Gave information about IP, DNS, Domain Registrar etc.
  http://www.ernet.in/domain.html - Confirmed that ERNET India has been appointed as an exclusive domain registrar of domains like ac.in.
  https://www.quora.com/How-do-I-find-the-ownership-history-of-a-domain-without-paying-a-fee
  https://www.sslshopper.com/ssl-checker.html#hostname=https://students.iitmandi.ac.in/
  
  What I learned-
  1. WHOIS can be use to get information about websites.
  2. About Domain registars
  3. SSL Client Certificate to student.iitmandi.ac.in was given by GoDaddy.com, Inc.(and it expires in DEC-19 :P)
  

Task 3 - DuckDuckGo owns ZERO data-centres, it runs on 4 AWS datacenters (California, Virginia, Singapore, Ireland).
  Resources -
  http://highscalability.com/blog/2013/1/28/duckduckgo-architecture-1-million-deep-searches-a-day-and-gr.html
  https://duck.co/help/company/architecture 

