# using library docker (module)
import docker
# module for sending info/ alerts to specific email
import smtplib
#  extract, format and print stack traces of a python program
import traceback
# for writing fancy emails
from email.mime.text import MIMEText

# Docker client setup 
client = docker.from_env()

# Function to monitor container status
# It will check for running containers in docker 
def monitor_container_status():
    for container in client.containers.list(all=True):
        container_info = client.api.inspect_container(container.id)
        if container_info['State']['Running'] is False:
            send_email(container_info)

# Function to send alert via email
def send_email(container_info):
    #we have to set sender's email
    sender_email = 'your_email@example.com'
    # receiver email here saic email 
    receiver_email = 'saic@students.iitmandi.ac.in'
    # subject that will be sent to email 
    subject = 'Sysadmin test 2023 - Challenge 2'
    # body of email
    body = 'The container with ID {} and Name {} has exited. \n\n' \
           'It was running the following program: {} \n\n' \
           'The container exited at: {} \n\n' \
           'If any, here is the exit code or traceback: \n{}' \
        .format(container_info['Id'], container_info['Name'], container_info['Config']['Image'], container_info['State']['FinishedAt'], container_info['State']['Error'])
    # this is for handling exception 
    # it will try to connect to docker daemon but if it fails then it will raise exception and print it on console and exits 
    try:
        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = receiver_email

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, 'your_password')
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        # prints on console if alert sent succesfully or not
        print('Alert sent successfully.')
    except Exception as e:
        print('Error occurred while sending alert: ', str(e))
        print(traceback.format_exc())

if __name__ == '__main__':
    #it will continuously check for docker containers info for that it will call monitor_conatiner_status function
    while True:
        monitor_container_status()
