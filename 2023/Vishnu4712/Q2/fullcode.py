import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def send_email(subject, body):
    
    sender_email = "b22144@students.iitmandi.ac.in"
    receiver_email = "saic@students.iitmandi.ac.in"
    password = "password_for_sender_email"

   
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


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


if __name__ == "__main__":
    monitor_docker()
