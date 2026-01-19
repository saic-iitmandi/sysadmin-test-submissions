import os
import datetime
import requests

# ===== TELEGRAM CONFIG =====
# Note: Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID as environment variables
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "YOUR_TELEGRAM_CHAT_ID_HERE")

def telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

# ===== LOG ANALYSIS =====

# Monitor only Challenge-2 related containers
containers = os.popen("docker ps --filter name=site --filter name=demo --filter name=badsite -q").read().splitlines()


report = "DOCKER LOG ANALYSIS REPORT\n"
report += str(datetime.datetime.now()) + "\n\n"

alert_flags = []

for c in containers:
    name = os.popen(f"docker inspect --format='{{{{.Name}}}}' {c}").read().strip()

    logs = os.popen(f"docker logs {c} 2>&1").read()

    report += f"Container: {name}\n"
    report += "-"*50 + "\n"

    # Extract error/critical logs
    errors = [l for l in logs.split("\n") if "error" in l.lower() or "critical" in l.lower()]

    if errors:
        report += "Error Logs:\n"
        for e in errors[-5:]:
            report += "  " + e + "\n"
        alert_flags.append(f"Errors in {name}")

    # Port clash detection
    if "port is already allocated" in logs.lower():
        report += "PORT CLASH DETECTED\n"
        alert_flags.append(f"Port clash in {name}")

    report += "\n"

# Save summary report
with open("docker_log_report.txt", "w") as f:
    f.write(report)

print("Report generated → docker_log_report.txt")

# ---- Container crash detection ----
status = os.popen("docker ps -a --filter name=site --filter name=demo --filter name=badsite").read()


for line in status.split("\n"):
    if "Restarting" in line or "Exited" in line:
        alert_flags.append("Container Crash Detected")

# ---- Send Telegram Alert ----
if alert_flags:
    message = "🚨 DOCKER ALERT 🚨\n\n" + "\n".join(alert_flags)
    telegram(message)
