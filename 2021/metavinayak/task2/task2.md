## Instructions to run the script :

First edit the mail.py and change the **sender_email,receiver_email,password and smtp_server** variables as per your need.

Then turn ON  "Less secure app access" for your account.This is required for mail to be sent

Run the 'script.sh' file inside 'task2' directory as follows:

When inside the 'SAIC-test-2021' directory,just run

``` bash
cd task2
chmod +x ./script.sh
./script.sh
```
-------------------------------------------------------------------------------

### There are 3 scripts : script.sh,gather_info.sh,mail.py
#### The bash scripts have been commented properly for each code snippet

'mail.py' is used to mail the gathered ip info to user

All the information regarding ip/domain is gathered in gather_info.sh

Details of gather_info.sh (Explanation comments in scripts itself) : 

All commands found using google search :),Reference links at end

`dig google.com +short` (gives only the ip adresses for the domain)

`dig $domain ANY +noall +answer` (gives the DNS info for the domain)

`traceroute $domain` (Traceroute is used to track the pathway taken by a packet on an IP network from source to destination in real-time)

`nslookup google.com`  (gives ip and address info of server)

Nmap gives the PORT,STATE and SERVICE active on the ip address

`sudo nmap -p- --open <ip>`

'-p-' to scan for all 65535 ports,takes very long time(do at last).

`sudo nmap -p --open $lower_p-$upper_p $ip`

Scans all open ports in the specified range

`curl https://ipinfo.io/<ip>` (gives detailed location,hostname,timezone,etc for web server)


`whois <ip>`

whois lokup gives a lot of registered info regarding the ip address organization and the details of the domain name owner

### References:

From `man pages` documentation of various commands.

https://www.tutorialspoint.com/how-to-find-linux-server-geographic-location-in-terminal

https://www.2daygeek.com/check-find-dns-records-of-domain-in-linux-terminal/


## Send email (make periodic)
https://realpython.com/python-send-email/


## For script.sh :

https://unix.stackexchange.com/questions/275794/iterating-over-multiple-line-string-stored-in-variable


**Making cron jobs to run script periodically**

https://stackoverflow.com/questions/878600/how-to-create-a-cron-job-using-bash-automatically-without-the-interactive-editor

Using bash arguments for user friendly inputs:

https://stackoverflow.com/questions/13869879/storing-passed-arguments-in-separate-variables-shell-scripting/36558556


## Learning outcomes :

Learnt to gather lots of information about a domain/ip like finding all ip addresses of a domain,it's open ports,the DNS routes the data takes,all the whois info,etc

Learnt mail automation using Python and Bash combined.

Learnt Bash scripting(taking user input,creating cron jobs,invking scripts from main script,passing arguments)

Learnt RegEx use through grep.