import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import time

login_url = 'https://lms.iitmandi.ac.in/login/index.php'
homepage_url = 'https://lms.iitmandi.ac.in/'

payload = {
    'username': 'b23354',
    'password': 'Piyush@2904'
}

def send_email(subject, body):
    # Gmail SMTP settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465  
    sender_email = 'www.piyushdwivedi117@gmail.com'
    app_password = '***********' # App password generated from Google account settings
    receiver_email = 'b23354@students.iitmandi.ac.in' #student email

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def extract_due_date_and_time(div_element):
    # Use regular expression to extract date and time information
    return div_element.find('strong').text.strip() if div_element else "N/A"

def run_script():
    with requests.Session() as s:
        p = s.get(login_url)
        soup = BeautifulSoup(p.content, 'lxml')
        payload['logintoken'] = soup.find('input', attrs={'name': 'logintoken'})['value']
        r = s.post(login_url, data=payload)
        soup = BeautifulSoup(r.content, 'lxml')

        # Find all <a> tags on the page
        all_links = soup.find_all('a')

        # Define the pattern you're looking for in the href attribute
        course_pattern = "https://lms.iitmandi.ac.in/course/view.php?id="
        matching_course_links = [link.get('href', '') for link in all_links if course_pattern in link.get('href', '')]

        # Create a list to store course information
        courses_info = []

        # Iterate through all course links
        for course_link in matching_course_links:
            # Get the page corresponding to the course link
            t = s.get(course_link)
            soupt = BeautifulSoup(t.content, 'lxml')

            # Finding all elements with class 'activity-item'i.e. all assignments
            activity_items = soupt.find_all('div', class_='activity-item')

            for activity_item in activity_items:
                aalink = activity_item.find('a', class_='aalink')
                assignment_link = aalink['href'] if aalink else "N/A"

                instancename_span = activity_item.find('span', class_='instancename')
                assignment_name = instancename_span.text.strip() if instancename_span else "N/A"

                assignment_info = {
                    "Course ID": course_link.split('=')[-1],
                    "Assignment Name": assignment_name,
                    "Assignment Link": assignment_link,
                }

                courses_info.append(assignment_info)
                print(assignment_info)

run_script()