sudo systemctl start cron

read -p "Enter the domain to scan(eg: google.com): " domain

echo -e "Enter the range of ports to scan(from 1 to 65535):"
read -p "Enter lower port limit: " lower_p
read -p "Enter upper port limit: " upper_p

# Write out current crontab
crontab -l > mycron

directory=$(pwd)    # Gives the directory where the script is located

# Sets up a Cron Job that executes everyday at 12pm and runs the desired scripts with proper arguments.
echo "0 12 * * * cd $directory; ./gather_info.sh $domain $lower_p $upper_p" >> mycron
#install new cron file
crontab mycron
# Cron job can be removed by commenting the line '* * ...' at end as '# * * ...' after using command 'crontab -e'

# delete the bash variable for cron job
rm mycron