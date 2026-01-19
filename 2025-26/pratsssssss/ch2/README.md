**Created two Dockerized services:**
  - Flask app (workload) using Dockerfile
  - Nginx reverse proxy using Dockerfile.nginx
- The Flask app binds to 8080 → 5000
  The Nginx container tries to bind to the same host port (8080 → 80) creating a port clash scenario

**Script File: monitor.py**
- Detects containers running in Created / Exited state
- Detects port binding failures via docker ps & logs
- Automatically kills the failed container
- Reassigns Nginx to next free port (8081, 8082, ...)
- Verifies recovery by checking status + logs
- Prints filtered + prioritized logs:
    [FAILURE]
    [CLASH]
    [ACTION]
    [RECOVERY]

**How to Simulate Failure**
docker run -d -p 8080:5000 --name web1 flask-web
docker run -d -p 8080:80 --name nginx1 nginx-web
- Result:
    - web1 succeeds
    - nginx1 fails with port clash → enters Created state

Running the Monitor Script:
   - ./monitor.py
if you wants to save logs: 
   - ./monitor.py | tee output.log

**Sample Output Log: output.log**
Contains:
   - Clash detection
   - Recovery action
   - Recovered state
   - Steady state logs

**Verification**
After recovery:
 - docker ps
Shows:
 - web1 healthy on 8080
 - nginx1 healthy on next available port (8081)