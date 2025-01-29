from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import smtplib
from datetime import datetime
import time
from pwinput import pwinput

print("""For north to mandi enter 1 \nFor mandi to north enter 2\nFor north to mandi(direct) enter 7""")
"""The written in question, I could not find what are other two exect options so I put things which all can understand."""
route_field_input=input()
date_input=input("Enter date here (format : YYYY-MM-DD ): ").split("-")
print("You should stay on this code running app, you will get to choose time of bus, according to your route.")

driver = webdriver.Chrome()
driver.get("https://oas.iitmandi.ac.in/instituteprocess/common/login.aspx")

username=driver.find_element(By.NAME,"txtLoginId")
username.clear()        # If you have some kind of saved info in your chrome then this will clear it. (username)
username.send_keys("xxxxx")
password=pwinput("Enter password : ")       # Password needs to be protected
password_field=driver.find_element(By.NAME,"txtPassword")
password_field.clear()          # Removing already saved 
password_field.send_keys(password)
time.sleep(2)
submit_field=driver.find_element(By.ID,"btnLogin")
submit_field.click()
""" You are logged in here. """
time.sleep(2)
driver.get("https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx")
time.sleep(5)   # Loading of another page may take more time
date_field=driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$TabContainer1$TabPanel1$txtFromDate")
date_field.click()
time.sleep(2)

# Date catching starts
ajax__calendar_title_link=driver.find_element(By.CLASS_NAME,"ajax__calendar_title")
current_time = str(datetime.now())  # Returns the current local date and time
time_in_list_system=current_time.split(" ")[0].split("-")
month_int_name={
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}    #  Dictionary From chatgpt 
# month_today=month_int_name(str(time_in_list_system[1]))
time.sleep(1)
if month_int_name[date_input[1]] not in ajax__calendar_title_link.text:
    next_arrow_link=driver.find_element(By.ID,"C1_nextArrow")
    time.sleep(1)
    next_arrow_link.click()
time.sleep(2)
if int(date_input[2])<15:
    i=0
    if int(date_input[2])<10:
        date_noob=date_input[2][1]  # Info about Thought of this has given in word.
    else:
        date_noob=date_input[2]
    while i<6:
        j=0
        while j<=6:
            mystr=f"C1_day_{i}_{j}"
            element=driver.find_element(By.ID,mystr)
            time.sleep(0.1)
            if element.text==date_noob:
                element.click()
                break
            j+=1
        i+=1
elif int(date_input[2])>15:
    i=5
    while i>=0:
        j=6
        while j>=0:
            mystr=f"C1_day_{i}_{j}"
            element=driver.find_element(By.ID,mystr)
            time.sleep(0.1)
            if element.text==str(date_input[2]):
                element.click()
                break
            j-=1
        i-=1
# Date setting got ended
time.sleep(5)
route_field=Select(driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$TabContainer1$TabPanel1$ddlRoute"))
route_field.select_by_value(route_field_input)
time.sleep(2)
schedule_field=Select(driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$TabContainer1$TabPanel1$ddlTiming"))
time.sleep(2)
time_list=[]
for option1 in schedule_field.options:
    time_list.append(option1.text)
    print(option1.text)
time.sleep(2)
time_of_bus=input("Give number time of bus from above and same sentence pattern : ")
schedule_field.select_by_index(time_list.index(time_of_bus))
time.sleep(2)
bus_name_field=Select(driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$TabContainer1$TabPanel1$ddlBus"))
time.sleep(2)
for bus in bus_name_field.options:
    print(bus.text)
print("DO NOT TYPE ANYTHING, FIRST Bus will be selected automatically.")
time.sleep(2)
bus_name_field.select_by_index(1)   #You can change index for second bus, by changing code here.
time.sleep(2)
iter=1
seat_counter=0
while iter<30:
    idnumber="checkbox"+str(iter)
    checkboxes = driver.find_element(By.ID,idnumber)
    if not checkboxes.is_selected():
        checkboxes.click()
        seat_counter+=1
    if seat_counter==1:
        break
    iter+=1

time.sleep(5)   #I've put more time as this step shouldn't consider any mistake here.

# Uncomment things below to choose submit option.
"""submit_button=driver.find_element(By.ID,"lnkSave")
submit_button.click()"""        # Submission process may take time and therefore I've put 5seconds delay
time.sleep(5)       
driver.get("https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx")
time.sleep(5)
"""------Tickets gets booked here------"""

booked_detail_tab=driver.find_element(By.ID,"__tab_TabPanel2")
booked_detail_tab.click()
time.sleep(5)
details_fields=driver.find_elements(By.TAG_NAME,"td")
list_of_details=[]
for tag_detail in details_fields:
    list_of_details.append(tag_detail.text)
while "" in list_of_details:
    list_of_details.remove("")
with open("Problem5\details_of_ticket.txt","w") as file:
    file.write(str(list_of_details))

sender_mail="xxxx"
reciever_mail="xxxx"

subject="Booking confirmation of Ticket on OAS"
message=f"Date : {list_of_details[1]} \n Route : {list_of_details[2]} \n Bus Board : {list_of_details[3]} \n Time : {list_of_details[4]} \n No of person : {list_of_details[5]} \n Name : {list_of_details[6]} "
text_on_email=f"Subject : {subject} \n\n {message}"

with open("Problem5\details_of_ticket.txt","a") as file:
    file.write(message)

server=smtplib.SMTP("smtp.gmail.com",587)   #587 is port number
server.starttls()
server.login(sender_mail,"<APP PASSWORD>")    #Second arguement is app password, watch vedio in same folder for details.

server.sendmail(sender_mail,reciever_mail,text_on_email)

"""Mail is Sended."""