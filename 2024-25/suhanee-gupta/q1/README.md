## CHALLENGE 1-vm

I succesfully imported virtual machine and started machine.
logged in as guest and attempted to view user saic or work as root, but obviously failed.
then i tried some simple exploits like -
- booted machine, attemping to open grub (grub opens as root privelage), but failed.
- started parsing through /etc/ to cat out shadow (permission denied) and passwd(nothing useful).
- tried an SUID exploit, and used gtfobins to attemt to get root access but was unsuccessful
# <img align="center"  src="/2024-25/suhanee-gupta/q1/find.png" width=500><br><br> 
- since cron jobs run with root privelages, i first listed out the present cronjobs. there were 4 cronjobs, that would run all executables in certain directories. 
# <img align="center"  src="/2024-25/suhanee-gupta/q1/cronjob.png" width=500><br><br> 
now i just had to find a directory i can write in. unfortunately i could not create a file in any of these directories.
Now, this is Ubuntu 12.04.4 lts, so I started doing older exploits
- started with a polkit exploit i found, which invovded killing a dbus command while it was running, which would allow us to create a new user with sudo privelages
# <img align="center"  src="/2024-25/suhanee-gupta/q1/dbus.png" width=500><br><br> 
even after multiple attempts i couldnt create the user.
ultimately we got the hint to use SQL injection, which means that there was a site being hosted. ```ss -tulnp``` returned 3 ports: 3306(means SQL database is running), 80(so a web server is being hosted) and 53. So i can access the site being hosted, perform SQL injected and get into the running database.
i went into the /var/www/ and found a README.md file. There were files for a notes app made in php.
# <img align="center"  src="/2024-25/suhanee-gupta/q1/seed.png" width=500><br><br> 
So i figured out the ip address (192.168.187.48) and opened up the site. it wanted a login, which was somewhere i could carry out the sql injection. after parsing through the code for login page (login.php -> login-page.js -> api/user/login.php) and searching through other files as well, i couldnt find the sql query.
i went to check the network traffic which led me back to login.php. i kept going in circles.