**Objective**
- I had to make a remote control connection between my Windows device to another server by running a script on windows and make sure it's get quitely connected and then allow the controller to send shell commands over a raw TCP connection.

**Tools i used:**
- Windows 11 (target)
- Ubuntu WSL (as controller)
- Python3 (To write the listener script)
- Poweshell(Admin)[for target's script]


**What i did, Why i did and where i landed**
-  I had no idea, about what to do although i do got by reading the challenge file but still no idea what i had to do so did some googling and youtube, and came up with that i had to establish an TCF connection, cause TCF was stream based connection and the shell outputs which we needed are text streams so TCF was perfect for that.
- Then took some help from GPT and wrote the listener's script in python. and then wrote powershell client script using System.Net/Sockets/TcpClient and then ran the listener script in WSL and target's script in powershell and let windows connect out to the WSL and send the commands output.
- Although commands do run and i was getting output but noticed stderr getting appended and Powershell was printing something like "Cannot overwrite variable ERROR...."
- did some googling and found out $error was built-in reserved powershell variable which we were using in out target's script so it was conflicting so just changed it  and the spam dissapered. but still powershell window was visible the whole time while commands were running and tbh had no idea how to do it, thought maybe make it script running permanantly, and here took some help from GPT and it gave me solution of running the script using Start-Process and finally now i was able to run commands while Powershell window was closed.