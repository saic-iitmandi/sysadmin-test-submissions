from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import os
import time
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()
# Timing mapping (value to timing)
TIMING_MAPPING = {
    "8": "7:00 AM",
    "6": "8:00 AM",
    "22": "9:00 AM",
    "10": "10:00 AM",
    "11": "11:00 AM",
    "12": "12:00 PM",
    "2": "4:00 PM",
    "3": "2:00 PM",
    "4": "3:00 PM",
    "1033": "3:15 PM",
    "15": "4:00 PM",
    "16": "5:00 PM",
    "1032": "5:40 PM",
    "7": "6:00 PM",
    "1022": "7:00 PM",
    "1024": "8:00 PM",
    "1025": "9:00 PM",
}

# Route mapping
VALID_ROUTES = [
    "North Campus -To- Mandi (via South)",
    "Mandi -To- North Campus (via South)",
    "North Campus -To- Mandi (Direct)"
]






def run(date: str, timing: str, route: str):
    """
    Automates the bus booking process.

    Args:
        date (str): The desired date for booking in 'DD/MM/YYYY' format.
        timing (str): The desired timing as a string (e.g., "5:00 PM").
        route (str): The desired route as a string (e.g., "North Campus -To- Mandi (via South)").
    """
    login_id = os.getenv("LOGIN_ID")
    password = os.getenv("PASSWORD")
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")
        # Validate the route
    if route not in VALID_ROUTES:
        print(f"Invalid route: {route}. Please choose from: {VALID_ROUTES}")
        return

    # Find the corresponding timing value
    timing_value = None
    for value, time_label in TIMING_MAPPING.items():
        if time_label == timing:
            timing_value = value
            break

    if not timing_value:
        print(f"Invalid timing: {timing}. Please choose from: {list(TIMING_MAPPING.values())}")
        return

    # Set up WebDriver
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)

    try:
        # Open the website
        driver.get("https://oas.iitmandi.ac.in/InstituteProcess/Common/Login.aspx")
        time.sleep(5)

        # Maximize the browser window
        driver.maximize_window()
       

        # Login credentials (use environment variables for security)
        LOGIN_ID = os.getenv("LOGIN_ID")  # Default fallback
        PASSWORD = os.getenv("PASSWORD")

        # Enter username
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtLoginId")))
        element.send_keys(LOGIN_ID)
        time.sleep(5)

        # Enter password
        element = driver.find_element(By.ID, "txtPassword")
        element.send_keys(PASSWORD)
        time.sleep(5)

        # Submit the form
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnLogin")))
        button.click()
        time.sleep(5)

        # Wait for the page to load and switch to the bus reservation page
        WebDriverWait(driver, 10).until(EC.url_changes("https://oas.iitmandi.ac.in/InstituteProcess/Common/Login.aspx"))
        driver.get("https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx")
        time.sleep(5)

        # Select the date
        date_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtFromDate")))
        driver.execute_script(f"arguments[0].value = '{date}'; arguments[0].dispatchEvent(new Event('change'));", date_input)
        time.sleep(5)

        # Wait for the route dropdown to be present and select the route
        route_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ddlRoute")))
        select_route = Select(route_dropdown)
        select_route.select_by_visible_text(route)
        time.sleep(5)
        print(f"Selected route: {route}")

        # Wait for the timing dropdown to populate after route selection
        timing_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ddlTiming")))
        select_timing = Select(timing_dropdown)

        # Select timing by its value
        select_timing.select_by_value(timing_value)
        time.sleep(10)
        print(f"Selected timing: {timing} successfully.")

        # Select any available bus
        bus_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ddlBus")))
        select_bus = Select(bus_dropdown)
        bus_options = select_bus.options

        if len(bus_options) > 1:  # Ensure there's at least one bus available (excluding default)
            select_bus.select_by_index(1)  # Select the first available bus option
            bus_option=bus_options[1].text
            print(f"Selected bus: {bus_options[1].text}")
        else:
            print("No buses available for the selected timing.")
        time.sleep(5)

        # Select the first available checkbox
        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and not(@disabled)]")
        if checkboxes:
            checkboxes[0].click()
            chbox=checkboxes[0].get_attribute('id')
            print(f"Selected checkbox with ID: {checkboxes[0].get_attribute('id')}")
        else:
            print("No available checkboxes to select.")
        time.sleep(5)

        # Click the save button
        element = driver.find_element(By.ID, "lnkSave")
        element.click()
        time.sleep(5)
        alert=Alert(driver)
        alert.accept()



        time.sleep(1)

        # Send an email notification
        smtp_server = "smtp.gmail.com"  # For Gmail, use smtp.gmail.com
        smtp_port = 587  # Port number for TLS
     

        # Create the email
        subject = "BUS BOOKING DETAILS"
        body = "successfully booked the seat\n" + "Booking details:\n" +"Seat No.:"+chbox[8:] +"\nBus Name:"+bus_option +"\nTiming:"+timing +"\nRoute:"+route +"\nDate:"+date
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        # Send the email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, sender_password)
                server.send_message(message)
                print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}") 
        print("Booking saved successfully.")



        

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # close the browser
        print("Script execution completed. Browser will remain open.")
        driver.quit()


        




timing_data = [
    {"value": 8, "timing": "7:00 AM", "routes": [1, 1, 0]},
    {"value": 6, "timing": "8:00 AM", "routes": [0, 1, 0]},
    {"value": 22, "timing": "9:00 AM", "routes": [1, 0, 0]},
    {"value": 10, "timing": "10:00 AM", "routes": [0, 1, 0]},
    {"value": 11, "timing": "11:00 AM", "routes": [1, 0, 0]},
    {"value": 12, "timing": "12:00 PM", "routes": [0, 1, 0]},
    {"value": 3, "timing": "2:00 PM", "routes": [1, 0, 0]},
    {"value": 4, "timing": "3:00 PM", "routes": [0, 1, 0]},
    {"value": 1033, "timing": "3:15 PM", "routes": [0, 1, 0]},
    {"value": 15, "timing": "4:00 PM", "routes": [1, 0, 0]},
    {"value": 2, "timing": "4:00 PM", "routes": [1, 0, 0]},
    {"value": 16, "timing": "5:00 PM", "routes": [1, 1, 0]},
    {"value": 1032, "timing": "5:40 PM", "routes": [0, 0, 1]},
    {"value": 7, "timing": "6:00 PM", "routes": [1, 0, 0]},
    {"value": 1022, "timing": "7:00 PM", "routes": [1, 1, 0]},
    {"value": 1024, "timing": "8:00 PM", "routes": [1, 1, 0]},
    {"value": 1025, "timing": "9:00 PM", "routes": [0, 1, 0]},
    ]
route=["North Campus -To- Mandi (via South)","Mandi -To- North Campus (via South)","North Campus -To- Mandi (Direct)"]
date=input("Enter the date in 'DD/MM/YYYY' format: ")
route_choice = int(input("Enter the route number (1, 2, or 3): "))
available_timings = [t for t in timing_data if t["routes"][route_choice - 1] == 1]

if not available_timings:
    print("No timings available for the selected route. Exiting.")


# Display available timings
print("\nAvailable timings for the selected route:")
for t in available_timings:
    print(f"{t['value']}: {t['timing']}")
# Get user input for timing
timing_choice = int(input("Enter the timing value from the list above: "))

if timing_choice not in [t["value"] for t in available_timings]:
    print("Invalid timing choice. Exiting.")

x=run(date,TIMING_MAPPING[str(timing_choice)],route[route_choice-1])
print(x)
