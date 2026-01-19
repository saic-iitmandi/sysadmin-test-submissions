## Instructions for running the script
### Prerequisites:
- Docker Desktop or Docker Engine Installed
- Python 3 installed with the Docker SDK `(pip install docker)`.
- Note: No `sudo` is required if user permissions are configured correctly, but the script supports context switching if needed.

After you have setup your docker environment and initialized the container to run you can run the script, from terminal to fix and monitor Health Summary of the container.
```c 
python3 monitor.py 
```

## Simulating and Verifying the Port Clash scenario
You can simulate the port clash scenario using these publicly available images setup, as explained below

1. Start the blocker (An nginx service) at port 8085 or any other of your choice
```c
docker run -d --name blocker -p 8085:80 nginx
```
2. Start the victim (An HTTPD service) at same port 8085 or whatever you chose for blocker
```c
docker run -d --name victim -p 8085:80 httpd
```
3. Run the Monitor:  Upon execution, monitor.py detects the victim container in a "Created/Exited" state with bind errors.

4. Verify the Fix: The script output confirms the resolution. We can verify the new service is running on a new port (e.g., 34921) using:
```c
docker ps
```
- You will see that, Output shows 'victim_recovered' running on 0.0.0.0:34921->80/tcp (34921 is for representation only, you will actually see a random port here)

5. Service Check: We confirm the website is accessible on the new port:
```c
curl http://localhost:34921
```
-  You will see it returns: `<html><body><h1>It works!</h1></body></html>`

## Sample Log Output

Below is a sample log output after all the above steps along with initialization of an error_app to verify the error_logs given by the script.
```c
Standard connection failed. Searching for active Docker Context...
   Found active context endpoint: unix:///home/kds-hacker/.docker/desktop/docker.sock
 Connected successfully to: unix:///home/kds-hacker/.docker/desktop/docker.sock

--- [ ANALYSIS STARTED AT 21:27:26 ] ---

 Checking for Port Clashes...
 CRITICAL: Port Clash detected in 'victim'
     ACTION: Auto-healing... Redeploying to port 48531
    RESOLVED: Service restored as 'victim_recovered'
     Cleanup: Failed container removed.

 [ LOG HEALTH SUMMARY ]
 victim_recovered: Healthy (Running)
  error_app: 15 critical entries found.
    - 2026-01-17 CRITICAL: Database connection failed
    - 2026-01-17 CRITICAL: Database connection failed
    - 2026-01-17 CRITICAL: Database connection failed
 blocker: Healthy (Running)
```