
from datetime import datetime
import docker
import socket

client = docker.from_env()
REPORT_FILE = "clash_report.txt"


# ---------- Utility Logger ----------
def log(msg):
    with open(REPORT_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


# ---------- Port Utilities ----------
def is_port_free(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(("127.0.0.1", port))
    s.close()
    return result != 0


def find_free_port(start=8000, end=9000):
    for port in range(start, end):
        if is_port_free(port):
            return port
    return None


# ---------- Critical Issue Detection ----------
def detect_critical_issue(container):
    container.reload()
    state = container.attrs["State"]["Status"]

    if state != "running":
        log(f"[CRITICAL] Container {container.name} is NOT running (state = {state})")
        return True
    else:
        log(f"[OK] Container {container.name} running normally")
        return False


# ---------- Port Clash Handler ----------
def handle_port_clash(container):
    container.reload() # Refresh attributes
    
    # Try getting ports from NetworkSettings (Running containers)
    ports = container.attrs["NetworkSettings"]["Ports"]
    
    # If None (common in stopped containers), try HostConfig (Configured ports)
    if not ports:
        port_bindings = container.attrs["HostConfig"]["PortBindings"]
        if port_bindings:
            # Reformat HostConfig to match NetworkSettings structure for the loop below
            ports = port_bindings
        else:
            log(f"[INFO] Container {container.name} has no exposed ports configuration")
            return

    for container_port, bindings in ports.items():
        if bindings is None:
            continue

        host_port = int(bindings[0]["HostPort"])

        # Check if the host port is currently occupied
        if not is_port_free(host_port):
            
            # LOGIC CHANGE HERE:
            # If the container is RUNNING, it owns the port. leave it alone (It is the "First" container).
            if container.status == "running":
                log(f"[INFO] Port {host_port} is busy, but owned by THIS running container ({container.name}). No action needed.")
                continue

            # If the container is NOT RUNNING (Stopped/Created), and port is busy, 
            # this is the "Second" container. We reroute THIS one.
            log(f"[WARNING] Port clash detected on host port {host_port}. Container {container.name} cannot start.")

            new_port = find_free_port()
            if new_port is None:
                log("[ERROR] No free port available. Manual intervention required.")
                return

            log(f"[RECOVERY] Rerouting colliding container {container.name} to new port {new_port}")

            image = container.attrs["Config"]["Image"]

            # Remove the clashing container
            container.remove()

            # Recreate it with the new port mapping
            client.containers.run(
                image,
                name=container.name,
                detach=True,
                ports={container_port: new_port}
            )

            log(f"[SUCCESS] Container {container.name} rerouted and started on port {new_port}")

        else:
            # If port is free and container is stopped, we might want to start it, 
            # but strict instructions say only handle clashes.
            log(f"[OK] Port {host_port} is free for container {container.name}")


# ---------- Main Controller ----------
def main():
    # Clear old report
    open(REPORT_FILE, "w", encoding="utf-8").close()

    log("===== Clash_WATCH CORE SYSTEM REPORT =====")
    log(f"Timestamp: {datetime.now()}\n")

    containers = client.containers.list(all=True)

    if not containers:
        log("No containers found on system.")
        return

    for container in containers:
        log(f"\nInspecting Container: {container.name}")

        # Step 1 — Detect critical container state issue
        detect_critical_issue(container)

        # Step 2 — Detect and fix port clash
        handle_port_clash(container)

    log("\n===== REPORT COMPLETE =====")
    print("Report saved to clash_report.txt")


# ---------- Runner ----------
if __name__ == "__main__":
    main()