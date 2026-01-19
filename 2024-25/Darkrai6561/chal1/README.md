Question 1
Opened the vuln.ova file in Vm
 

Went to guest login and opened terminal
![image](https://github.com/user-attachments/assets/86ed2313-86dd-4fcf-8c2f-3cfc7ec8837d)

First opened firefox and checked what is the thing it is hosting
entered ‘localhost’ and a website came up asking for sign in
made a dummy account
 ![image](https://github.com/user-attachments/assets/c8c2f69e-a9fc-41ac-bc42-a7683288b8c9)


Then inspected the website found nothing interesting for now
After that I knew I should find some ip address and all because if something is connected to internet it should have an ip address and It will be helpful somehow











Did some research on how to find ip address
Then used the command ip addr show to get the ip address of the machine
![image](https://github.com/user-attachments/assets/3f3d665b-3c06-466b-bd40-9ced3092893b)

 
Here I see 2 addresses that I believe might be the correct ip addresses of the machine the one in inet6 that’s 127.0.0.1/8  And  one in eth0 that’s 10.0.2.15/24
did some googling on ip addresses and found the one starting with 12.0.0 is local address and 10.0.2.15 is the default ip assigned for every machine connected to nat
At this point I thought that the ips were not that useful for now
But then I remembered seeing a similar solution in last years solution repository and they did port forwarding, so I did the same using the ips I found and accessed the same website on my local machine
I didn’t understand why should I do it but still did it anyways
After that I was a bit clueless
so asked chatgpt It suggested me I get the public ip address of the machine using command
 curl ifconfig.me    used it but it wasn’t installed and it needed admin permissions to install
so used an alternative wget -qO- ifconfig.me and this one worked
the ip address I found was 14.139.34.151
 
![image](https://github.com/user-attachments/assets/142d11af-bb88-4e61-956b-104bf031af24)

Now I got the public Ip address 
so I sometimes do ctfs and while reading resources on it somewhere they mentioned to find open ports on a ip address
so tried to do that 
Found a command nmap for this

ran it on my local machine
Found 4 ports 113, 4443,3306 and one more but there was an issue that I will address later on
Tried to access the ports but nothing seemed to be working  ;-;

It took quite a long time so just took a break
after few hours came back and ran nmap again but this time only could see 2 ports 


 
Again tried to access them using ssh, nc, even put the ports on browser but nothing worked
![image](https://github.com/user-attachments/assets/8905bc73-f563-4d78-9c9d-8b4b039414d9)


So decided to just drop the idea and do something else with the machine
I explored all the files on the machine first the home ones that had things like desktop, downloads etc
there was nothing there so used command cd / to access other files like root, bin,etc

explored all files like bin, etc which I thought might have some clue 

thought hard and read a lot of logs and all that appeared but nothing had things of my interest

Resorted to using chatgpt again and asked it to summarize what every kind of file does
It gave lots of explaination couldn’t understand much, so just straight up asked “I have a virtual vm machine that is hosting a website which of the files might have the files for the website” it told me var/www might have them
so went there and found all the files of website :D
![image](https://github.com/user-attachments/assets/34bb97a8-3076-461c-9769-d1411706e566)

 
now my most basic sense was screaming at me that database directory might have things like passwords and all but still before going to database “super genius me /s” went to see all the other files 
… they had lots of things, lots of things that almost made my brain fried

So finally I went to database and read the files there
First in seed.sql found this
 
 
![image](https://github.com/user-attachments/assets/5b0fd99e-ed2e-492d-a017-98a60a33d24a)
These are some interesting infos
15476daa5905d5e8e38062b4dc423cd7 this seems to be some kind of encryption for password
And ‘-password for user is shortpass’ seems something worth to look into 
now I need to know what is that encryption 
Read the schema.sql file and found this


 ![image](https://github.com/user-attachments/assets/224f051f-1f54-433d-a65a-a8515481c111)

Doesn’t seem that interesting just seems to be declaration of variable kind of thing
Readme.md in www directory seemed to have some links
But they weren’t opening :(
 
 ![image](https://github.com/user-attachments/assets/4bf7622a-7981-4670-bcf9-819aff872826)

 
 
 

I did lots of research on what could I do more but couldn’t understand anything
So just thought its what all I could do for now maybe I will come back to it if I have time after trying other questions but for now I stop my infiltration journey here 
