from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BOOKING_URL = "https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx"
USERNAME = os.getenv("IIT_MANDI_USERNAME")
PASSWORD = os.getenv("IIT_MANDI_PASSWORD")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(subject, body):
    """Sends a confirmation email."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Confirmation email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def login(driver):
    """Logs into the system."""
    driver.get(BOOKING_URL)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "loginButton").click()
        print("Logged in successfully.")
    except TimeoutException:
        print("Error: Login elements did not load in time.")
        driver.quit()
        exit()

def book_seat(driver, bus_path):
    """Books a seat as soon as bookings open."""
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pathSelector"))
        )
        path_selector = driver.find_element(By.ID, "pathSelector")
        path_selector.send_keys(bus_path)
        path_selector.send_keys(Keys.RETURN)

        book_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "bookButton"))
        )
        book_button.click()

        print("Seat booked successfully.")
        email_subject = "Bus Booking Confirmation"
        email_body = f"Your seat has been successfully booked for the path: {bus_path}.\n\nThank you for using the booking system."
        send_email(email_subject, email_body)
    except TimeoutException:
        print("Error: Booking elements did not load in time.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def wait_until_booking_opens(booking_datetime):
    """Waits until the specified booking time."""
    booking_time_epoch = time.mktime(time.strptime(booking_datetime, "%Y-%m-%d %H:%M:%S"))
    current_time = time.time()
    wait_time = booking_time_epoch - current_time
    if wait_time > 0:
        print(f"Waiting for {wait_time} seconds until booking opens...")
        time.sleep(wait_time)
    else:
        print("Booking time has already passed.")

if __name__ == "__main__":
    booking_date = input("Enter the date when the booking opens (YYYY-MM-DD): ")
    booking_time = input("Enter the time when the booking opens (HH:MM AM/PM): ")
    bus_path = input("Enter the bus path: ")

    booking_datetime = f"{booking_date} {time.strftime('%H:%M:%S', time.strptime(booking_time, '%I:%M %p'))}"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)

    try:
        login(driver)
        wait_until_booking_opens(booking_datetime)
        book_seat(driver, bus_path)
    finally:
        driver.quit()