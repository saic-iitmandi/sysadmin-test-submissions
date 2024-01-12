from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from datetime import datetime, timezone, timedelta
import re
import time
import smtplib
from email.message import EmailMessage

user_id = '_____'
Moodle_password = '*****'
course = '______'
total_assign = 0
submition_report =[]

#Create an email body
sender_email = ''    # sender's email
sender_email_password = '*****' # password of sender email
receiver_email = '' # receiving email
subject = f'Do your assignment of {course} stupid'

# will be modifying the body later to make it a littile more dynamic
body_1 = ''' 
        SHAME a bot have to remind you now that your assignment in subject is not yet completed.
        AND less than 6 hrs are left  now
'''

em = EmailMessage() 
em["To"] = sender_email
em["From"] = receiver_email
em["Subject"] = subject
em.set_content(body_1)


curr = time.time()

#function to calculate remaining time
def remaining_time(Due):
    epoch_time = int(Due.replace (tzinfo = timezone.utc).timestamp())
    
    time = (epoch_time - curr) / 3600
    return round(time , 2) 


#function to extract date and time of assignment

def extract_dates_and_times(input_text):
    # Define regular expressions for extracting dates and times
    opened_match = re.search(r'Opened: (.+?)\n', input_text)
    due_match = re.search(r'Due: (.+?)\n', input_text)

    # Extract matched groups
    opened_date_str = opened_match.group(1) if opened_match else None
    due_date_str = due_match.group(1) if due_match else None

    # Convert date strings to datetime objects
    opened_date = datetime.strptime(opened_date_str, '%A, %d %B %Y, %I:%M %p') if opened_date_str else None
    due_date = datetime.strptime(due_date_str, '%A, %d %B %Y, %I:%M %p') if due_date_str else None

    return opened_date, due_date

# getting into website to collect information
# i have explained the process along the way as much as i could
with sync_playwright() as p :
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://lms.iitmandi.ac.in/login/index.php")
    page.fill("input#username",user_id)
    page.fill("input#password",Moodle_password)
    page.click("button[type=submit]")

    nt_button = page.get_by_role("link",name=course)
    nt_button.click()

    # find total no. of assignments 
    k = True
    while k :
        inputext = f'Assignment {total_assign + 1}'
        result = page.locator(f'text=/{inputext}/i')
        try:
            if result.is_visible():
                k = True
            else:
                k = False
        except:
            k = True

        total_assign += 1
    total_assign -= 1
    # move inside the assignment to find time remaining
    for i in range(1,total_assign + 1) :
        assignment_button = page.get_by_role("link",name=f"Assignment {i}")
        assignment_button.click()

        page.is_visible('div.description-inner')

        #parsing html file using Beautifulsoup library and extracting as much info as we can
        html = page.inner_html("#region-main-box")  # collecting html file
        soup = BeautifulSoup(html,'html.parser')  # parsing html file
        submission_status = soup.find("td",{'class':'submissionstatussubmitted cell c1 lastcol'}).text
        str = soup.find('div',{'class':"description-inner"}).text

        # calculate hours remaining to submit assignment
        opened_time, due_time = extract_dates_and_times(str)
        submission_due = remaining_time(due_time)
        
        # Aggregation of all informations
        submition_report.append([f'Assignment {i}' , submission_status , submission_due])

        nt_button.click()

# Sending an email 
def email(receiver , sender , password , email):
    smtpobj = smtplib.SMTP('smtp.gmail.com' , 587)    
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.login(sender , password)
    smtpobj.sendmail(sender , receiver , email.as_string())
    smtpobj.quit()


# Conditioning to what to do
for i in range(total_assign):
    if (submition_report[i][1] == 'No submissions have been made yet') and (0 < submition_report[i][2] < 6.1):
        
        #send the email        
        body_1 = f'''
            SHAME a bot have to remind you now that your assignment {i+1} in {course} is not yet completed.
        AND less than 6 hrs are left  now
        '''
        em.set_content(body_1)
        # em['Subject'] = subject_1
        email(receiver_email, sender_email, sender_email_password, em)

    elif (submition_report[i][1] == 'No submissions have been made yet') and (0 > submition_report[i][2] ):
        #send the email        
        body_1 = f'''
            you have unsubmitted assignment {i+1} in subject {course} 
        '''
        em.set_content(body_1)
        # em['Subject'] = subject_1
        email(receiver_email, sender_email, sender_email_password, em)    
    

