# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 15:56:07 2024

@author: arani
"""

def auto(subject,text):
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import smtplib
    smtp = smtplib.SMTP('mail.smtp2go.com', 2525) 
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login('email', 'password')
    msg = MIMEMultipart() 
    msg['Subject'] = subject 
    msg.attach(MIMEText(text)) 
    to = "saic@students.iitmandi.ac.in"
    smtp.sendmail(from_addr="email",to_addrs=to, msg=msg.as_string()) 
    smtp.quit()