import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import docker

client = docker.from_env()

# adding the mailing service
smtp_server = 'smtp.gmail.com'
smtp_port = 465  
sender_email = ''
app_password = ''
receiver_email = ''

def send_email(container_name, program_name, timestamp, exit_code):
    subject = f"Container Alert: {container_name} Status Change"
    body = f"Container '{container_name}' running '{program_name}' stopped at {timestamp}. Exit code: {exit_code}"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.set_debuglevel(1)  

            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print("Error occurred while sending email:")
        print(e)

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
                
                send_email(container_name, program_name, timestamp, exit_code)
        
        time.sleep(60)  # Monitoring the containers every minute

if __name__ == "__main__":
    monitor_containers()
