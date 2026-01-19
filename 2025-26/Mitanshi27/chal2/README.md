# Challenge 2 – Docker Scripting & Log Analysis

## Log Analysis
Docker container logs were inspected using `docker logs <container>`.
Error and service-related messages can be identified from container output.

## Port Clash Detection
A port clash was simulated by attempting to start multiple containers on the same host port.
Docker correctly reported a bind failure (`address already in use`).

## Recovery
The issue was resolved by reassigning a free port and restarting the affected container.

## Commands Used
- docker ps
- docker logs <container>
- docker run -p <host_port>:80 nginx
