import pwinput 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=r"C:\Users\shiva\OneDrive\Documents\WebScrapping\credential.env")
booked = False
def send_email(from_email,body,EMAIL_PASS):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = "b24159@students.iitmandi.ac.in"
        msg["Subject"] = "BUS BOOKED!!"
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() 
        server.login(from_email, EMAIL_PASS)

        server.sendmail(from_email,EMAIL_PASS, msg.as_string())
        server.quit()

        print(f"Email sent successfully to b24159@students.iitmandi.ac.in!")

    except Exception as e:
        print(f"Error: {e}")
def BookTicket(input_date,input_time,input_route,user_name,user_pass,selected_bus):
    loginurl = "https://oas.iitmandi.ac.in/InstituteProcess/Common/Login.aspx"
    reservationurl = "https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx"
    driver = webdriver.Edge()
    driver.get(loginurl)
    Ldapu = driver.find_element(By.NAME, 'txtLoginId')
    Ldapu.clear()
    Ldapu.send_keys(user_name)
    LdapP = driver.find_element(By.NAME,'txtPassword')
    LdapP.clear()
    LdapP.send_keys(user_pass)
    Log_in = driver.find_element(By.NAME,"btnLogin")
    Log_in.click()
    driver.get(reservationurl)

    try:
        time.sleep(5)
        date_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'txtFromDate'))
        )
        date_field.click()
        day_elements = driver.find_elements(By.CLASS_NAME,"ajax__calendar_day")
        for day in day_elements:
            if input_date.split(" ")[0] in day.text and input_date.split(" ")[1] in day.get_attribute('title'):
                day.click()

        time.sleep(1)
        route = driver.find_element(By.ID, 'ddlRoute')  
        route.click()
        select = Select(route)
        select.select_by_visible_text(input_route)
        time.sleep(1)
        
        dropdown_element = driver.find_element(By.ID, 'ddlTiming')
        dropdown_element.click()
        time.sleep(1)
        time_elements = driver.find_elements(By.XPATH,f'//option[contains(@title, AM)]')
        for ele in time_elements:
            if ele.text==input_time:
                ele.click()     
        time.sleep(1)

        Bus_elements = driver.find_element(By.ID, 'ddlBus')
        Bus_elements.click()
        time.sleep(2)
        buses = driver.find_elements(By.XPATH,f'//option[contains(@title, BUS)]')
        for bus in buses:
            if bus.text == selected_bus:
                bus.click()
        time.sleep(4)
        seat_no = 0
        for i in range(1,31):    
            try:
                busSeat = driver.find_element(By.ID,f"checkbox{i}")
                is_disabled = busSeat.get_attribute("disabled")
                if not is_disabled:
                    busSeat.click()  
                    seat_no = i  
                    break                
            except NoSuchElementException:
                continue
        time.sleep(2)
        
        saveButton = driver.find_element(By.ID,"lnkSave")
        saveButton.click()
        booked  = True
        send_email(os.getenv("EMAIL"),f'''
                    Your Bus has been booked!
                    date : {traveldate}
                    time : {traveltime}
                    route : {route}
                    seat :  {seat_no}
                    Enjoy the journey!!
                        ''',os.getenv("EMAIL_PASSWORD"))


                

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
useremail = os.getenv("EMAIL")
email_password = os.getenv("EMAIL_PASSWORD")
username = input("Enter username: ")
password = pwinput.pwinput(prompt="Enter Password: ")
routeKey = int(input("Enter 1,2 for 3 for \n1)North Campus -To- Mandi (via South) \n2)Mandi -To- North Campus (via South) \n3)North Campus -To- Mandi (Direct)\n"))
Routes = {
    1: "North Campus -To- Mandi (via South)",
    2:  "Mandi -To- North Campus (via South)",
    3: "North Campus -To- Mandi (Direct)"
}
traveldate = input("Enter the date and month (eg: 20 January): ")
traveltime = input("Enter the travel time(HH:MM AM/PM): ")
userbus = 'BUS(G)'#Hardcoded, will have to change according to need
print(int(traveltime[3:]))
try:
    BookTicket(traveldate,traveltime,Routes[routeKey],username,password,userbus)
except:
    scheduler =  BackgroundScheduler()
    scheduler.add_job(
    BookTicket,  
        'cron', hour=int(traveltime[:2]), minute=int(traveltime[3:]), args=[traveldate, traveltime, Routes[routeKey], username, password, userbus]
    )
    scheduler.start()

    try:
        while not booked:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
