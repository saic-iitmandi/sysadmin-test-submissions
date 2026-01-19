import subprocess
import re
from datetime import datetime

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True, stderr=subprocess.STDOUT)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_file = f"docker_report_{timestamp}.txt"

containers_output = run('docker ps --format "{{.ID}} {{.Names}}"')
containers = containers_output.strip().splitlines()

with open(report_file, "w") as report:
    report.write(f"Docker Log Analysis Report - {timestamp}\n")
    report.write("=" * 40 + "\n\n")

    if not containers:
        report.write("No running containers found.\n")

    for entry in containers:
        cid, name = entry.split()

        logs = run(f"docker logs --tail 200 {cid}")

        critical_lines = [
            line for line in logs.splitlines()
            if re.search(r"(error|fatal|critical|panic|address already in use)", line, re.IGNORECASE)
        ]

        if critical_lines:
            report.write(f"Container: {name}\n")
            report.write("-" * 20 + "\n")
            for line in critical_lines:
                report.write(line + "\n")

            if any("address already in use" in line.lower() for line in critical_lines):
                report.write("⚠ Port clash detected\n")

        report.write("\n")

print(f"Report generated: {report_file}")
