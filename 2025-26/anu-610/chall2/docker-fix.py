import docker
import google.generativeai as genai
import os
import re
import socket
import time

# --- CONFIGURATION ---
GENAI_API_KEY = "AIzaSyD2mz5aBgjOm8CIiEZPb6lXqvTyucbmim8"
genai.configure(api_key=GENAI_API_KEY)

# Initialize
client = docker.from_env()
model = genai.GenerativeModel('gemini-2.5-flash')

# --- PART 1: LOG ANALYSIS (For Running Containers) ---
def analyze_running_websites():
    print("\n[TASK 1] 🔍 Scanning Running Containers for Application Errors...")
    
    # Get only running containers
    running_containers = client.containers.list(filters={'status': 'running'})
    
    with open("website_health_report.md", "w") as report:
        report.write("# 📊 Website Health Report\n\n")
        
        for container in running_containers:
            # 1. Fetch Logs
            try:
                logs = container.logs(tail=100).decode('utf-8', errors='ignore')
            except Exception as e:
                print(f"  ⚠️ Could not read logs for {container.name}")
                continue

            # 2. Filter: Look for critical app errors (Traffic crashes, 500s, Exceptions)
            # We skip 'info' logs and look for signals of distress
            error_pattern = re.compile(r'(ERROR|CRITICAL|FATAL|Exception|Traceback|50[0-9] )', re.IGNORECASE)
            
            if error_pattern.search(logs):
                print(f"  🚩 Issue detected in website: {container.name}")
                
                # 3. AI Analysis
                prompt = f"""
                Analyze these logs from a Dockerized website ('{container.name}').
                Focus on application crashes, high-traffic failures, or backend errors.
                
                LOGS:
                {logs[-2000:]} 
                
                REPORT:
                - **Issue:** (What specifically failed? e.g., Database timeout, Syntax error)
                - **Severity:** (Low/Medium/Critical)
                - **Recommended Fix:** (How to resolve it)
                """
                
                try:
                    response = model.generate_content(prompt)
                    analysis = response.text.strip()
                    
                    # Write to Report
                    report.write(f"## 🌐 Container: `{container.name}`\n")
                    report.write(f"**Status:** Running (With Errors)\n")
                    report.write(f"{analysis}\n")
                    report.write("---\n")
                except Exception as e:
                    print(f"  ❌ AI Analysis failed: {e}")
            else:
                print(f"  ✅ {container.name} seems stable.")

# --- PART 2: PORT CLASH HANDLING (For Failed Startup) ---
def find_free_port(start_port):
    """Utility: Finds the next available port on the host."""
    port = int(start_port)
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
            port += 1

def resolve_port_clashes():
    print("\n[TASK 2] 🚑 Checking for Port Clash Crashes...")
    
    # Get EXITED containers (where startup failures live)
    exited_containers = client.containers.list(filters={'status': ['exited', 'created']})
    print(exited_containers)
    for container in exited_containers:
        try:
            # Check exit code (1 or 128+ usually means crash)
            if container.attrs['State']['ExitCode'] == 0:
                continue
            container.reload()

            logs = container.logs().decode('utf-8', errors='ignore')
            # NEW: Get the System Error (if logs are empty)
            system_error = container.attrs['State']['Error']
            print(system_error)
            # Combine logs and system error for detection
            full_evidence = logs + " " + system_error


            # Detect Port Clash Signature
            if "port is already allocated" in full_evidence or "Address already in use" in full_evidence:
                print(f"  💥 Port Clash Detected: {container.name}")
                
                # 1. Extract the Config from the dead container
                image = container.attrs['Config']['Image']
                print(f"image: {image}")
                
                # Get the ports it TRIED to use. 
                # Format: {'80/tcp': [{'HostIp': '', 'HostPort': '8080'}]}
                port_bindings = container.attrs['HostConfig']['PortBindings']
                
                if not port_bindings:
                    print("  ⚠️ No port bindings found to fix.")
                    continue

                # 2. Calculate New Ports
                new_bindings = {}
                for internal_port, bindings in port_bindings.items():
                    for binding in bindings:
                        old_host_port = binding['HostPort']
                        new_host_port = find_free_port(int(old_host_port) + 1)
                        
                        print(f"    - Remapping {internal_port}: Host {old_host_port} -> {new_host_port}")
                        new_bindings[internal_port] = new_host_port

                # 3. Automatic Recovery
                print(f"    - removing dead container...")
                container.remove()
                
                print(f"    - 🚀 Restarting service on new port...")
                new_container = client.containers.run(
                    image,
                    ports=new_bindings,
                    detach=True,
                    name=f"{container.name}_recovered"
                )
                print(f"    ✅ Recovery Successful! New ID: {new_container.short_id}")
                with open("recovery_audit.txt", "a") as audit:
                    audit.write(f"[{time.ctime()}] Fixed Port Clash for '{container.name}'. Moved to Port {new_host_port}.\n")

        except Exception as e:
            print(f"  ❌ Recovery failed for {container.name}: {e}")

if __name__ == "__main__":
    print("--- 🤖 SYSADMIN AGENT STARTED ---")
    analyze_running_websites()
    resolve_port_clashes()
    print("\n--- ✅ MISSION COMPLETE ---")