## NOTE : THE OBJECTIVE OF THIS QUESTION WAS NOT ACHIEVED. BELOW IS THE DOCUMENTATION OF THE ATTEMPTS MADE TO SOLVE IT:

# Challenge 1 – Gain Access to a Remote
## Methodology and Attempted Exploitation Report

---

## 1. Scope and Approach

The focus was on identifying misconfigurations, vulnerable services, or local escalation vectors commonly found on improperly secured servers.

A structured methodology was followed:
1. System and service enumeration
2. Identification of privileged execution contexts
3. Investigation of common privilege escalation vectors
4. Controlled exploitation attempts

---

## 2. System Enumeration

After logging in as the `student` user, the following system information was identified:

- Distribution: Ubuntu 14.04.6 LTS
- Kernel: 4.4.0-148-generic
- Architecture: x86_64

---

## 3. Web Service Analysis

An internally hosted web service was accessible from within the virtual machine. The site presented a static page labeled as an internal dashboard.
(Helios Internal Dashboard)

Actions performed:
- Source inspection of the served page
- Manual testing of common endpoints (e.g., `/admin`, `/login`, `/debug`)
- Observation of filesystem and process activity during repeated page requests

Outcome:
- No dynamic behavior or backend interaction was observed
- No file creation, modification, or state changes occurred during requests
- No parameters, inputs, or error messages indicative of web-layer vulnerabilities were identified

Conclusion:
The web service did not appear to provide a direct exploitation surface. I did note that the site looked the same as its source.

---

## 4. Privilege Escalation Enumeration

### 4.1 Sudo Permissions

The following command was executed:
sudo -l

Result:
- The `student` user was not permitted to execute any commands via sudo.

---

### 4.2 SUID Binary Enumeration

The system was scanned for SUID binaries:
find / -perm -4000 2>/dev/null

Findings:
- Only standard system SUID binaries were identified
- No custom or non-standard SUID executables were discovered that could be trivially abused

---

## 5. Privileged Process Analysis

Running processes were examined to identify services executing with root privileges:
ps aux | grep root

A notable process was identified:
/bin/bash /usr/local/bin/helios-runner.sh

Observations:
- The script was owned by root and executed with root privileges
- The file was not readable or executable by the `student` user
- Direct inspection, execution, or tracing of the script was restricted by file permissions

This suggested a potential indirect privilege escalation vector through interaction with resources used by the script rather than direct modification.

---

## 6. Temporary File and Filesystem Interaction Analysis

World-writable directories (`/tmp`, `/var/tmp`) were examined for files potentially used by privileged processes.

Actions performed:
- Identification of temporary files owned by the `student` user
- Monitoring of timestamps before and after system and web activity
- Controlled replacement and symlink-based testing of candidate files

Outcome:
- No timestamp changes or access patterns indicated interaction by privileged processes
- No execution or sourcing of user-controlled temporary files was observed

---

## 7. PATH and Environment-Based Attack Assessment

The execution environment was evaluated for potential PATH hijacking vulnerabilities.

Actions performed:
- Inspection of the `$PATH` variable
- Permission checks on all directories listed in `$PATH`

Outcome:
- All PATH directories were owned by root and not writable by the `student` user
- PATH hijacking did not appear feasible

---

## 8. Polkit / pkexec Investigation

The system was found to be running:
pkexec version 0.105

Given this version, known polkit-based privilege escalation techniques were investigated.

Actions performed:
- Manual invocation of `pkexec` commands
- Timing-based and loop-based authentication bypass attempts
- Verification of polkit service presence and behavior

Outcome:
- Privilege escalation via `pkexec` did not succeed during testing
- Attempts did not produce a root shell or elevated execution context

---

## 9. Kernel-Level Exploitation Consideration

Kernel-level privilege escalation was considered due to the legacy distribution.

Observations:
- Kernel-level privilege escalation attempts did not result in elevated privileges

---

## 10. Conclusion

Root-level access was not obtained within the available time. However, the assessment demonstrated a structured and methodical approach to privilege escalation, including:

- Investigation and elimination of multiple common escalation paths:
  - sudo misconfiguration
  - SUID binary abuse
  - PATH hijacking
  - Insecure temporary file usage
  - Web-based exploitation
  - Known local privilege escalation techniques

All actions were performed in accordance with the challenge restrictions and followed standard security assessment methodology.

---

