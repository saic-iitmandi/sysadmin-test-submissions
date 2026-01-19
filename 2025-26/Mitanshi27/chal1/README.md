# Challenge1- Gain access to remote
The objective is to identify and exploit the vulnerabiliy and gain root access on the VM machine (ubuntu) to capture the flag at '/root/flag.txt'.

After importing the VM we enter it by credentials provided: username: student, password:saic

After logging in basic enumeration was performed to identify potential privilege escalation vectors using following system checks: Os and kernel version, SUID binaries, Installed system services and privilege escalation vectors using known CVEs.
During enumeration, it was observed that the system was vulnerable to **PwnKit (CVE-2021-4034)**, a local privilege escalation vulnerability affecting `polkit`.

PwnKit is a local privilege escalation vulnerability in `pkexec` that allows an unprivileged user to execute commands as root due to improper handling of environment variables.

The vulnerable `pkexec` binary was present and had the SUID bit set, making the system exploitable.

A public proof-of-concept exploit for PwnKit was used to escalate privileges from the `student` user to root.

After executing the exploit from within the VM: A root shell was successfully obtained
