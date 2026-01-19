# Docker Service Watch

Docker Service Watch is a host-level monitoring and diagnostic script for Dockerized web services.
It analyzes container logs, detects operational issues, identifies port clashes, and performs safe,
controlled recovery where appropriate.

The script is designed to be conservative by default, transparent in behavior, and suitable for
both manual execution and being automated through a cron job (not implimented yet, can be in the future).

---

## Prerequisites

- Linux system (tested on Ubuntu 22.04) or WSL2 on windows with Docker Desktop.
- Docker installed and running
- At least one running container with a published host port

---

## Running the Script

1. Make the script executable (only required once):

   chmod +x docker-service-watch.sh

2. Run the script:

   ./docker-service-watch.sh

By default, the script:
- Scans recent container logs
- Detects error-level and critical issues
- Attempts recovery only for well-defined infrastructure failures

---

## Script Options (Flags)

The script supports the following command-line options:

- --tail N  
  Number of recent log lines to scan per container (default: 200)

- --historical  
  Scan deeper logs for investigation (automatic recovery disabled)

- --dry-run  
  Detect issues and show actions without executing them

- --help  
  Display usage information

Examples:

./docker-service-watch.sh --tail 1000  
./docker-service-watch.sh --dry-run  
./docker-service-watch.sh --historical  

---


## Simulating a Port Clash Scenario

Port clashes at the Docker host level (for example, two containers attempting to bind the same host
port) are handled directly by the Docker daemon. In such cases, the container fails to start and no
runtime logs are produced. As a result, these failures cannot be detected through container log
analysis.

This script is designed to detect **application-level port binding failures inside a running
container**, where a service fails to bind to a port at runtime and logs the error. These scenarios
are observable via container logs and are suitable for automated handling.

## General Simulation Approach

To simulate a detectable port clash:

- Use any containerized application that attempts to start **multiple services or processes inside
  the same container**
- Ensure that at least two processes attempt to bind the **same port**
- Ensure the container remains running after the failure so that logs can be inspected

This produces a runtime port binding error (commonly logged as `address already in use` or
`EADDRINUSE`) while keeping the container active.

---

## Example Simulation Using a Docker Hub Image

1. Pull a standard application image from Docker Hub (for example, a language runtime or web server):

   docker pull node

2. Run a container that intentionally triggers a port binding failure while remaining running:

   docker run -d --name port-clash-demo -p 3000:3000 node \
     sh -c "node -e \"require('http').createServer(()=>{}).listen(3000); require('http').createServer(()=>{}).listen(3000)\" || true; tail -f /dev/null"

   In this example:
   - One process successfully binds to the port.
   - A second process attempts to bind the same port and fails.
   - The resulting error is written to container logs.
   - The container remains running to allow log inspection.

3. Run the monitoring script:

   ./docker-service-watch.sh

4. Observe output indicating:
   - Detection of a critical port binding error
   - Port clash warning
   - Recovery action (or dry-run output, if enabled)

---


## Verifying Automatic Recovery and Service Restoration

1. Run the script:

   ./docker-service-watch.sh

2. Observe output similar to:

   [WARN] Port clash detected in port-test-2  
   [ACTION] Restarting container port-test-2  
   [INFO] Restart issued for port-test-2  

3. Verify container state:

   docker ps

---

## How the Script Works

### Web-Facing Container Detection

Only containers with published host ports are analyzed.
This ensures the script focuses on externally reachable services and avoids unsafe automation on
internal dependencies.

---

### Log Analysis Strategy

- Logs are analyzed using a bounded window (default: last 200 lines per container)
- This avoids acting on stale or already-resolved issues
- Log depth can be adjusted using the --tail option

---

### Severity Classification

Logs are classified into two severity levels:

Critical (infrastructure-impacting):
- Crashes, fatal errors, segmentation faults
- Port binding failures (address already in use, EADDRINUSE)

Error-level (application-visible):
- Exceptions
- Failures
- Service unavailability

Only critical infrastructure issues are eligible for automatic recovery.

---

### Recovery Safeguards

- Recovery is disabled in --historical mode
- Recovery actions are previewed in --dry-run mode
- All actions are explicitly logged
- No blind or repeated restarts are performed

---

## Design Rationale

This script intentionally avoids:
- Full historical log ingestion
- Runtime- or framework-specific log parsing
- Aggressive or blind remediation

The goal is safe observability and controlled recovery.

---

## Future Improvements

The current design allows for future extensions such as:
- Time-based log scanning
- Pluggable keyword profiles per runtime
- Structured output for alerting systems
- Policy-based recovery thresholds
- Controlled scheduling with explicit safeguards

These are intentionally not implemented to preserve clarity and safety.

---

## Summary

Docker Service Watch provides clear visibility into container health, detects real operational
issues, and acts automatically only when it is safe to do so (like performing recovery while not in dry-run mode)
