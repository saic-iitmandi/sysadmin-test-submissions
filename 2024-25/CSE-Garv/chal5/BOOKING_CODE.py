import os
import time
import datetime
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from apscheduler.schedulers.blocking import BlockingScheduler
import smtplib
from email.mime.text import MIMEText

# Load credentials securely (replace with your .env values or hardcoded)
USERNAME = config("USERNAME")
PASSWORD = config("PASSWORD")
EMAIL = config("EMAIL")
EMAIL_PASSWORD = config("EMAIL_PASSWORD")

LOGIN_URL = "https://oas.iitmandi.ac.in/InstituteProcess/Common/Login.aspx"
BOOKING_URL = "https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx"
DESIRED_PATH = "North Campus -To- Mandi (via South)"


# Function to check if an element is focusable
def is_focusable(driver, element):
    return element.is_displayed() and element.is_enabled()


# Function to book a bus seat
def book_seat():
    global booking_time, booking_date
    try:
        # Format the booking date to match the input format required
        booking_date_formatted = booking_date[8:] + booking_date[5:7] + booking_date[:4]

        # Initialize WebDriver (use the appropriate driver for your browser)
        driver = webdriver.Edge()
        driver.get(LOGIN_URL)
        wait = WebDriverWait(driver, 10)

        # Login to the system
        driver.find_element(By.ID, "txtLoginId").send_keys(USERNAME)
        driver.find_element(By.ID, "txtPassword").send_keys(PASSWORD)
        driver.find_element(By.ID, "btnLogin").click()

        # Navigate to the booking page
        driver.get(BOOKING_URL)
        time.sleep(1)

        # Fill in the booking details
        text_field = wait.until(EC.presence_of_element_located((By.ID, "txtFromDate")))
        text_field.click()
        for _ in range(13):  # Move to the start of the text field
            text_field.send_keys(Keys.ARROW_LEFT)
        text_field.send_keys(booking_date_formatted)

        # Select the route
        route_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "ddlRoute"))))
        route_dropdown.select_by_visible_text(DESIRED_PATH)
        time.sleep(1)

        # Select the timing
        timing_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "ddlTiming"))))
        timing_dropdown.select_by_visible_text(booking_time)
        time.sleep(1)

        # Select the bus
        bus_dropdown = Select(wait.until(EC.presence_of_element_located((By.ID, "ddlBus"))))
        bus_dropdown.select_by_index(1)

        # Select a seat
        seat_number = None
        for i in range(1, 31):
            seat_id = f"checkbox{i}"
            seat_element = wait.until(EC.presence_of_element_located((By.ID, seat_id)))
            if is_focusable(driver, seat_element):
                seat_element.click()
                seat_number = i  # Record the seat number
                break

        if seat_number is None:
            raise Exception("No available seat was found.")

        # Submit the booking
        wait.until(EC.presence_of_element_located((By.ID, "lnkSave"))).click()

        # Send a confirmation email
        email_message = (
            f"Your bus booking is successful!\n\n"
            f"Details:\n"
            f"- Date: {booking_date}\n"
            f"- Route: {DESIRED_PATH}\n"
            f"- Time: {booking_time}\n"
            f"- Seat Number: {seat_number}\n\n"
            f"Safe travels!"
        )
        send_email("Bus Booking Successful", email_message)
        print("Booking successful! Confirmation email sent.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


# Function to send email notifications
def send_email(subject, message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = EMAIL

        # Send email using SMTP
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, EMAIL_PASSWORD)
            server.sendmail(EMAIL, EMAIL, msg.as_string())
        print("Notification email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")


# Function to schedule the booking
def schedule_booking(booking_date, booking_time):
    """Schedule the booking process."""
    try:
        # Convert booking time from AM/PM to 24-hour format
        booking_time_24hr = datetime.datetime.strptime(booking_time, "%I:%M %p").strftime("%H:%M")

        # Combine booking date and time into a single datetime object
        booking_datetime = datetime.datetime.strptime(f"{booking_date} {booking_time_24hr}", "%Y-%m-%d %H:%M")
        current_time = datetime.datetime.now()

        # Calculate the 15 days before the booking date
        schedule_time = booking_datetime - datetime.timedelta(days=15)

        if current_time < schedule_time:
            # Schedule the booking for 15 days before the booking date
            print(f"Scheduling booking for: {schedule_time}")
            scheduler = BlockingScheduler()
            scheduler.add_job(book_seat, 'date', run_date=schedule_time, id='booking_job')
            scheduler.start()
            print(f"Booking scheduled. Will execute at {schedule_time}.")
        else:
            # Book immediately if within 15 days
            print("Booking now as it's within 15 days of the booking date.")
            book_seat()

    except ValueError as e:
        print(f"Error in date or time format: {e}")


# Input parameters and main execution
if __name__ == "__main__":
    try:
        booking_date = input("Enter the booking date (YYYY-MM-DD): ")
        booking_time = input("Enter the booking time (e.g., 10:00 AM or 03:00 PM): ")

        # Schedule or book now
        schedule_booking(booking_date, booking_time)

    except Exception as e:
        print(f"Unexpected error: {e}")
