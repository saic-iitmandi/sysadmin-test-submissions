# Challenge 2 – Docker Scripting & Log Analysis

## What I Did
- Ran website containers using Docker.
- Inspected logs using `docker logs`.
- Identified error-level messages.
- Simulated a port clash by binding two containers to the same host port.

## How Port Clash Was Detected
Docker reported a bind failure (`address already in use`) when starting a container on an occupied port.

## Recovery Approach
- Stop the conflicting container.
- Reassign a free port.
- Restart the service.

## How to Reproduce
1. Start a container on port 80.
2. Start another container on port 80.
3. Observe error and resolve by changing port.
