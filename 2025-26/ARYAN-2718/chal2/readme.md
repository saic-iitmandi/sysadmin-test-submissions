# Challenge 2 – Docker Scripting & Log Analysis

## Introduction

In this challenge, the objective was to analyze logs from Docker containers running web services, detect failures and port conflicts, and automatically recover services wherever possible.

Instead of keeping this purely theoretical, I tested everything on a real local Docker setup and intentionally broke containers to observe real logs and failure behaviour before automating the recovery process.

All work was done locally using Docker Desktop with WSL.

---

## System & Tools Used

- OS: Windows 11  
- Docker: Docker Desktop (WSL backend)  
- Shell: Ubuntu (WSL)  
- Programming Language: Python 
- Web Server for testing: NGINX  

Python was chosen because it made it easy to parse command output, analyze logs, and automate Docker commands in a readable way.

---

## Step 1 – Setting up Web Containers

To simulate containerized websites, I started multiple NGINX containers on different ports.

- `web1` was started on port **8080**
- `badweb` was started on port **8081**

After starting the containers, I verified that:
- Both containers were running using `docker ps`
- Both websites were accessible in the browser via `localhost`

This confirmed that the baseline setup was working correctly.

---

## Step 2 – Simulating a Service Failure

To test log analysis and failure detection, I intentionally stopped the NGINX service inside the `badweb` container.

After stopping the service, I used `docker logs badweb` to inspect the logs.

The logs clearly showed:
- SIGTERM signal received
- Worker processes shutting down
- Graceful exit of the container

This step was important to ensure that the script would later be able to correctly detect a real service failure based on container state and logs.

---

## Step 3 – Simulating a Port Clash

To test port clash detection, I intentionally tried to run two containers on the same host port.

- `clash1` was started on port **9090**
- `clash2` was then started on the same port (**9090**)

Docker returned an error stating that the port was already allocated, and the second container was left in a `Created` state.

This successfully reproduced a real-world port conflict scenario, which the automation script was expected to detect and handle.

---

## Step 4 – Log Analysis & Auto-Recovery Script

After manually observing failures and port clashes, I wrote a Python script to automate the following:

- List all Docker containers (running and stopped)
- Check container status
- Detect critical issues:
  - Containers in `Exited` state (service crash)
  - Containers stuck in `Created` state (startup or port failure)
- Automatically recover services:
  - Restart containers that exited
  - Redeploy containers affected by port clashes using a new free port
- Generate a clean, readable summary report

The script was executed inside WSL using:

python3 docker_log_analyzer.py


---

## Script Output & Verification

When the script was executed, it correctly:

- Detected the stopped `badweb` container
- Restarted it automatically
- Detected the port clash involving `clash2`
- Redeployed the container on a new port
- Left healthy containers untouched

After the script completed, I verified the results using `docker ps`.  
All containers were running successfully and no port conflicts remained.

---

## Summary Report

At the end of execution, the script produced a summary that included:

- Number of healthy containers
- Number of services restarted
- Number of port clashes resolved

This made it easy to understand the overall system state at a glance.

---

## Problems Faced & How They Were Solved

- Docker daemon initially not responding  
  → Fixed by starting Docker Desktop and ensuring WSL2 integration was enabled

- `pkill` not available inside the NGINX container  
  → Used supported signal-based service stopping instead

- Port allocation errors during container startup  
  → Intentionally reproduced to validate detection logic

- Python indentation errors during development  
  → Fixed by converting all indentation to spaces

These issues helped better understand Docker’s runtime behaviour and error handling.

---

## Screenshots Submitted

The following screenshots were captured and included:

1. Docker version and daemon running  
2. Initial running containers (`docker ps`)  
3. NGINX website opened in browser  
4. Logs showing `badweb` service shutdown  
5. Port clash error during container startup  
6. Script execution showing detection and recovery  
7. Final container status after recovery  

---

## Final Status

- Log analysis: Implemented  
- Service failure detection: Working  
- Port clash detection: Verified  
- Automatic recovery: Successful  
- Summary reporting: Completed  




