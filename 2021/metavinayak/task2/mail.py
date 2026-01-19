## https://realpython.com/python-send-email/
import smtplib, ssl,sys

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "xyz@gmail.com"
receiver_email = "pqr@gmail.com"
password="<Enter password here>"

info_file=sys.argv[1] # supplied as argument by bash script
message=open(info_file,"r+").read()

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
