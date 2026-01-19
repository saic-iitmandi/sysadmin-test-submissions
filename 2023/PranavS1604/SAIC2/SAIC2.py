import docker
import traceback
import logging
import yagmail
from cred2 import*

def send_email(subject, body, to_email):
    # Set up your Gmail credentials
    gmail_user = user_email #Sender's email through which you will send
    gmail_password = user_password  # 16 characters generated password

    # Set up the connection to Gmail
    yag = yagmail.SMTP(gmail_user, gmail_password)

    # Compose the email
    email_subject = subject
    email_body = body

    # Send the email
    yag.send(to=to_email, subject=email_subject, contents=email_body)

def get_command_info(container):
    config = container.attrs.get("Config")
    cmd = config.get("Cmd")
    entrypoint = config.get("Entrypoint")
    return {
        "Command": " ".join(entrypoint + cmd) if entrypoint else " ".join(cmd),
        "WorkingDir": config.get("WorkingDir", ""),
    }

def monitor_docker_events():
    client = docker.from_env()

    # Iterate over existing containers
    for container in client.containers.list():
        try:
            container_id = container.id
            container_info = client.containers.get(container_id)
            program_info = get_command_info(container_info)
            timestamp = container_info.attrs["State"]["StartedAt"]
            
            subject = "Sysadmin test 2023 - Challenge 2"
            body = f"""Container {container_info.name} started.
                        Program: {program_info['Command']}
                        Working Directory: {program_info['WorkingDir']}
                        Timestamp: {timestamp}"""

            send_email(subject, body, target_email)
            print(subject, body)

        except docker.errors.NotFound:
            logging.warning(f"Container {container_id} not found.")
        except Exception as e:
            logging.error(f"Error processing Docker event: {e}")
            traceback.print_exc()

    # Monitor events for new containers
    for event in client.events(decode=True):
        try:
            container_id = event.get("Actor").get("ID")
            status = event.get("status")

            if status in ["die", "stop"]:
                container_info = client.containers.get(container_id)
                program_info = get_command_info(container_info)
                timestamp = container_info.attrs["State"]["FinishedAt"]
                
                subject = "Sysadmin test 2023 - Challenge 2"
                body = f"""Container {container_info.name} exited.
                        Program: {program_info['Command']}
                        Working Directory: {program_info['WorkingDir']}
                        Timestamp: {timestamp}"""

                send_email(subject, body, target_email)
                print(subject, body)

        except docker.errors.NotFound:
            logging.warning(f"Container {container_id} not found.")
        except Exception as e:
            logging.error(f"Error processing Docker event: {e}")
            traceback.print_exc()

if __name__ == "__main__":
    logging.basicConfig(filename='docker_monitor.log', level=logging.ERROR)
    monitor_docker_events()
