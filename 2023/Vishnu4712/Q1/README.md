So first of all we were given the saic.ova file which was the link for the VM. I installed the VM from oracle VM virtualbox. After the installation, it was asking for the password so I tried basic passwords like root, saic but was unsuccessful in gaining access. Then I used the command

nmap 192.168.0.0/24

To do a network scanning to find out all the devices that are connected to my network, with which I found the IP address of the VM. I also found more about that IP address by running the command

nmap -sV 192.168.0.102 

192.168.0.102 being the IP address of the VM.
From this I came to know that there is an Apache web server (version 2.2.22)  running on port 80.

 Then I went to the website which was about the fox character Xenia also known as linuxfox. Now my task was to get into the server by exploiting any vulnerability that I find. 

So for exploiting website I used kali linux VM. So I used nikto, gobuster and skipfish tools.
Commands Used:

nikto -h 192.168.0.102

gobuster dir -u http://192.168.0.102/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

skipfish -o skip 192.168.0.102

From these tools I found several things:
1) Many hidden directories (/index, /secure, /nothing, /tmp etc..)
2) Directory indexing was found in directories /secure, /uploads etc.
3) /#wp-config.php# file found 

So I started going to all the hidden directories and in most of them I was not able to find anything useful but when I went to /secure it had 2 links, one was the parent directory and the other one was a backup.zip file. So I clicked on that and it downloaded a zip file which was encrypted. So i used johntheripper tool to crack it and I was successful in it. I found out that the password for the zip file was freedom.

Commands Used:

zip2john backup.zip > backup.txt

john backup.txt

The zip file contained an .mp3 file which I opened but it was giving me some error “Missing codecs. Install suitable plugins”.
So I used VLC to open that file but still I was unable to open. The file was corrupted so I googled online .mp3 repair files and tried but was unsuccessful. Then I used audacity which is a popular audio editing and recording tool. I tried to open that file and luckily it did, but did not find anything useful.