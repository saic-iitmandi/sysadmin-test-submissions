\# Challenge 1
1.Operating the virtual machine

After a lot of confusion regarding the question, I finally learnt that I had to first install a virtual Box. The file saic ova file was imported into the Virtual box and opened. I understood later that the local host of the Virtual machine is not the same as the local host of our computer. 



2.Gettin familiar with the environment

I logged in using the credentials provided to me as student user. Earlier I had practiced a bit of Linux commands and attempted to open and discover what all files I could. I tried using the Sudo command to gain access but again was denied permission. Then by first using the ls -all command listed all the files. I tried to understand the structure it was written in and each character stood for, and opened .. (home directory) because I saw that file was owned by the root and belong to the group root as well. In that I found 3 more directories namely ops saic and student.

I tried to enter the ops directory but was denied permission but got access to the saic directory.

I then checked which all files were readable by the ls -all, ls -ld commands. I was denied permission to see the bash\_histroy.

I read the readable files by using the cat command.

Got a file named sudo and opened it’s content and found the following flag.

SAIC{C0ngr4ts\_y0u\_s0lv3d\_it\_saic-VirtualBox}  /root/flag.txt 

What I did in this challenge was directory enumerations. I figured ever file and directory which seemed unusual and checked it

