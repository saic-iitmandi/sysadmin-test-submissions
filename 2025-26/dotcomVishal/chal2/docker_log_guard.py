#!/usr/bin/env python3

import subprocess
import datetime
import re

CRITICAL_KEYWORDS = [
    "error", "critical", "fatal", "panic", "exception",
    "segmentation fault", "crash", "failed"
]

PORT_CLASH_PATTERNS = [
    r"port.*already in use",
    r"bind: address already in use",
    r"cannot assign requested address",
    r"listen tcp.*address already in use"
]

REPORT_FILE = "docker_log_report.txt"

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True, errors="ignore")

def get_running_containers():
    output = run('docker ps --format "{{.ID}} {{.Names}}"')
    if not output.strip():
        print("[INFO] No running containers found.")
        return []
    return [line.split() for line in output.strip().splitlines()]


def analyze_logs(container_id, name):
    logs = run(f"docker logs --tail 200 {container_id}")
    critical = []
    port_clash = False

    for line in logs.splitlines():
        lower = line.lower()

        if any(k in lower for k in CRITICAL_KEYWORDS):
            critical.append(line)

        for p in PORT_CLASH_PATTERNS:
            if re.search(p, lower):
                port_clash = True

    return critical, port_clash

def restart_container(container_id, name):
    print(f"[RECOVERY] Restarting container: {name}")
    run(f"docker restart {container_id}")

def main():
    containers = get_running_containers()

    report_lines = []
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_lines.append(f"=== Docker Log Guard Report ===")
    report_lines.append(f"Generated at: {now}\n")

    for cid, name in containers:
        report_lines.append(f"Container: {name} ({cid})")

        critical_logs, port_clash = analyze_logs(cid, name)

        if critical_logs:
            report_lines.append("  [CRITICAL LOGS]")
            for l in critical_logs:
                report_lines.append("    " + l)
        else:
            report_lines.append("  No critical errors found.")

        if port_clash:
            report_lines.append("  [PORT CLASH DETECTED]")
            restart_container(cid, name)
            report_lines.append("  Container restarted for recovery.")

        report_lines.append("")

    with open(REPORT_FILE, "w") as f:
        f.write("\n".join(report_lines))

    print(f"\nReport written to {REPORT_FILE}")

if __name__ == "__main__":
    main()
