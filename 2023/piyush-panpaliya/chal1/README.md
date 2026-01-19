## Challenge 1 - Gain Access to a Remote Server

was expecting to gain root privilege and then there should be something in `/root` folder like flag.txt so started by downloading and booting into the vm with virtualbox and now I logged in as guest user.

ran `ss -tunl` to know all open ports and found a http server on port 80, a mysql server at 3306 and a CUPS server at 631.

now opened the website in the vm itslef it was about xenia and now I wanted to open it on my host so went on localhost and it didnt worked, checked the network adapter was bridge and thought this should work. so just used firefox inside the vm and had a glance at the website and `localhost/robots.txt` and found some paths but none were suspicious except `/nothing` but didnt found anything useful.

Now I wanted to look at it on host for better dev tools, so as a jugaad used nat adapter with port forwarding and checked for cookies, localstorage and headers but stoped looking on website.

Shifted my focus on CUPS since it was old, ran a searchsploit on cups and found remote code execution which was very ccomplex but kept on looking then found that we can change the location of err file and thought of changing it to `.bash_history` or even `root/flag.txt` and then read it via web dashboard of cups but idk why but changing the err file required root privilege so it didnt worked and then gave up on it.

then after meet call in morning understood that bridge actually assigns a different IP to vm as well so did `ip addr` and now used that IP and it worked.

again went on `VM_IP/robots.txt` to see all the possible routes and tried each this time also inspecting it, and surprisingly `/nothing` had `#my secret pass` as

```
xenia
tux
freedom
password
diana
helloworld!
iloveroot
```

commented in html. tried using this as logging in into root with su root but it didn't worked. so saw all the available user by `cat /etc/passwd` and tried for every user even tried encoding the pass with base64 and used that but it didnt worked.

no ssh or ftp ports opened so cant explore that but tried logging in sql with the password but it didnt worked.

Next day,tried opening the website and it didnt worked, no idea how so thought the ip changed, so did `ip addr` and no ip was showing so restarted for few time and that too didnt worked so just used nat with port forwarding from 8069:80 and sarted checking out dirs in vm since I found nothing on website other than /nothing and after some exploring, found `/var/www` and the website was there and thus dicovering two new routes `secure` and `SecreTSMSgatwayLogin` which was a login page for an app playsms.

opened secure and found a zip which was password protected but the password from `/nothing` didnt worked so tried using single words and boom `freedom` worked, opened the .mp3 in notepad since it didnt had any audio in it and it had a username and password and the login page I found earlier.

now opened the login page and now again went to `/var/www/SecreTSMSgatwayLogin` and in `config.php` found the password for mysql it was `hello@mysql` and DB name was playsms. In the user table `playcms_tblUser` found admin and a password which didnt worked on the login page, and the id found in mp3 also didnt worked with the password, I think because the password stored are hashed, so tried freedom but it didnt worked so again started trying all the passwords from `/nothing` and `diana` worked.

now it was time to search vuln of playSMS, so did a searchsploit on playsms and found `https://www.exploit-db.com/exploits/42044` and now its time for some remote code execution.

```csv
Name,Mobile,Email,Group,code,Tags
<?php $t=$_SERVER['HTTP_USER_AGENT']; system($t); ?>,11,ok@ok.ok,1,1
```

this csv can be uploaded on phonebook import and when I send the request it will execute the command present in the user agent, so searched on how to change user agent on firefox and found that in `about:config` we can change it in `general.useragent.override`, so changed it to `ls` and sent the request and got the list of files in the directory.

now the user was www-data by `whoami` and now I wanted root access so saw what commands can www-data run without password a classic SUID exploit by doing `sudo -l` and found perl can be used. so changed the user agent to `sudo /usr/bin/perl -pe '' /root/flag.txt` and GOT the flag.

**Well done, Neo!**
