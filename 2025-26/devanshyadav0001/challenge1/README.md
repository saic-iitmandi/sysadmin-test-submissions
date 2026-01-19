# Challenge 1 – Helios Privilege Escalation

## 📌 Overview

This challenge involved analyzing a vulnerable Linux virtual machine named **Helios**, identifying internal services, discovering insecure application logic, and attempting a privilege escalation path from a low-privileged user to a higher-privileged service account.

The objective was to demonstrate a logical escalation chain through misconfigured internal services and insecure secret storage.

---

## 🖥️ Environment Setup

- Platform: VirtualBox  
- VM Format: OVA appliance  
- Initial User: `student`  
- Access: Local terminal login  

The target machine was imported into VirtualBox and accessed using provided credentials.  
System enumeration confirmed an Ubuntu Linux environment and absence of administrative privileges.

---

## 🔎 Reconnaissance

Initial enumeration focused on:

- Operating system identification  
- Current user privileges  
- Open network services  

### Key Findings

| Port | Service | Exposure |
|------|---------|----------|
| 22 | SSH | Public |
| 80 | Nginx Web Server | Public |
| 5000 | Internal Helios Web Service | Localhost only |
| 9000 | Internal Helios Worker Service | Localhost only |

The discovery of **internal-only services** indicated hidden attack surfaces within the VM.  
(Page 2 of the report shows service enumeration results.)

---

## 🌐 Web Service Discovery

The public web server on port 80 acted as a **reverse proxy**, forwarding requests to an internal Python backend running on a local-only port.

Direct interaction with the internal backend allowed deeper inspection of application behavior and API logic.  
(Page 3 illustrates reverse proxy configuration and backend mapping.)

---

## 🧩 Vulnerability Discovery

Source code review of the internal web application revealed:

- A hidden internal API endpoint
- An authentication mechanism relying on an internally stored token
- IP-based access restriction limited to localhost

Additionally, sensitive credentials were found stored in a readable configuration file, representing **insecure secret management**.  
(Page 4 of the report details this logic flaw.)

---

## ⚙️ Exploitation Summary (High-Level)

Using the disc
