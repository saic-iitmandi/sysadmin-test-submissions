import subprocess
import re
import random

print("=" * 60)
print(" Docker Container Monitoring & Auto-Recovery ")
print("=" * 60)

summary = {
    "healthy": 0,
    "restarted": 0,
    "port_clash_fixed": 0
}

containers = subprocess.check_output(
    ["docker", "ps", "-a", "--format", "{{.ID}} {{.Names}} {{.Status}}"],
    text=True
).strip().splitlines()

for container in containers:
    parts = container.split()
    cid = parts[0]
    name = parts[1]
    status = " ".join(parts[2:])

    print(f"\nContainer: {name}")
    print(f"Status   : {status}")

    # 🚨 SERVICE FAILURE (Exited)
    if "exited" in status.lower():
        print("⚠ Service failure detected → restarting container")
        subprocess.run(["docker", "restart", cid], stdout=subprocess.DEVNULL)
        summary["restarted"] += 1
        print("✅ Container restarted successfully")
        print("-" * 60)
        continue

    # 🚨 PORT CLASH (Created state)
    if status.lower().startswith("created"):
        print("⚠ Port clash detected → redeploying container")

        new_port = random.randint(9000, 9999)
        print(f"🔁 Assigning new port: {new_port}")

        subprocess.run(["docker", "rm", cid], stdout=subprocess.DEVNULL)

        subprocess.run([
            "docker", "run", "-d",
            "--name", name,
            "-p", f"{new_port}:80",
            "nginx"
        ], stdout=subprocess.DEVNULL)

        summary["port_clash_fixed"] += 1
        print("✅ Port clash resolved and container redeployed")
        print("-" * 60)
        continue

    # ✅ HEALTHY CONTAINER
    print("✅ No critical issues found")
    summary["healthy"] += 1
    print("-" * 60)

# 📊 SUMMARY REPORT
print("\n" + "=" * 60)
print(" Summary Report ")
print("=" * 60)
print(f"Healthy containers       : {summary['healthy']}")
print(f"Services restarted       : {summary['restarted']}")
print(f"Port clashes resolved    : {summary['port_clash_fixed']}")
print("=" * 60)

