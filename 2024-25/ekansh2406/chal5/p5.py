import os
import time
import smtplib
from datetime import datetime, timedelta
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import base64
import pickle
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
load_dotenv(dotenv_path="path/to/.env")  # Replace with the path to your '.env' file
SCOPES = ['https://www.googleapis.com/auth/gmail.send']


load_dotenv()
USERNAME = os.getenv("BOOKING_USERNAME") # stored in .env file
PASSWORD = os.getenv("BOOKING_PASSWORD") # stored in .env file
BOOKING_URL = "https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx"
DESIRED_DATE = "31/01/2025- 09:00"   # format: DD/MM/YYYY - HH:MM  # desired date and time of booking  
BUS_PATH = "North Campus -To- Mandi (via South)" # path of the bus

parsed_date = datetime.strptime(DESIRED_DATE, "%d/%m/%Y- %H:%M")
booking_release_time = parsed_date - timedelta(days=15)
current_time = datetime.now()
wait_time = (booking_release_time - current_time).total_seconds()
formatted_date = parsed_date.strftime("%d%m%Y")
formatted_time = parsed_date.strftime("%I:%M %p")
if wait_time > 0:
    print(f"Sleeping for {wait_time} seconds until booking opens...")
    time.sleep(wait_time)

def book_seat():
    print(f"Username: {USERNAME}, Password: {PASSWORD}")
    if not USERNAME or not PASSWORD:
        raise ValueError("Environment variables for USERNAME or PASSWORD are not set.")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(BOOKING_URL)
    wait = WebDriverWait(driver, 10) 


    username_field = wait.until(EC.element_to_be_clickable((By.ID, "txtLoginId")))
    username_field.click()
    username_field.send_keys(USERNAME) 
    password_field = wait.until(EC.element_to_be_clickable((By.ID, "txtPassword")))
    password_field.click()
    password_field.send_keys(PASSWORD)
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "btnLogin")))
    login_button.click()
    driver.get(BOOKING_URL)
    
    travel_date_field = wait.until(EC.element_to_be_clickable((By.ID, "txtFromDate")))
    travel_date_field.click()
    

    travel_date_field.send_keys(Keys.CONTROL + "a") 
    travel_date_field.send_keys(Keys.DELETE)
    travel_date_field.send_keys(Keys.HOME)
    travel_date_field.send_keys(formatted_date)
    
    time.sleep(0.1)
    route_dropdown = wait.until(EC.presence_of_element_located((By.ID, "ddlRoute")))
    Select(route_dropdown).select_by_visible_text("North Campus -To- Mandi (via South)")
   
    time.sleep(0.1)
    time_dropdown = wait.until(EC.presence_of_element_located((By.ID, "ddlTiming")))
    select_time = Select(time_dropdown)
    select_time.select_by_visible_text(formatted_time)  

    time.sleep(1)
    bus_dropdown = wait.until(EC.presence_of_element_located((By.ID, "ddlBus")))
    select_bus = Select(bus_dropdown)
    select_bus.select_by_index(1)

    time.sleep(0.1)
    seat_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "checkbox1"))).click()
    # Currently, it will book only seat 1, but we can modify the code to book any empty seat.
   
    time.sleep(0.1)
    save_button = wait.until(EC.element_to_be_clickable((By.ID, "lnkSave")))
    save_button.click()



    """Authenticate and send an email."""
    try:
        service = authenticate_gmail()
        
        sender = 'sender@gmail.com'  # Replace with your email
        to = 'receiver@gmail.com'  # Replace with recipient's email
        subject = 'bus booked'
        body = f'Your booking for {DESIRED_DATE} on {BUS_PATH} is confirmed.'
        send_email(service, sender, to, subject, body)
    
    except Exception as error:
        print(f'An error occurred: {error}')
    driver.quit()


def authenticate_gmail():
    """Authenticate and return the Gmail API service."""
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r"crediantials.json", SCOPES)  # Path to your 'credentials.json' file
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)



def send_email(service, sender, to, subject, body):
    """Send an email message using the Gmail API."""
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(body)
    message.attach(msg)
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    try:
        message = service.users().messages().send(userId="me", body={'raw': raw_message}).execute()
        print(f'Message sent successfully! Message ID: {message["id"]}')
    except HttpError as error:
        print(f'An error occurred: {error}')



book_seat()
