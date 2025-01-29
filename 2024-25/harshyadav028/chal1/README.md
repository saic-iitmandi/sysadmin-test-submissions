## **Challenge 1 - Gain Access to a Remote**

This challenge seems interesting to me as attacking a VM machine server seems cool. So, I begin with downloading saic.ova file and booting it up in virtual box. Then, logged in as guest user. I would also like to mention that I used bridge network for VM for easy IP Address access.

ran `ip addr` to get the IP address which I used to run `http://<VM-IP address >` in the browser.

I tried with running `nmap -A <VM-IP>` to get the all open ports. Get to know about the common vulnerabilities and methods like hydra(Attempt common username-password combinations from the wordlist we provide can be called as brute force) and gobuster( which basically check brute run all the wordlist contents with `http://<VM-IP>` to get the hidden directories may be present ) but did not use them for the challenge.

I inspect the login page to find something suspicious but did not succeed. Explored the *login.php page*, *signup.php page*. sign up obviously with fake credentials and then comes the *index.php (home) page* which seems like a note management application. Tested every feature like add note, delete note, edit, logout etc. on the page.

Next day, While inspecting in dev tools of login page found the *JavaScript URL* which provide information of server used in the web page which is *Apache/2.2.22 (Ubuntu) Server at 192.168.76.9 Port 80*. Researched on the server which tell that server is 2012 version then tried to found the vulnerabilities which are stated on internet about the Ubuntu 2012 and Apache 2012 server. Found some of these like *Apache Mod_proxy Exploit*, *Apache mod_proxy Directory Traversal* used `http://<VM-IP address/proxy >` and found a page which has unstyled login and signup pages which I tried to login or signup but failed. Read more about *Apache Mod_proxy Exploit* but get no useful information.

tried for every available user by `localhost/etc/passwd`, `localhost/etc/apache2/apache2.conf` but that did not worked.

I did *SQL ijection* on the *index.php* page in the hope to get some suspicious files from the SQL database.
Then I run,

 `localhost/var/www/html/db.php`
`localhost/var/www/html/config.php`
 `localhost/var/www/html/database.php`
 `localhost/var/www/html/db_config.php`

To get some information form database files that may be available. But, would not find any information about the flag.
Next day, I again read the last years solution and then found a /robots.txt file was suspect last year so run that in the challenge and found this file exists and has following information inside:

_User: *_

_Disallow: /admin/_

And I also found */backup file* which has: 

_#! /bin/bash_

*echo "work in progress"*

I tried to edit the backup file to extract *flag.txt* if available but denied the permission to save/replace the backup file.
I went deeper into the _/admin/_ and _/robots.txt_ things but would not find any further useful information.
I tried to allow the admin permission for *(_everyone_) from inspect but did not find any clue.

At last, I tried for some random address such as _/root/flag.txt, /secure_ but the pages are not found.