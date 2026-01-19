1)adding '127.0.0.1       saic.com' to /etc/hosts
vs
2) creating a dns domain pointing to an ip address and using that ip in docker???


https://forums.docker.com/t/docker-with-dns-redirection/68516/2


https://www.baeldung.com/linux/mapping-hostnames-ports  

In Linux, /etc/hosts is a file used by the operating system to translate hostnames to IP-addresses. It is also called the ‘hosts’ file. By adding lines to this file, we can map arbitrary hostnames to arbitrary IP-addresses, which then we can use for testing websites locally.


1) seems better


search 'Map the ports for the container such that both the sites are up and running on 127.0.0.1(localhost) of your host OS's browser using the mapped ports.'