# Network.md Problemset

1. PCs and Ports
   Utility Used: NMap

  - 14.139.34.2 OS: Linux
  PORT      STATE    SERVICE      VERSION
  22/tcp    open     ssh          OpenSSH 6.6p1 Ubuntu 2ubuntu1 (Ubuntu Linux; protocol 2.0)
  53/tcp    open     domain
  80/tcp    open     http         Apache httpd 2.4.7 ((Ubuntu))
  443/tcp   open     ssl/http     Apache httpd 2.4.7 ((Ubuntu))
  3000/tcp  open     ntop-http    Ntop web interface 5.0.1
  5001/tcp  open     ssh          OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
  7001/tcp  open     ssh          OpenSSH 6.0p1 Debian 4+deb7u2 (protocol 2.0)
  10000/tcp open     http         MiniServ 1.690 (Webmin httpd)


  - 14.139.34.3 OS: Linux
  PORT      STATE  SERVICE    VERSION
  53/tcp    open   domain     ISC BIND 9.10.3-P4-Ubuntu
  80/tcp    open   http       Apache httpd 2.4.18 ((Ubuntu))
  110/tcp   open   pop3       Dovecot pop3d
  143/tcp   open   imap       Dovecot imapd
  443/tcp   open   ssl/http   Apache httpd 2.4.18 ((Ubuntu))
  465/tcp   open   ssl/smtp   Postfix smtpd
  993/tcp   open   ssl/imap   Dovecot imapd
  995/tcp   open   ssl/pop3   Dovecot pop3d
  10000/tcp open   http       MiniServ 1.850 (Webmin httpd)


  - 14.139.34.4 OS: Linux
  PORT     STATE    SERVICE      VERSION
  22/tcp   open     ssh          OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.6 (Ubuntu Linux; protocol 2.0)
  80/tcp   open     http         Apache httpd 2.4.7 ((Ubuntu))
  6001/tcp open     X11:1?
  8080/tcp open     http         Apache httpd 2.4.7 ((Ubuntu))

  - 14.139.34.8
  PORT      STATE  SERVICE  VERSION
  80/tcp    open   http     Apache httpd 2.2.22 ((Debian))
  389/tcp   open   ldap     OpenLDAP 2.2.X - 2.3.X
  443/tcp   open   ssl/http Apache httpd 2.2.22 ((Debian))
  10000/tcp open   http     MiniServ 1.850 (Webmin httpd)

  - 14.139.34.9 OS: Linux
  PORT      STATE  SERVICE    VERSION
  80/tcp    open   http       Apache httpd 2.4.18 ((Ubuntu))
  110/tcp   open   pop3       Dovecot pop3d
  143/tcp   open   imap       Dovecot imapd
  443/tcp   open   ssl/http   Apache httpd 2.4.18 ((Ubuntu))
  465/tcp   open   ssl/smtp   Postfix smtpd
  993/tcp   open   ssl/imap   Dovecot imapd
  10000/tcp open   http       MiniServ 1.820 (Webmin httpd)

  - 14.139.34.10 OS: Unix
  PORT     STATE    SERVICE      VERSION
  21/tcp   open     ftp          vsftpd 3.0.3
  22/tcp   open     tcpwrapped
  80/tcp   open     http         Apache httpd 2.4.18 ((Ubuntu))
  443/tcp  open     ssl/http     Apache httpd 2.4.18 ((Ubuntu))
  8000/tcp open     http         Gunicorn 19.4.5
  8082/tcp open     http         Octoshape P2P streaming web service

  - 14.139.34.11 OS: Linux
  PORT     STATE    SERVICE      VERSION
  22/tcp   open     ssh          OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
  53/tcp   open     domain       ISC BIND 9.10.3-P4-Ubuntu
  80/tcp   open     http         nginx 1.10.3 (Ubuntu)
  8080/tcp open     http         Apache httpd 2.4.10 ((Debian))

  - 14.139.34.26 OS: Windows
  PORT      STATE    SERVICE       VERSION
  80/tcp    open     http          Microsoft IIS httpd 8.5
  135/tcp   open     msrpc         Microsoft Windows RPC
  1023/tcp  open     remoting      MS .NET Remoting services
  1433/tcp  open     ms-sql-s      Microsoft SQL Server 2014 12.00.5000; SP2
  1801/tcp  open     msmq?
  2103/tcp  open     msrpc         Microsoft Windows RPC
  2105/tcp  open     msrpc         Microsoft Windows RPC
  2107/tcp  open     msrpc         Microsoft Windows RPC
  2383/tcp  open     ms-olap4?
  3389/tcp  open     ms-wbt-server Microsoft Terminal Service
  49152/tcp open     msrpc         Microsoft Windows RPC
  49153/tcp open     msrpc         Microsoft Windows RPC
  49154/tcp open     msrpc         Microsoft Windows RPC
  49155/tcp open     msrpc         Microsoft Windows RPC
  49156/tcp open     msrpc         Microsoft Windows RPC
  49157/tcp open     msrpc         Microsoft Windows RPC
  49158/tcp open     msrpc         Microsoft Windows RPC
  49159/tcp open     msrpc         Microsoft Windows RPC

  Learnt: Different ports and using Nmap

  ------------

2. students.iitmandi.ac.in has been bought from:
   ERNET India, 5th Floor,
   Block-I, A Wing DMRC,
   IT Park, Shastri Park,
   New Delhi 110053

   Resources Utilised: whois domain name lookup
   Learnt: ERNET India provides ac.in, edu.in and res.in Internationalized Domain Names

  ------------

3. DuckDuckGo does not own any data centers.
   It utilizes Amazon AWS
