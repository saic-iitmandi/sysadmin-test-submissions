# importing selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

# Define URLs
loginPage = "https://oas.iitmandi.ac.in/InstituteProcess/Common/Login.aspx"
seatBookingPage = "https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx"

load_dotenv()

# Credentials
username = os.getenv("LDAPUSERNAME")
password = os.getenv("LDAPPASSWORD")

seatBooked = False
# Target date components
target_day = "12"
target_month = "February" # month in format 'February', 'January' etc.
target_year = "2025" # year in numerics
route = 'North Campus -To- Mandi (via South)'
# routes are ['Mandi -To- North Campus (via South)', 'North Campus -To- Mandi (via South)', '	North Campus -To- Mandi (Direct)']
bookTime = '07:00 PM' # format is 'hour:minute am/pm'

# calculating the delta
bookingDate = datetime.strptime(f"{target_day} {target_month} {target_year} {bookTime}", "%d %B %Y %I:%M %p")
openDate = bookingDate - timedelta(days=15)
timeDiff = (openDate - datetime.now()).total_seconds()
if(timeDiff > 0):
    time.sleep(timeDiff) # sleeping until the portal opens

# setting up chrome
driver = webdriver.Chrome()

# Logging in and going to seat booking page
try:
    driver.get(loginPage)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "txtLoginId"))).send_keys(username) # giving a 60s buffer
    driver.find_element(By.NAME, "txtPassword").send_keys(password, Keys.RETURN)
    print("Logged in successfully.")
    time.sleep(1) # allowing the website to load.
except Exception as e:
    print("Login failed:", e)
    driver.quit()

try:
    driver.get(seatBookingPage)
    time.sleep(1) # allowing page to load
except Exception as e:
    print("Couldn't go to seat booking page:", e)
    driver.quit()

# selecting the date
try:
    date_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "txtFromDate"))
    )
    date_field.click()

    # waiting for calender to load
    calendar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ajax__calendar"))
    )
    
    # looping to go to the correct page.
    while True:
        calenderTitle = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ajax__calendar_title"))
        )
        if target_month in str(calenderTitle.text) and target_year in str(calenderTitle.text):
            break
        next_button = calendar.find_element(By.CLASS_NAME, "ajax__calendar_next")
        next_button.click()
        time.sleep(1)  # waiting for calender to refresh
        
    day_elements = calendar.find_elements(By.CLASS_NAME, "ajax__calendar_day")
    monthStart = False
    for day_element in day_elements:
        day_text = day_element.text.strip()
        if monthStart and day_text == '1':
            break
        if day_text == '1':
            monthStart = True

        if day_text == target_day and monthStart:
            day_element.click()
            print(f"Date successfully selected: {target_day} {target_month} {target_year}")
            break
except Exception as e:
    print("Error selecting date:", e)
    driver.quit()

# selecting the route  
try:
    route_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ddlRoute")))
    route_dropdown.click()
    time.sleep(1)  # Wait for dropdown options to load
    route_dropdown.find_element(By.XPATH, f"//option[text()='{route}']").click()
    print("Date and route selected.")
    time.sleep(2)
except Exception as e:
    print("Date and route selection failed:", e)
    driver.quit()

# selecting the time
try:
    time_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ddlTiming"))
    )
    time_dropdown.click()
    time.sleep(1)

    options = time_dropdown.find_elements(By.TAG_NAME, "option")
    selected = False

    for option in options:
        if " ".join(option.text.split()) == " ".join(bookTime.split()):
            option.click()
            print(f"Time selected: {option.text}")
            selected = True
            break

    if not selected:
        print(f"Time '{bookTime}' not found in the dropdown options.")

    time.sleep(2)
except Exception as e:
    print("Time selection failed:", e)
    driver.quit()


lastBusText = ''
seatID = -1
# selecting the last bus in the list
try:
    busDropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ddlBus"))
    )
    busDropdown.click()
    time.sleep(1) # Wait for dropdown options to load

    # Get all bus options
    buses = WebDriverWait(driver, 10).until(
        lambda d: busDropdown.find_elements(By.TAG_NAME, "option")
    )
    
    if len(buses) > 1: # ignoring the 'Select' default option.
        lastBus = buses[-1]
        lastBus.click()
        lastBusText = lastBus.text
        print(f"Last Bus ID selected: {lastBus.text}")
    else:
        print("No valid options found in the bus dropdown.")
except Exception as e:
    print("Bus ID selection failed:", e)

# selecting the seat which is available
try:
    seats = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//input[starts-with(@id, 'checkbox') and not(@disabled)]"))
    )
    if seats:
        seats[0].click()
        print(f"Seat {seats[0].get_attribute('id')} selected successfully.")
        seatID = seats[0].get_attribute('id').split('checkbox')[1]
        save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "lnkSave")))
        while True:
            save_button.click()
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            if alert.text == 'Selected seat successfully booked.':
                print("Seat booking saved successfully.")
                seatBooked = True
                alert.accept()
                break
            else:
                if alert.text == 'Travel date and time is not as per rule.':
                    print('Couldnt book')
                    alert.accept()
    else:
        print("No available seats to select.")
        raise(Exception("No available seats to select."))
except Exception as e:
    print("Seat booking failed:", e)
finally:
    driver.quit()

senderEmail = os.getenv("SENDEREMAIL")

if seatBooked:
    # setting up the email
    subject = "Bus Seat Successfully Booked"
    body = f"""Your bus seat has been successfully booked with the following details:
    - Date: {target_day} {target_month} {target_year}
    - Time: {bookTime}
    - Route: {route}
    - Bus ID: {lastBusText}
    - Seat ID: {seatID}"""

    sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    fromEmail = Email(senderEmail)
    toEmail = To(f'{os.getenv('LDAPUSERNAME')}@students.iitmandi.ac.in')
    content = Content("text/plain", body)

    mail = Mail(fromEmail, toEmail, subject, content)

    try:
        response = sg.send(mail)
        print(f"Email sent successfully! Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")