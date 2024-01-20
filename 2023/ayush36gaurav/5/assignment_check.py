import os
import glob
import time
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalendarEvent:
    def __init__(self, **kwargs):
        self.summary = kwargs.get('SUMMARY', '')
        self.dtstamp = datetime.strptime(kwargs.get('DTSTAMP', ''), "%Y%m%dT%H%M%SZ")
        self.dtstart = datetime.strptime(kwargs.get('DTSTART', ''), "%Y%m%dT%H%M%SZ")
        self.dtend = datetime.strptime(kwargs.get('DTEND', ''), "%Y%m%dT%H%M%SZ")

    def __repr__(self):
        return f"{self.summary} - {self.dtstart} to {self.dtend}"

def parse_ics_content(content):
    events = []
    in_event = False
    current_event = {}

    for line in content.split('\n'):
        if line.startswith("BEGIN:VEVENT"):
            in_event = True
            current_event = {}
        elif line.startswith("END:VEVENT"):
            in_event = False
            events.append(CalendarEvent(**current_event))
        elif in_event and ":" in line:
            key, value = line.split(":", 1)
            current_event[key] = value.strip()

    return events

def send_reminder_email(assignment_name, due_date):
    subject = f"Assignment Reminder: '{assignment_name}'"
    from_email = "---Sender's Email---"
    to_email = "---Recipient's Email---"
    recepient_name = "---Recipient's Name---"
    body = f"Dear {recepient_name} \n \nYou have an unsubmitted assigment named '{assignment_name}' due within 6 hours at {due_date} on LMS.\n \nMake sure to submit it on time. \n \nThank You \nLMS Server\nIIT Mandi"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, "---App Password---")  # Provide your app password here
        server.send_message(msg)

# Set your credentials for LMS
username = "---LMS Username---"
password = "---LMS Password---"

# Set the path to the ChromeDriver executable
chrome_driver_path = "C:\\Users\\Dell\\Desktop\\chromedriver.exe" # Path to the chrome driver

# Set the path to the Chrome executable for testing
chrome_binary_path = "C:\\Users\\Dell\\Desktop\\chrome-win64\\chrome.exe" # Path to the chrome executable

# Create ChromeOptions instance
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path

# Create a ChromeDriver instance with ChromeOptions
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://lms.iitmandi.ac.in/login/index.php")

# Wait for the login page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))

# Enter credentials and submit the form
driver.find_element(By.XPATH, "//input[@name='username']").send_keys(username)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Identify the XPath for the "Import or Export Calendars" link and click it
import_export_link_xpath = "//a[contains(text(),'Import or export calendars')]"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, import_export_link_xpath)))
driver.find_element(By.XPATH, import_export_link_xpath).click()

# Click the "Export Calendar" button
export_button_xpath = "//button[contains(text(),'Export calendar')]"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, export_button_xpath)))
driver.find_element(By.XPATH, export_button_xpath).click()

# Check the radio buttons for "All events" and "This month"
driver.find_element(By.XPATH, "//input[@id='id_events_exportevents_all']").click()
driver.find_element(By.XPATH, "//input[@id='id_period_timeperiod_monthnow']").click()

# Click the export button
driver.find_element(By.XPATH, "//input[@id='id_export']").click()

# Wait for the file to be downloaded
time.sleep(5)

# Identify the latest downloaded file in the specified directory
download_directory = "C:\\Users\\Dell\\Downloads\\"
latest_file = max(glob.glob(download_directory + "icalexport*.ics"), key=os.path.getmtime)

# Parse the content of the latest downloaded .ics file
with open(latest_file, 'r') as file:
    ics_content = file.read()

# Update the script to handle unexpected keys
events = parse_ics_content(ics_content)

# Filter events with future deadlines and no submissions
upcoming_events = [event for event in events if event.dtend > datetime.utcnow()]
late_submissions = [event for event in events if event.dtend < datetime.utcnow()]

# Send email reminders for upcoming events
for event in upcoming_events:
    if event.dtend < datetime.utcnow() + timedelta(hours=6):
        send_reminder_email(event.summary, event.dtend + timedelta(hours=5, minutes=30))

# Print late submissions
for event in late_submissions:
    print(f"Past Deadline for '{event.summary}' with deadline on {event.dtend + timedelta(hours=5, minutes=30)}.")

# Close the WebDriver
driver.quit()
