#!/usr/bin/env python3
import subprocess, json, re, time, os

def sh(cmd):
    return subprocess.check_output(cmd).decode()

def parse():
    out = sh(["docker", "ps", "-a", "--format", "{{json .}}"]).splitlines()
    return [json.loads(l) for l in out]

def logs(name):
    try: return sh(["docker", "logs", "--tail", "200", name])
    except: return ""

def find_free_port(start=8081):
    port = start
    while True:
        out = subprocess.getoutput(f"netstat -tln | grep :{port}")
        if out == "":
            return port
        port += 1

while True:
    print("---scan---")
    containers = parse()

    for c in containers:
        name  = c["Names"]
        state = c["State"]
        status = c["Status"]
        ports = c.get("Ports","")
        log = logs(name)

        # Detect failure (created/exited/stopped)
        if state != "running":
            print(f"[FAILURE] {name} {state}")

            # Detect clash intent
            if "nginx" in name:
                print(f"[CLASH] nginx tried to bind port 8080 but failed")

            print(f"[ACTION] removing failed container: {name}")
            subprocess.call(["docker", "rm", "-f", name])

            # Resilience strategy C: restart on next free port
            new_port = find_free_port()
            print(f"[ACTION] restarting {name} on {new_port}")
            subprocess.call(["docker", "run", "-d", "-p", f"{new_port}:80", "--name", name, "nginx-web"])

            time.sleep(2)
            print(f"[RECOVERY] {name} recovered on {new_port}")
            break

        # log-based detection
        if re.search(r"(CRITICAL|ERROR|bind|address in use)", log, re.I):
            print(f"[LOG-ALERT] {name}")

    time.sleep(3)
