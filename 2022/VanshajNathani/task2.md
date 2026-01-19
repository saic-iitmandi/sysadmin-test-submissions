# SAIC SysAdmin Test 
## Task 2. Shell Scripting

There were two ways in which I could detect which connection I currently was and when I changed my connection.
First, to check my current connection every 10 seconds and keep a track of previous connection. This, although works fine, will always keep the CPU busy, doing unnecessary computation.

So I needed a way to run a script only when my current connection changes. To do so, I used a linux utility name `Network Manager`. This util broadcasts every time a network change is detected, and also has the ability to run scripts at different stages of network switch. 

I first created a shell script which would call a C binary which inturn would call/run a python file.
To do so, first create a `script.sh` file in the `/etc/NetworkManager/dispatcher.d/pre-up.d` directory. 
The contents of the script.sh file are as follows:
~~~
/home/msi/saic/wifi
~~~

`/home/msi/saic/wifi` is a C compiled binary from the file wifi.c

The wifi.c file has the fiollowing.
~~~
#include <unistd.h>

int main()
{
    int id = fork();
    if(!id)
        execlp("python", "/home/msi/saic/script.py", NULL);
}
~~~

And finally the script.py file has the following code.

~~~
import os
import subprocess
import time
import json

time.sleep(2)

res = subprocess.check_output("nmcli").decode("utf-8").split('\n')

with open("wifiConnections.json") as f:
    data = json.load(f)
    wifi = res[0][res[0].find("connected to")+13:]
    if wifi in data.keys():
        os.execute("proxyman load iit")
    else:
        os.execute("proxyman unset")
~~~


So, basically, all the scripts in `pre-ud.d` folder should complete their execution before connecting to any network. That why, A C code with a fork statement was used, which created a child process which run the python file. Then the python file goes to sleep for _2 seconds_. During this time, the parent C process completes its execution, the child process changes its parent to the current terminal. After the 2 seconds durations, we can assume thatg the system has connected to a different netowrk. Therefore `nmcli` gives us the correct network connection.

This script makes use of any external proxy configuration application named `Proxyman`. I tried to make it all self developed but given the time constraints, this is what I used in the final script.

Also you will need proxyman installed on your system + a profile with the name `iit` with proper proxy configurations suited for our college wifi.
