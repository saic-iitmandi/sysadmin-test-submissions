import os
import time
import requests
from bs4 import BeautifulSoup
import ssl
import smtplib
import datetime 
import schedule

def job_to_do():
    ID = "enter login id for lms"  # here we can use env file also to take input from it for id and passwd 
    password = "enter password of lms"

    # Initialize the session
    session = requests.Session()

    # Log in to the LMS
    response = session.post('https://lms.iitmandi.ac.in/login/index.php', data={
        'username': ID,
        'password': password
    })

    # Scrape the assignments
    response = session.get('https://lms.iitmandi.ac.in/course/view.php?id=IC152') # Change the course ID here
    # here this scripts check for single course only but we can modify it to work for all courses 
    soup = BeautifulSoup(response.text, 'html.parser')
    assignments = soup.find_all('div', class_='activityinstance')
    # function for sending the email remainder 
    smtp_server = "smtp.gmail.com" # Change this to your email provider's SMTP server
    port = 587 # Change this to your email provider's port number for TLS/STARTTLS
    sender_email = "sender's email address" # The email we're using to send the reminders
    receiver_email = "ID@iitmandi.ac.in" # The email where we want to send the reminders
    password = password # The password for your email account
    subject = "LMS Reminder"
    body = "This is a reminder for a submission of assignment in LMS."
    def send_email(subject, body):
        message = f"6 hours remaining for submission of assignment Course:{subject} "

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    for assignment in assignments:
        # Extract the relevant details
        title = assignment.find('a', class_='instancename').text
        deadline = int(assignment.find('span', class_='label')['data-time'])
        submitted = assignment.find('div', class_='status completed') is not None

        # Calculate the time remaining
        time_remaining = deadline - int(time.time())

        # Send a reminder if there's less than 6 hours remaining
        if not submitted and time_remaining <= 6 * 60 * 60:
            # Email sending code called
            send_email("IC152",body)

    # Print the name of any course and title of assignment that is past deadline and doesn't have any submission yet
    for assignment in assignments:
        # Extract the relevant details
        title = assignment.find('a', class_='instancename').text
        deadline = int(assignment.find('span', class_='label')['data-time'])
        submitted = assignment.find('div', class_='status completed') is not None

        # Check if the assignment is past deadline and not submitted yet
        if not submitted and deadline < int(time.time()):
            print(f'Warning: The assignment "{title}" is past deadline and has not been submitted yet.')


# Check if the current time matches the scheduled time
SCHEDULED_TIME= '10:00' #set it on our own choice
# here just we have checked assignment only once a day at 10 am but we can modify the scipt to check it at regular intervals
def check_schedule():
    current_time = datetime.datetime.now().strftime('%H:%M')
    return current_time == SCHEDULED_TIME
if check_schedule():
    job_to_do()
else:
    # If not, schedule the script to run at the specified time
    schedule.every().day.at(SCHEDULED_TIME).do(job_to_do)
while True:
    schedule.run_pending()
    time.sleep(60)
