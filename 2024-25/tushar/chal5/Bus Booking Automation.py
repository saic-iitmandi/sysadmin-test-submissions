import os #for environment variables
import time
from datetime import datetime #for scheduling
from apscheduler.schedulers.background import BackgroundScheduler #for scheduling
from selenium import webdriver #for web automation
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv #for environment variables
import smtplib #for email notification
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
RETRY_INTERVAL = 3600  # 5 minutes
# Load environment variables
load_dotenv(dotenv_path=r"D:\SYSAdmin\.env")

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
USERNAME= os.getenv("LDAP_USERNAME")
BOOKING_PASSWORD= os.getenv("LDAP_PASSWORD")
BOOKING_URL = "https://oas.iitmandi.ac.in/InstituteProcess/Common/Login.aspx"

# Booking parameters
booking_date = "2025-01-30"  # Desired date
# Format the date to MM/DD/YYYY (or check the expected format of the input field)
booking_time = "07:00 AM"
bus_path = "North Campus -To- Mandi (via South)"

# Email notification function
def send_email_notification(status):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = EMAIL
        msg["Subject"] = "Bus Booking Confirmation"

        body = f"Booking Status: {status}\nPath: {bus_path}\nDate & Time: {booking_date} {booking_time}"
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, EMAIL, msg.as_string())
        print("Notification sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# send_email_notification("status")
def safe_select_time(driver):
    retries = 3
    while retries > 0:
        try:
            # Re-locate the time dropdown element
            time_dropdown = Select(driver.find_element(By.ID, "ddlTiming"))
            
            # Try selecting the desired time
            time_dropdown.select_by_visible_text(booking_time)
            print(f"Successfully selected time: {booking_time}")
            return True
        except Exception as e:
            print(f"Error selecting time: {e}")
            retries -= 1
            time.sleep(1)  # Wait before retrying
    return False

# Safe Select Function to Handle Stale Element Reference (Extended to Handle ddlBus)
# def safe_select_bus(driver):
    retries = 3
    while retries > 0:
        try:
            # Re-locate the bus dropdown element
            bus_dropdown = Select(driver.find_element(By.ID, "ddlBus"))
            
            # Select the desired bus (For now, we select the first option, you can change it)
            bus_dropdown.select_by_index(0)
            print("Successfully selected bus.")
            return True
        except Exception as e:
            print(f"Error selecting bus: {e}")
            retries -= 1
            time.sleep(1)  # Wait before retrying
    return False

def safe_select_bus(driver):
    retries = 3
    while retries > 0:
        try:
            # Re-locate the bus dropdown element
            bus_dropdown = Select(driver.find_element(By.ID, "ddlBus"))
            
            # Select the desired bus (BUS(E) in this case)
            # bus_dropdown.select_by_index(0)
            bus_dropdown.select_by_visible_text("BUS(E)")  # Change "BUS(E)" to the bus name you need

            # Trigger the onchange event using JavaScript
            driver.execute_script("arguments[0].onchange();", bus_dropdown)
            
            print("Successfully selected bus.")
            
            # Check for the alert and accept it if it appears
            try:
                WebDriverWait(driver, 2).until(EC.alert_is_present())
                alert = driver.switch_to.alert
                print(f"Alert Text: {alert.text}")
                alert.accept()
                print("Alert accepted.")
            except:
                print("No alert detected.")
            
            return True
        except Exception as e:
            print(f"Error selecting bus: {e}")
            retries -= 1
            time.sleep(1)  # Wait before retrying
    return False

# Function to select an available seat
def select_seat(driver):
    retries = 3
    while retries > 0:
        try:
            # Locate all seat checkboxes (available and unavailable) with an ID that starts with "checkbox"
            checkboxes = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//input[@type='checkbox' and starts-with(@id, 'checkbox')]"))
            )

            # Loop through all checkboxes to find the first available seat
            for checkbox in checkboxes:
                # Check if the checkbox is enabled and not already checked
                if checkbox.is_enabled() and not checkbox.is_selected():
                    # Scroll into view to ensure visibility
                    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)

                    # Click the checkbox using JavaScript
                    driver.execute_script("arguments[0].click();", checkbox)

                    # Confirm the seat was selected
                    print(f"Seat selected: {checkbox.get_attribute('id')}")

                    # Wait for the save button to become clickable
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "lnkSave")))

                    # Re-locate and click the save button
                    save_button = driver.find_element(By.ID, "lnkSave")
                    driver.execute_script("arguments[0].click();", save_button)
                    print("Booking confirmed.")

                    # Send email notification
                    send_email_notification("Success")
                    return True

            # If no available seat was found, log and return
            print("No seat available.")
            return False

        except Exception as e:
            print(f"Error selecting seat: {e}")
            retries -= 1
            time.sleep(1)  # Wait before retrying

    # If all retries are exhausted, return False
    return False

# Booking function
def book_seat():
    try:
        print("Starting booking process...")
        driver = webdriver.Chrome()  # Make sure the ChromeDriver is in PATH
        driver.get(BOOKING_URL)

        # Wait for login page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtLoginId")))
        time.sleep(1)  # Add before sending credentials

        driver.find_element(By.ID, "txtLoginId").send_keys(USERNAME)
        driver.find_element(By.ID, "txtPassword").send_keys(BOOKING_PASSWORD)

        driver.find_element(By.ID, "btnLogin").click()  # Replace with the correct button ID
        print("Login submitted. Waiting for navigation...")
        
        SEAT_BOOKING_URL = "https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx"
        driver.get(SEAT_BOOKING_URL)
        
        # Wait for Travel Date input and Route Schedule dropdown to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtFromDate")))  # Assuming ID for Travel Date
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ddlRoute")))  # Assuming ID for Route Schedule dropdown
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ddlTiming")))
        # Fill Travel Date (Assume the element is an input field of type 'date')
        travel_date = driver.find_element(By.ID, "txtFromDate")  # Replace with actual ID
        # Fill Travel Date using JavaScript to set the value directly
        formatted_date = datetime.strptime(booking_date, "%Y-%m-%d").strftime("%d/%m/%Y")  # Adjust format here if needed
        driver.execute_script(f"document.getElementById('txtFromDate').value = '{formatted_date}'")


        route_dropdown = Select(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ddlRoute"))
        ))

        # Print available options for debugging
        print("Available Routes:")
        for option in route_dropdown.options:
            print(option.text)
        route_dropdown.select_by_visible_text(bus_path)

        print("Travel Date and Route Schedule filled.")

        # Use the safe_select_time function to select the time
        if not safe_select_time(driver):
            print("Failed to select time after multiple attempts.")
        

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ddlBus")))
        # Use the safe_select_bus function to select the bus
        if not safe_select_bus(driver):
            print("Failed to select bus after multiple attempts.")

        # Select available seat
        if not select_seat(driver):
            print("No available seat found.")
        # Additional steps for confirming booking can be added here

        driver.quit()    
    except Exception as e:
        print(f"Booking failed: {e}")
        send_email_notification("Failed")

# book_seat()
# Monitor and book seats
def monitor_and_book():
    # driver = webdriver.Chrome()
    while True:
        if book_seat():
            print("Seat booked successfully. Exiting monitoring.")
            # driver.quit()
            break
        print(f"Retrying in {RETRY_INTERVAL // 60} minutes...")
        time.sleep(RETRY_INTERVAL)  # Wait before retrying

# Start monitoring
monitor_and_book()
# Scheduler function to trigger booking at the specified time
# def schedule_booking():
#     # Parse the desired booking date and time
#     booking_datetime = datetime.strptime(f"{booking_date} {booking_time}", "%Y-%m-%d %I:%M %p")

#     # Check if the desired time is in the future
#     now = datetime.now()
#     if booking_datetime <= now:
#         print("The booking time must be in the future!")
#         return

#     # Schedule the booking process
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(book_seat, 'date', run_date=booking_datetime)
#     scheduler.start()

#     # Print confirmation of the scheduled job
#     print(f"Booking scheduled for {booking_datetime.strftime('%Y-%m-%d %I:%M %p')}. Waiting for the time...")

#     # Keep the script running to allow the scheduler to execute
#     try:
#         while True:
#             time.sleep(1)
#     except (KeyboardInterrupt, SystemExit):
#         scheduler.shutdown()
#         print("Scheduler stopped.")

# Run the scheduler
# if __name__ == "__main__":
#     schedule_booking()
        # WebDriverWait(driver, 5).until(EC.alert_is_present())
                # Check for alerts
        # try:
        #     WebDriverWait(driver, 5).until(EC.alert_is_present())
        #     alert = driver.switch_to.alert
        #     print(f"Alert Text: {alert.text}")
        #     alert.accept()  # Accept alert if present
        #     print("Alert dismissed.")
        # except:
        #     print("No alert detected.")
                # Wait for the sidebar menu to load
                # Wait for the sidebar menu to load and expand Quick Links 