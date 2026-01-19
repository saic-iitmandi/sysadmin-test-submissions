flag :- SAIC{C0ngr4ts_d0_y0u_l0v3_ST4C?}


in this challenge, i was given a virtual machine acting as a server. my goal was to analyze the system, understand how it was structured, find security weaknesses, and attempt to gain root access.

i did not have strong prior knowledge of cybersecurity or system exploitation, so my approach focused on understanding the system .
i used VirtualBox to run machine as remote server
i logged in and then opened terminal , checked my current status and what machine i was running (whoami , uname -a)

i found out that i was running kernel 4.4 (Linux 4.4.0-148-generic to be precise)
i also learned that this kernel version is quite old, which usually means security vulnerabilities may exist.( which might be known and exist on internet )

when i checked what services were running and found out something interesting.
Port 80 was public and port 5000 and 9000 was internal services (both were local only)

i checked the server at port 80 and found out that it was using nginx 
So most probably the server was not directly hosting files , there was this gatekeeper system .(its called reverse proxy)
When I opened http://localhost, i only saw Helios Internal Dashboard . so i thought this website thing is something else and the message was exposed by nginx ( apparently i was wrong)
i checked nginx configuration (cat /etc/nginx/sites-enabled/*) 

 The exact thing i saw :-
 server {
    listen 80;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header X-Forwarded-For $http_x_forwarded_for;
    }
 }

All traffic from port 80 is forwarded to port 5000.
The X-Forwarded-For header is passed directly from the client. this means nginx trusts user-controlled data. 
this kind of trust could cause security problems if the backend had something that header.

so i accessed the backend directly (Server: BaseHTTP/0.3 Python/2.7.6)
and i got this :- Server: BaseHTTP/0.3 Python/2.7.6
The backend was written in Python 2.7 (2.7 seriously , outdated , python 2 support ended in like 2020 or something)

i did check port 9000 (curl -i http://127.0.0.1:9000)
but 'get' doesnt work on it so its probably something related to management or internal control

From all my observations, I understood the system structure as :- user :- nginx (80):- python backend (5000) :- internal service (9000) :- linux kernel

Now that I had a mental map of the system, I decided to test my theory about the Nginx X-Forwarded-For header. If the backend was blindly trusting this input, I could potentially inject system commands.

I tried to verify this by injecting a basic command: curl -H "X-Forwarded-For: 127.0.0.1; whoami" http://127.0.0.1:80

The server responded with the dashboard page, but it did not show me the output of whoami. This meant one of two things: either the injection failed, or it was "blind" (the command ran, but the output went to a log file somewhere I couldn't see). Debugging a blind web exploit is painful and slow. I realized I was shooting in the dark.

The Pivot to OS Exploitation I decided to stop fighting the web server and go back to my first observation: Kernel 4.4.0. I knew the OS was old, so I looked for "SUID binaries"—programs that legitimate users can run with root permissions.

I ran: find / -perm -u=s -type f 2>/dev/null

Most of the list was standard stuff (ping, mount, su), but one binary stood out: /usr/bin/pkexec. A quick check confirmed my suspicion: An outdated kernel combined with pkexec is the perfect recipe for CVE-2021-4034, also known as PwnKit. This vulnerability allows any unprivileged user to gain instant root access by manipulating the environment variables.

The Exploitation (and the mistake I made) I found a C exploit for PwnKit and decided to compile it on the machine. I wrote the code into pwnkit.c and ran: gcc pwnkit.c -o pwnkit

When I ran it, it crashed with an error: mkdir: cannot create directory ‘pwnkit’: File exists. I realized I had made a silly mistake. I named my executable file pwnkit, but the exploit code also tries to create a folder named pwnkit. In Linux, you can't have a file and a folder with the same name in the same place. I had basically blocked my own exploit.

The Fix and The Root Shell I deleted the failed files, recompiled the code, but this time I named the output exploit to avoid the conflict. ./exploit

It ran instantly. My command prompt changed to a #. I was root.

The Final Hurdle I typed whoami to celebrate, but the system hit me with: whoami: command not found. For a second, I thought I broke it. Then I realized that PwnKit works by wiping the system's "PATH" (the map that tells the shell where to find programs). I was root, but my shell was blind.

I had to use the full address for everything. Instead of cat flag.txt, I ran /bin/cat /root/flag.txt