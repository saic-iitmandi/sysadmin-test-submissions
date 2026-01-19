#!/usr/bin/env python3

import subprocess
import re
import json
from datetime import datetime

def get_running_containers():
    result = subprocess.run(
        ["docker", "ps", "--format", "{{.ID}} {{.Names}} {{.Ports}} {{.Image}}"],
        capture_output=True, text=True
    )
    containers = []
    for line in result.stdout.strip().split("\n"):
        if line:
            parts = line.split()
            cid = parts[0]
            cname = parts[1]
            ports = " ".join(parts[2:-1])
            image = parts[-1]
            containers.append({"id": cid, "name": cname, "ports": ports, "image": image})
    return containers

def analyze_logs(container_id):
    try:
        result = subprocess.run(
            ["docker", "logs", "--since", "1h", container_id],
            capture_output=True, text=True, timeout=10
        )
        logs = result.stdout.splitlines()
        errors = [line for line in logs if re.search(r"CRITICAL|ERROR|FAIL|Traceback", line, re.IGNORECASE)]
        return errors
    except subprocess.TimeoutExpired:
        return ["ERROR: Could not fetch logs (timeout)"]

def detect_port_clash(containers):
    """Detect if multiple containers are using the same host port."""
    port_map = {}
    clashes = []
    for c in containers:
        ports = re.findall(r'(\d+)->', c["ports"])
        for p in ports:
            if p in port_map:
                # Only record clash if containers are different
                first_container = port_map[p]
                second_container = c["name"]
                if first_container != second_container:
                    clashes.append((p, first_container, second_container))
            else:
                port_map[p] = c["name"]
    return clashes


def recover_port_clash(clash, containers):

    port, c1_name, c2_name = clash
    print(f"[WARNING] Port clash detected on port {port} between {c1_name} and {c2_name}")

    c2 = next((c for c in containers if c["name"] == c2_name), None)
    if not c2:
        print(f"[ERROR] Could not find container {c2_name}")
        return

    image = c2["image"]

def generate_summary(containers):

    summary = {}
    for c in containers:
        errors = analyze_logs(c["id"])
        summary[c["name"]] = errors

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    summary_file = f"docker_log_summary_{timestamp}.json"
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=4)

    print(f"[INFO] Summary report saved to {summary_file}")
    return summary_file

if __name__ == "__main__":
    print("[INFO] Starting Docker log analysis...")

    containers = get_running_containers()
    num_containers = len(containers)

    if num_containers == 0:
        print("[INFO] No running containers found. Exiting.")
        exit()
    elif num_containers == 1:
        print(f"[INFO] Only one container running: {containers[0]['name']}. No port clashes possible.")

    clashes = detect_port_clash(containers)
    if clashes:
        for clash in clashes:
            recover_port_clash(clash, containers)
    else:
        if num_containers > 1:
            print("[INFO] No port clashes detected.")

    summary_file = generate_summary(containers)
    print("[INFO] Docker monitoring complete.")
