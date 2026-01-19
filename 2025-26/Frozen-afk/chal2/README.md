# Challenge 2: Docker Scripting & Log Analysis

**January 18, 2026**

---

## 1 Learning the Basics

For this question, I didn’t know what Docker was initially, so I searched it up. I found out
it’s a tool that helps run applications in isolated environments called ”containers”—kind
of like running a website on a tiny, lightweight virtual computer that has everything the
app needs to run.

I also learned that Docker logs are the stream of text output (stdout/stderr) that
these applications produce, which acts as a record of what the application is doing or if
it has crashed.

I didn’t know the exact meaning of a port, though I had some idea. Now I understand
that a port is like a specific ”door number” on a computer that allows external traffic to
find and communicate with the correct application (like a web server listening on port
80).

---

## 2 Designing the Solution

I used Gemini to get a blueprint of how to approach this since the terms were new to me.
I found that I could solve this using Python, but it required three libraries I had never
used before:

• re: To search for specific patterns or keywords inside the text logs.

• subprocess: To run terminal commands (like docker ps) from inside the Python
script.

• socket: To check if a specific network port is already being used by another process.

I learned how to implement these libraries to build a ”monitor” script.

---

## 3 How the Code Works

### 3.1 Log Analysis

The analyze logs function first gets the list of IDs for all running containers. It then
retrieves their logs (both normal output and errors) using the helper function. I used
re.search() to scan these logs for specific keywords.

Why these keywords? I chose ”Error”, ”Critical”, ”Exception”, and ”Fatal” be-
cause these are standard ”Log Levels” in software development. ”Error” usually means
a specific request failed, while ”Critical” or ”Fatal” often means the application is about
to crash or has stopped working entirely.

Additional Detection: To make the script more robust, I also added ”Panic” (com-
mon in Go/Docker crashes) and ”Traceback” (which indicates a Python script crash).

---

### 3.2 Port Clash Handling Logic

In the check port clash function, the script first creates a list of IDs for stopped con-
tainers and checks their logs for the specific error ”bind: address already in use.”

If a clash is found, it calls the handle recovery function. This function uses a while

loop to find a replacement port, starting from 8081. Inside the loop, it uses the socket

library to attempt a connection to the port.

• The variable result stores the return code from this connection attempt.

• Crucially, if result is 0, it means ”Success”—the connection was successful
because an application is already listening on that port. This tells us the port is
busy, so we increment the port number and try again.

• If result is non-zero (indicating the connection failed), it means the port is free.

Once a free port is found, the loop breaks, and the script uses subprocess to run the
Docker command, successfully assigning that new, open port to the recovered container.

---

## Table of Contents

- Learning the Basics
- Designing the Solution
- How the Code Works
- Log Analysis
- Port Clash Handling Logic


# Challenge 2: Docker Scripting & Log Analysis

**Submitted by:** [Your Name/ID]

## 1. Project Overview
This project solves the challenge of monitoring Docker containers for errors and automatically fixing "Port Clashes."
It includes a Python script (`solver.py`) that:
1.  **Analyzes Logs:** Scans running containers for keywords like "CRITICAL" or "Error".
2.  **Detects Port Clashes:** Identifies containers that stopped because their port was busy.
3.  **Auto-Recovers:** Automatically finds a free port (e.g., 8081) and restarts the crashed service.

## 2. Prerequisites
* **OS:** Linux (Ubuntu recommended)
* **Dependencies:** Docker installed and running.
* **Language:** Python 3 (No external libraries required; uses standard `subprocess`, `re`, `socket`).

## 3. How to Simulate the "Crash" (Setup)
To test the script, you must first create a "broken" environment. Run these commands in your terminal one by one:

**Step A: Clean up any old containers (Optional but recommended)**
```bash
docker rm -f noisy-app mock-clash
```
**Step B: Start a "Noisy" Container (For Log Analysis)**
This container runs forever and prints a generic CRITICAL error every 5 seconds.
```bash
docker run -d --name noisy-app ubuntu /bin/sh -c "while true; do echo 'CRITICAL: Database connection failed'; sleep 5; done"
```
**Step C: Start a "Clashed" Container (For Recovery)**
This container tries to start, prints the "address already in use" error, and immediately exits.
```bash
docker run -d --name mock-clash nginx /bin/sh -c "echo 'bind: address already in use'; exit 1"
```
**Step D: WAIT 10 SECONDS**
Important: Wait a few seconds to ensure the containers have initialized and generated logs before running the solver.

## 4. How to Run the Solution
Once the simulation is running, execute the Python script:
```bash
python3 solver.py > sample_output.txt
```
1.  This will run the logic and save the results into sample_output.txt.
2.  If you want to see the output on the screen immediately, just run python3 solver.py.

## 5. Verification (Proof it Worked)
After the script finishes, verify the automatic recovery:
1.   **Check the Log Report:** View the generated file to see the detection logs:
```bash
cat sample_output.txt
```
Expected Output: You should see Alert: Container... and we handled the port_clash....
2.   **Check Docker Status:** Run the following command to see the recovered container running on a new port:
```bash
docker ps
```
Expected Result: You will see an nginx container running on port 8081 (or 0.0.0.0:8081->80/tcp).


