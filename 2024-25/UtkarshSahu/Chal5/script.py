from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import time
import yagmail
from datetime import datetime

# Load environment variables
load_dotenv()


mydate = ""
myroute = ""
mytime = ""


mydate = input("Enter date in ddmmyyyy\n")

myroute = int(input("Press:\n1 - North Campus to Mandi (via south)\n2 - Mandi to North Campus (via south)\n3 - North Cmapus to Mandi direct\n"))
while not( (myroute > 0) and (myroute < 4) ):
    myroute = int(input("Enter valid input"))
if(myroute == 3):
    myroute = 7
# mytime = input("Enter the option number according to your time")
mytime = input("Enter the time\n")

date_object = datetime.strptime(mydate, "%d%m%Y")
time_object = datetime.strptime(mytime, "%I:%M %p").time()
combined_datetime = datetime.combine(date_object, time_object)

scheduled_time = True
if(combined_datetime - timedelta(days=15) > datetime.now()):
    scheduled_time = combined_datetime - timedelta(days=15)
# print(scheduled_time)
mydate = mydate[0]+mydate[1]+"/"+mydate[2]+mydate[3]+"/"+mydate[4:8]
# print(scheduled_time)



# Get variables
username = os.getenv("MY_USERNAME")
password = os.getenv("MY_PASSWORD")
chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
# login_url = os.getenv("LOGIN_URL")
emailId = os.getenv("MY_EMAIL")
appPass = os.getenv("APP_PASSWORD")
login_url = 'https://oas.iitmandi.ac.in/InstituteProcess/Common/Login.aspx'


def send_mail():
    yag = yagmail.SMTP(emailId, appPass) 
    yag.send(
        to="b24172@students.iitmandi.ac.in",
        subject="Bus Booking",
        contents="Your Bus has been booked successfully"
    )
    print("Bus booked")

def run_script():
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    try:
        
        driver.get(login_url)

        # Log in
        driver.find_element(By.ID, "txtLoginId").send_keys(username)
        driver.find_element(By.ID, "txtPassword").send_keys(password)
        driver.find_element(By.ID, "btnLogin").click()

        

        driver.get("https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx")
        
        # driver.find_element(By.ID, "txtFromDate").send_keys(a)
        input_date = driver.find_element(By.ID, "txtFromDate")
        driver.execute_script("arguments[0].value = arguments[1];", input_date, mydate)

        routeDrop = Select(driver.find_element(By.ID, "ddlRoute"))
        # dropdown.select_by_visible_text(myroute)
        routeDrop.select_by_value(str(myroute))

        time.sleep(2)
        timeDrop = Select(driver.find_element(By.ID, "ddlTiming"))
        timeDrop.select_by_visible_text(mytime)
        # timeDrop.select_by_value(mytime)

        time.sleep(2)
        busDrop = Select(driver.find_element(By.ID, "ddlBus"))
        busDrop.select_by_index(1)

        time.sleep(4)
        for i in range (1,30):
            seatCheck = driver.find_element(By.ID, f"checkbox{i}")
            if seatCheck.is_selected():
                continue
            else:
                seatCheck.click()
                break
        time.sleep(4)
        driver.find_element(By.ID, "lnkSave").click()

    finally:
        send_mail()
        time.sleep(2)
        driver.quit()
        schedular.shutdown(wait=False)
        # print("hello")

# def run_script():
#     print("Hello World")
#     schedular.shutdown()
# run_script()

schedular = BlockingScheduler()
# schedular.add_job(run_script, 'date', scheduled_time)
schedular.add_job(run_script, 'date', run_date = datetime.now() if scheduled_time == True else scheduled_time)
print("Before schedular")
schedular.start()
print("After Schedular")