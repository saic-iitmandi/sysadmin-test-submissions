#! usr/bin/bash

if [ -f .env ]
then
    export $(cat .env | xargs)
else
    echo ".env file does not exist"
fi

ssid=$(iwgetid)
ssid=${ssid#*'"'}
ssid=${ssid%'"'*}
ssid=$(echo $ssid | sed 's/ //g')

# gsettings list-recursively org.gnome.system.proxy
if [ $ssid == $proxy_ssid ];
then 
    gsettings set org.gnome.system.proxy mode 'manual'
    gsettings set org.gnome.system.proxy.ftp host $proxy
    gsettings set org.gnome.system.proxy.ftp port $port
    gsettings set org.gnome.system.proxy.http host $proxy
    gsettings set org.gnome.system.proxy.http port $port
    gsettings set org.gnome.system.proxy.https host $proxy
    gsettings set org.gnome.system.proxy.https port $port
    gsettings set org.gnome.system.proxy.socks host $proxy
    gsettings set org.gnome.system.proxy.socks port $port

    $browser_name --new-window https://stgw.iitmandi.ac.in
    sleep 1
    windowId=$(xdotool search "IIT Mandi")
    for i in {1..5}
    do
        sleep 0.1
        xdotool search --name "IIT Mandi" key Tab
    done
    xdotool search --name "IIT Mandi" type $gateway_username
    sleep 0.2
    xdotool search --name "IIT Mandi" key Tab
    sleep 0.2
    xdotool search --name "IIT Mandi" type $gateway_password
    sleep 0.2
    xdotool search --name "IIT Mandi" key Tab
    sleep 0.2
    xdotool search --name "IIT Mandi" key Return
    sleep 0.3
    xdotool key ctrl+w
else
    gsettings set org.gnome.system.proxy mode 'none'
    gsettings set org.gnome.system.proxy.ftp host ''
    gsettings set org.gnome.system.proxy.ftp port 0
    gsettings set org.gnome.system.proxy.http host ''
    gsettings set org.gnome.system.proxy.http port 0
    gsettings set org.gnome.system.proxy.https host ''
    gsettings set org.gnome.system.proxy.https port 0
    gsettings set org.gnome.system.proxy.socks host ''
    gsettings set org.gnome.system.proxy.socks port 0
fi

echo $sudo_password | sudo -S ./script.py
