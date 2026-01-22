Challenge 1 – Gain Access to a Remote
Overview

The goal of this challenge was to identify a vulnerability in the provided Ubuntu virtual machine, exploit it to gain root access, and retrieve the flag located at /root/flag.txt.

The VM was imported and run locally, and all actions were performed from within the system as required.

Initial Access

Access to the machine was provided using the given credentials:

Username: student

Password: saic

After logging in as a low-privileged user, the system was ready for further investigation.

Enumeration

Once logged in, basic enumeration was performed to identify possible privilege escalation paths. This included checking:

Operating system and kernel version

SUID binaries

Installed services and configurations

Known privilege escalation vulnerabilities (CVEs)

During this process, it was observed that the system was running a vulnerable version of polkit, which is affected by PwnKit (CVE-2021-4034).

Vulnerability Identified: PwnKit (CVE-2021-4034)

PwnKit is a local privilege escalation vulnerability in the pkexec utility. Due to improper handling of environment variables, an unprivileged user can execute commands with root privileges.

The pkexec binary on the system had the SUID bit set, confirming that the machine was vulnerable and exploitable.

Exploitation

A publicly available proof-of-concept exploit for PwnKit was executed from the student account. The exploit successfully abused the vulnerable pkexec binary and resulted in a root shell.

No restricted methods such as recovery mode or external disk access were used during exploitation.

Flag Retrieval

After gaining root access, the flag was retrieved directly from the root directory:

/root/flag.txt

Conclusion

This challenge demonstrates how unpatched local privilege escalation vulnerabilities can lead to complete system compromise. It highlights the importance of keeping system packages updated and carefully auditing SUID binaries on production systems.
