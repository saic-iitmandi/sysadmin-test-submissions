print("Sending email ...")

exits = update= open('/home/abhinandan/Documents/SysAdmin/PS2_Monitor/firstScrape', 'r').read()

# print(exits)

import smtplib
import credentials

def send_email(message):
    sender = credentials.sender_email
    receiver = credentials.receiver_email
    password = credentials.my_password

    subject = 'Sysadmin test 2023 - Challenge 2'

    mail_content = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, mail_content)
    server.quit()

message = 'Alert! Following containers stopped : \n\n' + exits
# print(type(message))
send = send_email(message)
print('Email Sent!')
