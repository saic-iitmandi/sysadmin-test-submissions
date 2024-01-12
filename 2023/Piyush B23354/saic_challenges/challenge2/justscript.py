import time
import docker

client = docker.from_env()

def alert_on_stop(container_name, program_name, timestamp, exit_code):
    print(f"Container '{container_name}' running '{program_name}' stopped at {timestamp}. Exit code: {exit_code}")

def monitor_containers():
    while True:
        changed_containers = client.containers.list(filters={"status": "exited"})
        
        if changed_containers:
            for container in changed_containers:
                container_info = client.api.inspect_container(container.id)
                container_name = container_info['Name']
                program_name = container_info['Config']['Cmd']
                timestamp = container_info['State']['FinishedAt']
                exit_code = container_info['State']['ExitCode']
                
                alert_on_stop(container_name, program_name, timestamp, exit_code)
        
        
        time.sleep(60)  # Checking the containers every minute

if __name__ == "__main__":
    monitor_containers()

