Installed Streisand on pc(it took ~23 mins), running it on Digital Ocean droplet.
The droplet is running on bangalore datacenter, tried using NY datacenter it didnt work.
Gave the following error on NY (An exception occurred during task execution. To see the full traceback, use -vvv. The error was: DoError: Region is not available
fatal: [localhost]: FAILED! => {"changed": false, "msg": "Region is not available"})

file:///home/singh/streisand/generated-docs/streisand-1.html is showing step-by-step instructions for the services it provides.

Connected to my Streisand Gateway with SSL

Used OpenVPN(direct)
Used Linux(ubuntu) way of configuring OpenVPN
  In step 17 "Server Certificate Check" option was not there in the TLS Authentication tab.
  "Go to the TLS Authentication tab
      Under Server Certificate Check choose verify name exactly and enter stable-unfair-exclude as its value."
 Followed the 20 step instructions and my IP changed from 49.35.**.** to 139.59.56.186 .
 
 Now I have a option streisand-1 VPN in the ubuntu's network setting which can change my IP.
 
 
 
 Resoures-
 1. https://github.com/StreisandEffect/streisand
 2. http://devops.host/blog/streisand-vpn.html#getting-an-aws-account
 

