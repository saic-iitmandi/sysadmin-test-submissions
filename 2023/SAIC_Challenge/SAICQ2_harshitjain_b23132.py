#  password :: juru ppln nmfj civc
import os
import ssl # to add a layer of security
import smtplib # to send our email
from email.message import EmailMessage
import subprocess
import re
import time
import subprocess

def container_states():
    command = ["docker", "ps", "-a" ]
    output = subprocess.check_output(command)
    output=output.decode("utf-8")
    output=output.splitlines()
    list1=[]
    list_a=[]
    for i in output[1:]:
        j=re.split(r'\s{2,}',i)     # this line is used to split the output string if it finds 2 or more spaces occuring together.         
        list1.append(j)
    # print(list1)
    return list1

def send_email(subject,body):
            email_sender="harshitjjain05@gmail.com"
            email_password="juru ppln nmfj civc"
            email_receiver="harshitjainsolan@gmail.com"
            b=EmailMessage()
            b["From"]=email_sender
            b["To"]=email_receiver
            b["Subject"]=subject
            b.set_content(body)
            context=ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_receiver, b.as_string())        

states= container_states()
flag=0
while flag<100 :
    time.sleep(60)  # Wait for 60 seconds
    new_states = container_states()
    for i in range(min(len(states),len(new_states))):
    
        if states[i][4]!= new_states[i][4]:  
                subject="Sending the result of dockers running."
                body=f"Container {new_states[i][0]} changed state from {states[i][4]} to {new_states[i][4]}"
                send_email(subject, body)
    flag+=1
    states = new_states