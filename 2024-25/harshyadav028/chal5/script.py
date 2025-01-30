# all neccesary import
import os
import time
import schedule
import re
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# load enviroment variables
load_dotenv()

LDAP_USERNAME = os.getenv("LDAP_USERNAME")
LDAP_PASSWORD = os.getenv("LDAP_PASSWORD")

# bus_booking_email_confirmation function
def confirmation_email_sender(details):
    # sender email credentials
    sender_email="harshyadav110406@gmail.com"
    password="qowr kwnq sbim dfrz"

    # connect to gmail SMTP server 
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,password)

    # sender and reciever email
    reciever_email="harsh110406@gmail.com"

    # subject and body of email
    subject = "Bus Booking Comfirmation ;)"
    body = f"""Bus Booked Succesfully!
    Details: 
    {details}
    """

    #create the message
    message=MIMEMultipart()
    message["From"]=sender_email
    message["To"]=reciever_email
    message["Subject"]=subject
    message.attach(MIMEText(body,"plain"))

    #send...
    server.sendmail(sender_email,reciever_email,message.as_string())

    #quit server
    server.quit()
# function to automate booking

# function to select date from calender
# def select_date_from_calendar(driver, target_date):
#     # Parse the target date into day, month, and year
#     day, month, year = target_date.split("/")

#     # Click the date input to open the calendar
#     date_input = driver.find_element(By.ID, "txtFromDate")
#     date_input.click()
#     # Allow the calendar to load
#     time.sleep(2)

#     # select the day
#     calendar_days = driver.find_elements(By.CLASS_NAME, "ajax__calendar_day")
#     for calendar_day in calendar_days:
#         if calendar_day.text == day:
#             calendar_day.click()
#             break

# tried set up months selecting script
# modified function for mon the choosing also and handled some errors like format of date etc.
# function to select date from calender

def select_date_from_calendar(driver, target_date):
    try:
        # Validate date format (DD/MM/YYYY)
        if not re.match(r"^\d{2}/\d{2}/\d{4}$", target_date):
            raise ValueError("target_date must be in 'DD/MM/YYYY' format.")

        # Parse the target date
        day, month, year = target_date.split("/")
        month_int = int(month)

        # Click the date input to open the calendar
        date_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "txtFromDate"))
        )
        date_input.click()
        time.sleep(2)  # Allow the calendar to load

        # Click the navigation arrow to reach the correct month
        for _ in range(month_int - 1):  
            arrow_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "C1_nextArrow"))
            )
            arrow_input.click()
            time.sleep(1)  # Allow UI to update

        # Wait and re-fetch the calendar days to avoid StaleElementReferenceException
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "ajax__calendar_day"))
        )

        calendar_days = driver.find_elements(By.CLASS_NAME, "ajax__calendar_day")
        for calendar_day in calendar_days:
            if calendar_day.text == day:
                calendar_day.click()
                return  # Exit after selecting the date

        raise Exception(f"Day '{day}' not found in the calendar.")

    except TimeoutException:
        print("Error: Calendar elements did not load in time.")
    except StaleElementReferenceException:
        print("Error: The calendar refreshed, retrying...")
        select_date_from_calendar(driver, target_date)  # Retry function on stale element
    except Exception as e:
        print(f"An error occurred: {e}")

def mapping(booking_details):
    route = booking_details["route"]
    t_index = booking_details["timing_index"]

    # Define timings for each route
    timings_map = {}

    if route == "North Campus -To- Mandi (via South)":
        timings_map = {
            1: "7:00 AM",
            2: "9:00 AM",
            3: "11:00 AM",
            4: "2:00 PM",
            5: "4:00 PM",
            6: "4:00 PM",
            7: "5:40 PM",
            8: "6:00 PM",
            9: "7:00 PM",
            10: "8:00 PM",
        }

    elif route == "Mandi -To- North Campus (via South)":
        timings_map = {
            1: "7:00 AM",
            2: "8:00 AM",
            3: "10:00 AM",
            4: "12:00 PM",
            5: "3:15 PM",
            6: "5:00 PM",
            7: "7:40 PM",
            8: "8:00 PM",
            9: "9:00 PM",
        }

    elif route == "North Campus -To- Mandi (via South) (Special)":
        timings_map = {
            1: "5:40 PM",
        }

    # Validate if the timing index exists
    if t_index not in timings_map:
        raise KeyError(f"Invalid timing index {t_index} for route '{route}'")

    # Assign mapped time
    booking_details["timing_index"] = timings_map[t_index]

def automate_booking():
    print("starting the booking proccess")

    booking_details = {
        "date": "12/02/2025",
        "route": "North Campus -To- Mandi (via South)",
        "timing_index": 1,
        "bus_index": 1,
        "seat_no":20,
    }


    
    # set up selenium web driver
    driver = webdriver.Chrome() # set up chrome web driver
    driver.get("https://oas.iitmandi.ac.in/InstituteProcess/Common/Login.aspx") # driver with open the provided link

    # login proccess secretly 
    driver.find_element(By.ID, "txtLoginId").send_keys(LDAP_USERNAME)
    driver.find_element(By.ID, "txtPassword").send_keys(LDAP_PASSWORD)
    driver.find_element(By.ID, "btnLogin").click()

    # wait for the page to relaod
    time.sleep(5) # sleep for 5s

    # navigating to bus booking url
    print("navigating to booking page")
    driver.get("https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx")

    # wait for the page to relaod
    time.sleep(5) # sleep for 5s

    # fill booking details
    print("filling booking details")

    # Travel date
    select_date_from_calendar(driver, "12/02/2025") 

    # Explicitly wait for the field to be populated or validated
    time.sleep(3)

    # route
    route_select = Select(driver.find_element(By.ID, "ddlRoute"))
    route_select.select_by_visible_text(booking_details["route"])

    # wait for rout option to load
    time.sleep(3)

    # schedule
# Wait for the `ddlTiming` dropdown to populate
    print("Waiting for schedule timing options to load...")
    try:
        timing_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ddlTiming"))
        )
        timing_select = Select(timing_element)

        # Wait until options are available
        WebDriverWait(driver, 10).until(lambda d: len(timing_select.options) > 1)

        # Select timing
        timing_select.select_by_index(booking_details["timing_index"])
        print("Schedule timing selected successfully!")

    except Exception as e:
        print(f"Error selecting schedule timing: {e}")
        driver.quit()
        return


 # Select Bus
    print("Selecting bus...")
    try:
        # Continuously re-locate the element to handle stale references
        bus_select = None

        # Retry logic for stale element reference
        for _ in range(3):  # Try up to 3 times
            try:
                # Wait until the dropdown is present in the DOM
                bus_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "ddlBus"))
                )

                # Reinitialize Select object
                bus_select = Select(bus_element)

                # Wait until the dropdown has at least one option
                WebDriverWait(driver, 10).until(lambda d: len(bus_select.options) >= 1)

                # Select the desired bus by index
                bus_select.select_by_index(booking_details["bus_index"])
                print("Schedule bus selected successfully!")
                break  # Exit loop if successful

            except StaleElementReferenceException:
                print("Stale element reference detected. Retrying...")

        if not bus_select:  # If bus_select is still None after retries
            raise Exception("Failed to locate bus dropdown after retries.")

    except Exception as e:
        print(f"Error selecting schedule bus: {e}")
        driver.quit()
        return

    # select the seat
    try:
        seat_string_id = f"checkbox{booking_details['seat_no']}"
        print(seat_string_id)
        select_seat = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, seat_string_id))
        )
        print("Seat element found!")
        select_seat.click()
    except TimeoutException:
        print(f"Seat with ID {seat_string_id} was not found within the timeout.")
        driver.quit()
        return


    #wait for 2s
    time.sleep(2)

    # saving the bus booking
    save_button = driver.find_element(By.ID, "lnkSave")
    save_button.click()

    # wait for confirmation by the website
    time.sleep(3)

    # alert close up
    alert = Alert(driver)
    alert_text = alert.text # Extract the alert text
    print(f"Alert msg: {alert_text}")
    alert.accept() # Close the alert popup

    mapping(booking_details)
    # creating conformation details
    confirmation_details = {
        "date": booking_details["date"],
        "route": booking_details["route"],
        "timing": f"{booking_details['timing_index']}",
        "bus": f"Bus Index {booking_details['bus_index']}",
        "seat_no": booking_details["seat_no"],
        "alert_message": alert_text,
    }
    print("Booking Successful", confirmation_details)

    # send confirmation e