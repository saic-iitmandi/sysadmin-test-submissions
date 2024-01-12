import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import time

login_url = 'https://lms.iitmandi.ac.in/login/index.php'
homepage_url = 'https://lms.iitmandi.ac.in-/'

payload = {
    'username': 'b23354',
    'password': '****thepassword****'
}

def send_email(subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465  
    sender_email = 'www.piyushdwivedi117@gmail.com'
    app_password = '***********' # App password generated from Google account settings
    receiver_email = 'b23354@students.iitmandi.ac.in' #student email

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def extract_due_date_and_time(div_element):
    return div_element.find('strong').text.strip() if div_element else "N/A"

def run_script():
    with requests.Session() as s:
        p = s.get(login_url)
        soup = BeautifulSoup(p.content, 'lxml')
        payload['logintoken'] = soup.find('input', attrs={'name': 'logintoken'})['value']
        r = s.post(login_url, data=payload)
        soup = BeautifulSoup(r.content, 'lxml')

        all_links = soup.find_all('a')

        course_pattern = "https://lms.iitmandi.ac.in/course/view.php?id="
        matching_course_links = [link.get('href', '') for link in all_links if course_pattern in link.get('href', '')]
        courses_info = []

        for course_link in matching_course_links:
            t = s.get(course_link)
            soupt = BeautifulSoup(t.content, 'lxml')

            activity_items = soupt.find_all('div', class_='activity-item')

            for activity_item in activity_items:
                aalink = activity_item.find('a', class_='aalink')
                assignment_link = aalink['href'] if aalink else "N/A"

                instancename_span = activity_item.find('span', class_='instancename')
                assignment_name = instancename_span.text.strip() if instancename_span else "N/A"

                due_date_element = activity_item.find('div', class_='cursor-hover')
                due_date_str = extract_due_date_and_time(due_date_element)

                assignment_info = {
                    "Course ID": course_link.split('=')[-1],
                    "Assignment Name": assignment_name,
                    "Assignment Link": assignment_link,
                    "Due Date and Time": due_date_str
                }

                courses_info.append(assignment_info)

    current_time = datetime.now()
    for course_info in courses_info:
        due_datetime = datetime.strptime(course_info["Due Date and Time"], "%A, %d %B %Y, %I:%M %p")
        reminder_time = due_datetime - timedelta(hours=6)

        if current_time < reminder_time < current_time + timedelta(hours=3):
            subject = f"Assignment Reminder: {course_info['Assignment Name']}"
            body = f"Assignment '{course_info['Assignment Name']}' is due on {course_info['Due Date and Time']}."
            send_email(subject, body)

if __name__ == "__main__":
    while True:
        run_script()
        time.sleep(3 * 60 * 60)
