import subprocess
import time

def monitor_docker():
    while True:
        try:
            docker_ps_output = subprocess.check_output(["docker", "ps", "--format", "{{.ID}} {{.Names}} {{.Status}}"])
            container_list = docker_ps_output.decode("utf-8").split("\n")[:-1]
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving Docker container information: {e}")
            time.sleep(60)
            continue
        
        for container_info in container_list:
            container_info_parts = container_info.split(maxsplit=2)
            if len(container_info_parts) == 3:
                container_id, container_name, container_status = container_info_parts
                if container_status not in ["Up", "Healthy"]:
                    subject = "Sysadmin test 2023 - Challenge 2"
                    body = f"Container {container_name} (ID: {container_id}) exited or changed state at {time.ctime()}"
                    send_email(subject, body)

        time.sleep(60)
