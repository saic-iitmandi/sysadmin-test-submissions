import docker
import socket
import subprocess
import os
import datetime
import re

def connect_to_docker():
    """Tries standard connection, then hunts for the active Docker Context."""
    client = None
    
    # Attempt 1: Standard Environment Connection
    try:
        client = docker.from_env()
        client.ping()
        print(" Connected via standard environment settings.")
        return client
    except:
        pass

    # Attempt 2: Detect Active Context via CLI
    print("  Standard connection failed. Searching for active Docker Context...")
    try:
        # We run 'docker context ls' to find the one marked with '*' or 'true'
        cmd = "docker context ls --format '{{.Current}} {{.DockerEndpoint}}'"
        result = subprocess.check_output(cmd, shell=True).decode('utf-8')
        
        for line in result.splitlines():
            is_active, endpoint = line.split(maxsplit=1)
            
            # Docker Desktop often marks the active one with 'true' or '*' depending on version
            if is_active == 'true' or is_active == '*':
                # Clean up the endpoint (remove unix:// prefix for direct socket use if needed)
                print(f"   Found active context endpoint: {endpoint}")
                
                try:
                    client = docker.DockerClient(base_url=endpoint)
                    client.ping()
                    print(f" Connected successfully to: {endpoint}")
                    return client
                except Exception as e:
                    print(f"    Failed to connect to context endpoint: {e}")
    except Exception as e:
        print(f"   Error checking contexts: {e}")

    # Attempt 3: Hardcoded Fallback for Docker Desktop Linux (Your specific path)
    user_home = os.path.expanduser("~")
    desktop_socket = f"unix://{user_home}/.docker/desktop/docker.sock"
    try:
        client = docker.DockerClient(base_url=desktop_socket)
        client.ping()
        print(f" Connected via fallback path: {desktop_socket}")
        return client
    except:
        pass

    print(" FATAL: Could not connect to any Docker instance.")
    exit(1)

# Initialize Client
client = connect_to_docker()

# Keywords for Log Analysis
LOG_KEYWORDS = ["ERROR", "CRITICAL", "Exception", "Fatal", "Crash", "refused"]

def get_free_port():
    """Finds a random empty port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

def analyze_logs(container):
    """Scans logs for specific error keywords."""
    issues = []
    try:
        logs = container.logs(tail=50).decode('utf-8', errors='ignore')
        for line in logs.split('\n'):
            if any(keyword in line for keyword in LOG_KEYWORDS):
                issues.append(line.strip())
    except:
        pass
    return issues

def scan_and_fix():
    print(f"\n--- [ ANALYSIS STARTED AT {datetime.datetime.now().strftime('%H:%M:%S')} ] ---")
    
    # 1. PORT CLASH DETECTION
    print("\n Checking for Port Clashes...")
    clash_found = False
    
    # We must scan ALL containers to find the 'Created' (failed start) ones
    for container in client.containers.list(all=True):
        if container.status in ["exited", "created"]:
            
            # Check for error in two places: Internal State AND Logs
            state_error = container.attrs.get('State', {}).get('Error', '')
            try:
                logs = container.logs().decode('utf-8', errors='ignore')
            except:
                logs = ""

            # The specific error signature for port clashes
            if "port is already allocated" in state_error or "port is already allocated" in logs:
                clash_found = True
                print(f" CRITICAL: Port Clash detected in '{container.name}'")
                
                new_port = get_free_port()
                print(f"     ACTION: Auto-healing... Redeploying to port {new_port}")
                
                try:
                    # Relaunch the container
                    # Note: We assume internal port 80. In a real script, we might inspect Config.ExposedPorts
                    client.containers.run(
                        container.attrs['Config']['Image'],
                        detach=True,
                        ports={'80/tcp': new_port}, 
                        name=f"{container.name}_recovered"
                    )
                    print(f"    RESOLVED: Service restored as '{container.name}_recovered'")
                    
                    # Cleanup the broken container
                    container.remove(force=True)
                    print("     Cleanup: Failed container removed.")
                    
                except Exception as e:
                    print(f"    FAILURE: Could not autorecover: {e}")

    if not clash_found:
        print("   No port clashes detected.")

    # 2. LOG HEALTH REPORT
    print("\n [ LOG HEALTH SUMMARY ]")
    running_containers = client.containers.list()
    
    if not running_containers:
        print("   No active websites found.")
    
    for container in running_containers:
        issues = analyze_logs(container)
        
        if issues:
            print(f"  {container.name}: {len(issues)} critical entries found.")
            for issue in issues[:3]:
                print(f"    - {issue}")
        else:
            print(f" {container.name}: Healthy (Running)")

if __name__ == "__main__":
    scan_and_fix()