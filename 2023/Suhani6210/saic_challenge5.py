#challenge 5
import getpass, smtplib  
host="smtp-mail.outlook.com"
port=587
from_email="suhani.sharma6210@outlook.com"
to_email="tryanderror1288@gmail.com"  #to be taken via web scraping
pwd=getpass.getpass('Enter your password here :')

msg="""Subject: Reminder regarding unsubmitted assignment

Dear student
 
This is a reminder about your upcoming assignment which is due 6 hours from now.
Kindly submit the assignment on time 

Regards
Well wisher
"""
smtp=smtplib.SMTP(host,port)

try:
    status_code,response=smtp.ehlo()    
    print(f"[*] Echoing the server: {status_code},{response}")    
    status_code,response=smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")  

    status_code, repsonse = smtp.login(from_email,pwd)
    print(f"[*] Starting Logging in: {status_code} {response}")

    smtp.sendmail(from_email,to_email,msg)
    print('Mail sent successfully')

except smtplib.SMTPAuthenticationError as e:
     print(f"Error: SMTP Authentication failed. {e}")

smtp.quit()

 



