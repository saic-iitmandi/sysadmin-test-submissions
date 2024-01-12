import subprocess
import smtplib
from email.message import EmailMessage
import json

def monitor_containers():
    try:
        cmd = "docker ps -a --format '{{.ID}}:{{.Names}}:{{.State}}'"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        containers_info = result.stdout.strip().split("\n")

        for container_info in containers_info:
            container_data = container_info.strip("'").split(":")
            if len(container_data) >= 3:
                container_id = container_data[0]
                container_name = container_data[1]
                container_state = container_data[2]
            
            # Check if container state has changed or if it has exited
            if container_state not in ['running', 'active','normal']:
                container_details = subprocess.run(f"docker inspect {container_id}", shell=True, capture_output=True, text=True).stdout
                container_details = json.loads(container_details)

                # Extract useful information like program running inside the container, timestamps, etc.
                program_running = ' '.join(container_details[0]['Args'])
                started_at = container_details[0]['State']['StartedAt']
                stopped_at = container_details[0]['State']['FinishedAt']
                exit_code = container_details[0]['State']['ExitCode']
                error_message = container_details[0]['State']['Error']
                cmd_commands = container_details[0]['Config']['Cmd']
                
                body = (f"""
                    Container ID: {container_id}
                    Name: {container_name}
                    State: {container_state}
                    Program Running Inside: {program_running}
                    Started At: {started_at}
                    Stopped At: {stopped_at}
                    Exit Code: {exit_code}
                    Error Message: {error_message}
                    Running commands : {cmd_commands}
                    """)
                subject = "Sysadmin test 2023 - Challenge 2"
                
                send_email(subject,body)
                
    except Exception as e:
        print(f"Error: {e}")


def send_email(subject,body):
    recipient_email = "saic@students.iitmandi.ac.in"
    

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "utsavjain218@gmial.com" 
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login("utsavjain218@gmail.com", "app password")
        smtp.send_message(msg)


monitor_containers()