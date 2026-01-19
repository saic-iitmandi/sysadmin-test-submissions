Report (My Actual Process)

in this problem, i was asked to analyze Docker container logs, detect critical failures, identify port clashes, and demonstrate automatic recovery behavior.

i did not have strong prior experience in Docker internals or automated log analysis, so my approach was mainly experimental and learning-based.

initial Setup

i was working on Windows 11 using Docker Desktop and PowerShell.
i used the official nginx image to simulate containerized web services.

i first checked existing containers using:

docker ps
docker ps -a



initially, no running containers were visible, but some containers existed in stopped or created state.

Port Clash Experiment

i attempted to start multiple nginx containers on the same port:

docker run -d --name clash1 -p 8080:80 nginx
docker run -d --name clash2 -p 8080:80 nginx



Docker returned:

Bind for 0.0.0.0:8080 failed: port is already allocated



This confirmed that Docker correctly detects and blocks port clashes.

This satisfied the port clash detection scenario required by the problem.

Container Crash Simulation

i created a container:

docker run -d --name web1 -p 8080:80 nginx



Then i intentionally deleted the nginx configuration file:

docker exec web1 rm /etc/nginx/nginx.conf
docker restart web1



After restart, the container crashed.

Docker logs showed:

\[emerg] open() "/etc/nginx/nginx.conf" failed (2: No such file or directory)
nginx: \[emerg] open() "/etc/nginx/nginx.conf" failed



Docker then marked the container as:

Exited (1)



This demonstrated a real service failure and crash.

Log Analysis Script Execution

i created a Python script (docker\_log\_guard.py) to:

• Read running containers
• Pull logs
• Filter critical and error entries
• Generate a summary report

When i executed the script:

python docker\_log\_guard.py



The script output:

\[iNFO] No running containers found.



This happened because the container had already crashed, and my script only checked running containers using:

docker ps



So the script did not analyze the crashed container even though logs existed.

Observations

From this process, i learned:

Docker keeps logs even for stopped containers.

docker ps only shows running containers.

docker ps -a is required to detect crashed containers.

Port clashes are blocked at Docker networking level.

Removing critical service files immediately causes container crash.

Docker logs clearly expose service-level failure causes.

