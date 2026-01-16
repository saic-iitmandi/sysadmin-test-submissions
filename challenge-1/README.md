# Challenge 1 - Gain Access to a Remote Server

## Challenge Description

A drive link containing a saic.ova file is provided. It is to be imported into a Virtual Box and ran as a Guest, it will act as a remote server hosting a site wich can be seen on my localhost.

### Objective

To get inside the server by exploiting vulnerabilities and find a flag present at root/flag.txt by obtaining root privilages

### Scope and Constraints

1. Not to use Metasploit
2. Strictly not accessing the mounted disk from outside the VM environment
3. not using Recovery Mode or GRUB Terminal to gain root access
4. Access to server is limited to a VM enviroment only

### Environment

- Virtualization Platform: VirtualBox
- Initial User: `student`
- Initial Privilege Level: Standard user
- Network Mode: NAT

## Initial Access

username : student
password : saic

## Trying To Escalate Privilages

### Trying Sudo Misconfigurations

Command:

    ```bash

        sudo -l
    ```

Output :

    ```text
        Sorry, user student may not run sudo on saic-VirtualBox.
    ```