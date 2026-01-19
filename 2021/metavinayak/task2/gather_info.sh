domain=$1 # Bash argument 1
domain_ips=$(dig $domain +short) # Obtain ip address(es) from domain
# same domain can have multiple ip
# Of form 'dig <domain-url> +short'
# Domain is what's after "@" in an email address, or after "www." in a web address
# eg: google.com,gmail.com,students.iitmandi.ac.in,etc

lower_p=$2  # Bash argument 2
upper_p=$3  # Bash argument 3


date=$(date)
file_name="email_msg $date" # For unique file names with timestamps

dns_info=$(dig $domain ANY +noall +answer)
traceroute_info=$(traceroute $domain)

echo -e "\nGenerated from '$file_name.txt'\nDNS info:\n$dns_info\nTraceroute info:\n$traceroute_info" > "$file_name.txt" # intializing as blank file

IFS=$'\n'   # separator of ip(s)
# Looping in case there are multiple ip for same domain(eg:yahoo.in)
for ip in $domain_ips
do
    nmap_info=$(sudo nmap -p --open $lower_p-$upper_p $ip) # Scan for all the 'open' ports on the ip address in the provided range
    #Scan a range of ports 	nmap -p 1-100 192.168.1.1
    # use just 'nmap_info=$(sudo nmap $ip)' to scan the most common 1,000 ports(Saves time)

    ip_info=$(curl https://ipinfo.io/$ip)

    whois_info=$(whois $ip | grep -vE "^#|^Comment:")
    # grep:
    # -v inverts the output for regex,printing what lines where RegEx is NOT present
    # -E is used to simulate OR(|) operator in the grep regex.
    # "^#|^Comment:" is a Regular Expression to select those statements
    # where line begins with '#' or 'Comments:' (removes irrelevant data in whois lookup)

    echo -e "Domain : $domain\nIP address=$ip\n\n$nmap_info\n$ip_info\n$whois_info\n\n" >> "$file_name.txt"
    
done

python mail.py "$file_name.txt"
# rm "$file_name.txt" # un-comment this line to delete the records once mailed to user

