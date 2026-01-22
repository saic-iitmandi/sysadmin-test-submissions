Challenge 2 – Docker Scripting & Log Analysis
Overview

The objective of this challenge was to analyze Docker container logs, identify critical issues, and understand how containerized services behave during failure scenarios such as port conflicts.

The focus was on log inspection, error identification, and service recovery rather than building a complex automation framework.

Log Analysis

Docker container logs were examined using the docker logs command. By reviewing the output of running containers, it is possible to identify service-level messages, startup information, and error conditions related to crashes or misconfigurations.

This approach allows quick identification of issues without directly accessing container internals.

Port Clash Detection

To simulate a real-world failure scenario, a port clash was intentionally created by attempting to start multiple containers bound to the same host port (port 80). Docker correctly returned a bind error indicating that the port was already in use.

This behavior demonstrates how Docker prevents conflicting services from running simultaneously on the same port.

Recovery Approach

After detecting the port clash, the failed container was removed and restarted using a different, free host port. Once reassigned, the container started successfully and the service was restored without further issues.

This mirrors a basic automated recovery strategy where services are reconfigured and restarted to restore availability.

Commands Used

The following Docker commands were used during the process:

docker ps

docker logs <container>

docker run -p <host_port>:80 nginx

Conclusion

This challenge highlights the importance of log analysis and proactive error handling in containerized environments. Understanding how Docker reports failures and how to recover from common issues such as port clashes is essential for maintaining reliable container-based services.
