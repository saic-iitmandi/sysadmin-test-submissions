import smtplib
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

def parse_time_remaining(time_remaining):
    time_components = time_remaining.split()

    total_hours = 0

    for index, component in enumerate(time_components):
        if component == 'days':
            total_hours += int(time_components[index - 1]) * 24 
        elif component == 'hours':
            total_hours += int(time_components[index - 1])

    return total_hours


def send_email(subject,body):
    recipient_email = "utsavjain234@gmail.com"

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = "utsavjain218@gmial.com" 
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login("utsavjain218@gmail.com", "app password")
        smtp.send_message(msg)



options = webdriver.EdgeOptions()
options.add_argument("--headless")

driver = webdriver.Edge(options=options)
driver.get("https://lms.iitmandi.ac.in/login")


username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "loginbtn")

username_field.send_keys("username")
password_field.send_keys("******")
login_button.click()


driver.implicitly_wait(10)
course_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "coursename"))
)

# Dictionary to store course names and their links
course_data = {}

# Loop through the course elements to extract names and links
for course_element in course_elements:
    course_name = course_element.text.strip()
    course_link = course_element.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
    course_data[course_name] = course_link
    

for course_name, course_link in course_data.items():
    all_links = driver.find_elements(By.TAG_NAME,'a')
    
    driver.get(course_link)
    
    all_links = driver.find_elements(By.TAG_NAME, 'a')
    assignment_links = set()
    for link in all_links:
        href = link.get_attribute('href')
        if href and 'https://lms.iitmandi.ac.in/mod/assign/' in href:
            assignment_links.add(href)

    if not assignment_links:
        continue
    
    for assignment in assignment_links:
        driver.get(assignment)
        
        table_rows = driver.find_elements(By.CSS_SELECTOR,'.submissionstatustable tbody tr')
        submission_status = table_rows[0].find_element(By.CSS_SELECTOR,'td').text
        time_remaining = table_rows[2].find_element(By.CSS_SELECTOR,'td').text
        time_remaining= time_remaining.replace("remaining", "").strip()
        

        assignment_title = driver.find_element(By.CSS_SELECTOR,'h1.h2').text
        
        if time_remaining is not None and time_remaining != "-":

            if "No submissions have been made yet" in submission_status and all(keyword not in time_remaining for keyword in ["overdue", "submitted"]):
                time_remaining=parse_time_remaining(time_remaining)

                if time_remaining <= 6:
                    subject = f"Reminder: Assignment Submission - {assignment_title}"
                    body = f"Don't forget to submit {assignment_title} before the deadline."
                    send_email(subject,body)
                    
                    
                else:
                    scheduled_time = time_remaining - 6
                    subject = f"Reminder: Assignment Submission - {assignment_title}"
                    body = f"Don't forget to submit {assignment_title} before the deadline."
                    send_email(subject,body)
                    
                    # here i also send the the email if time remain is more than 6 also.
                    # you can change it and to make this script to send mails 6 hrs before deadline by making this script to run at a time before 6 hrs before the deadline means at around 6 pm as most of our assignment deadlines are at 12 am.
            
            
        # Check if the assignment is overdue and not submitted
            elif "No submissions have been made yet" in submission_status and "overdue" in time_remaining:
                # Find course name and assignment title using appropriate selectors
                subject = "Assignment is Overdue"
                body = f"Course Name: {course_name}\nAssignment Title: {assignment_title}"
                send_email(subject,body)
                
            else:
                continue  
        