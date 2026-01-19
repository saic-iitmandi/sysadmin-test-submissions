# Challenge 1 – Gain Access to a Remote (SAIC SysAdmin Test)

  
## Challenge Context

  

The objective of **Challenge 1** was to gain access to a provided Linux virtual machine by identifying and exploiting weaknesses **from inside the VM only**, eventually escalating privileges to root and retrieving the flag from:


```

/root/flag.txt

```

Login credentials were provided:

- **Username:** student  
- **Password:** saic  

No recovery mode, GRUB tricks, or disk mounting outside the VM were allowed.

---
## Initial Enumeration

After logging in as the `student` user, the first step was basic system enumeration to understand the environment and exposed services.


Key actions:

- Verified user privileges using `id` and `whoami`
- Checked OS and kernel details
- Enumerated listening services using `netstat` / `ss`
- Tested locally exposed HTTP services via `curl`
A locally hosted service was discovered responding on `127.0.0.1`, showing the message:

```

Helios Internal Dashboard

```


This immediately indicated the presence of an **internal-only service**, not meant to be publicly exposed.

---
## Discovery of the Helios Service (During Inspection)

  

While inspecting the system for misconfigurations and internal services, the **Helios service** was discovered.  

This was **not the original goal**, but a result of systematic inspection during Challenge 1.

### Service Identification

Key findings:

- Helios-related files were located under `/opt/helios`

- Multiple components existed:

  - `web`
  - `worker`
  - `runtime`

- Several directories were inaccessible due to permission restrictions, confirming privilege boundaries
Startup configuration files were found under:

```

/etc/init/

```

including:

- `helios-web.conf`
- `helios-worker.conf`
- `helios-runner.conf`

These revealed how the services were being started at boot.

  
---
## Web Component Analysis

The file:

```

/opt/helios/web/server.py

```


was readable and revealed critical logic.

Important observations from the source code: 

- The web server runs on **127.0.0.1 only**
- The endpoint `/internal/export` existed
- Two trust assumptions were enforced:
  1. Requests must originate from `127.0.0.1`
  2. Requests must include a valid `X-Internal-Token` header

Environment variables were loaded from:

- `/etc/helios/web.env`
- `/etc/helios/worker.env`

These contained sensitive tokens used for inter-service authentication.

---

## HTTP Interaction Attempts

Several requests were attempted to understand server behavior:

- `GET /` → Returned dashboard message
- `GET /internal/export` → Returned `403 Forbidden`
- `OPTIONS` requests → `501 Unsupported method`
- `POST` requests → `403 Forbidden`

These confirmed:

- The service strictly enforced method and header validation
- Token-based trust was a weak point if tokens could be leaked or reused

---
## Worker & Token Relationship


The `/internal/export` endpoint was designed to leak the **SERVICE_TOKEN**, which was explicitly stated in the code as:

```

SERVICE_TOKEN={token}

Used by helios-worker

```


This suggested a trust-chain weakness between services — a classic internal service exposure flaw.

However:
- Direct access to `/opt/helios/worker/control.py` was denied
- Token files were protected by permissions
- No writable paths or injection vectors were found at this stage

  

---
## Privilege Escalation Status

Despite extensive enumeration and service analysis:
- No writable root-owned scripts were found
- No cron misconfigurations were exploitable
- No SUID binaries provided escalation paths
- Tokens could be identified logically but not extracted directly
  

As a result:

> **Root access was not fully achieved.**  

> The challenge was **partially solved**, with deep service understanding but without final privilege escalation.

  

---
  

## Current Status


- ✔ Successful login and enumeration
- ✔ Discovery and analysis of hidden internal service
- ✔ Identification of trust flaws and token flow
- ✖ Root privilege escalation not completed
- ✖ Flag not retrieved
