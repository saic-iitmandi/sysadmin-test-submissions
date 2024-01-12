# SAIC SysAdminTest'23

## Challenge 1 - Gain Access to a Remote Server

Here we are given a .ova file. We need to get inside the server by exploiting any vulnerability we find.

Initially I decompressed the .ova file and got an .vmdk file so that I can explore the files inside the virtual machine. I tried to mount the virtual hard disk as a read-only disk using `vmware-mount.exe saic_fixed-disk001.vmdk c: /v` . It threw this error: `vmware-mount.exe: command not found` . I tried the VMWare Diskmount Utility but still didn't work. 

Then I tried nmap scanning. I then googled how to check open ports in linux. It suggested me a few commands like *ss*, *lsof*, *netsat*, *nmap*,etc. Then I found out using `ss -a` that port 3361,IPP,http,etc. Then I opened the http://localhost in the VM. It was all about Xenia. 

I didn't know any more what to do :( .
