# Challenge 2 – Docker Scripting & Log Analysis

## Log Analysis
Docker container logs were inspected using `docker logs <container>`.
Error and service-related messages can be identified from container output.

## Port Clash Detection
A port clash was intentionally triggered by binding multiple containers to port 80, resulting in a Docker bind error. The issue was resolved by removing the failed container and restarting it on a free port.

## Recovery
The issue was resolved by reassigning a free port and restarting the affected container.

## Commands Used
- docker ps
- docker logs <container>
- docker run -p <host_port>:80 nginx
