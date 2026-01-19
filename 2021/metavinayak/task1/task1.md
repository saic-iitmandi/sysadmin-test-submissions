First used Internal
Using NAT in network adapter
(why NAT?: https://www.virtualbox.org/manual/ch06.html)

command : "sudo lsof -i -P -n | grep LISTEN"

1st:
http://127.0.0.1:5678/

1 cookie

2nd:
http://127.0.0.1:5679/

crbug in console

----------------------------------------------------------------------------------

5678/tcp open  rrac

5679/tcp open  activesync

https://www.speedguide.net/port.php?port=5678

----------------------------------------------------------------------------------

### using "sudo nmap -sS -A localhost"  aggressive

5678/tcp open  http       Apache httpd 2.4.18 ((Ubuntu))

|_http-server-header: Apache/2.4.18 (Ubuntu)

|_http-title: hackme

5679/tcp open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; 

protocol 2.0)

| ssh-hostkey: 

|   2048 2f:c6:2f:c4:6d:a6:f5:5b:c2:1b:f9:17:1f:9a:09:89 (RSA)

|   256 5e:91:1b:6b:f1:d8:81:de:8b:2c:f3:70:61:ea:6f:29 (ECDSA)

|_  256 f1:98:21:91:c8:ee:4d:a2:83:14:64:96:37:5b:44:3d (ED25519)

Device type: general purpose

Running: Linux 2.6.X

OS CPE: cpe:/o:linux:linux_kernel:2.6.32

OS details: Linux 2.6.32

Network Distance: 0 hops

Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------

## On searching:

'ssh OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0) | ssh-hostkey'

https://www.exploit-db.com/exploits/40136

https://blog.raw.pm/en/TryHackMe-Simple-CTF-write-up/

----------------------------------------------------------------------------------

## Checking hidden directories on open ports using dirbuster,gobuster

### gobuster -e -u localhost -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 

used dirbuster instead of gobuster,gui :)

## Found two directories: `sites/ and icons/`,nothing very useful

"sudo nmap -v -sV -p- -oA devops_full 127.0.0.1"

5678/tcp  open  http       Apache httpd 2.4.18 ((Ubuntu))
5679/tcp  open  ssh        OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)


https://charlesreid1.com/wiki/Metasploitable/SSH/Exploits


~~NO time for trying exploits :')~~


## Learning outcomes :

Leant about the host-guess os and remote server networking configurations.

Learnt about open port checking and the kind of services active on those ports.Using agressive nmap commands and various flags for nmap using the `man pages` and google.

Learnt how to find unknown directories just from the ip address of the web server using `dirbuster` and `gobuster`.

Learnt about ssh working.

Read slightly about the kind of exploits that old software and firmware can have and the why to keep them updated.Like the `OpenSSH 7.2p2 - Username Enumeration` vulnerability



