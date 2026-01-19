import requests
from bs4 import BeautifulSoup
import re
import smtplib
import credentials

login_url = 'https://lms.iitmandi.ac.in/login/index.php'

header = {
    'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language: en-US,en;q=0.5',
    'Accept-Encoding: gzip, deflate, br',
    'Referer: https://lms.iitmandi.ac.in/',
    'DNT: 1',
    'Connection: keep-alive',
    'Upgrade-Insecure-Requests: 1',
    'Sec-Fetch-Dest: document',
    'Sec-Fetch-Mode: navigate',
    'Sec-Fetch-Site: same-origin',
    'Sec-Fetch-User: ?1',
}

data = {
    'anchor': '',
    'logintoken': '',
    'username': credentials.enrollementno,
    'password': credentials.my_password,
}

mycookies = {

}

def convert_time_to_seconds(time_string):
    time_units = {'days': 24 * 60 * 60, 'hours': 60 * 60, 'minutes': 60, 'seconds': 1}
    
    total_seconds = 0

    # Use regular expression to find numerical values and corresponding units
    matches = re.findall(r'(\d+)\s+(\w+)', time_string)

    for value, unit in matches:
        total_seconds += int(value) * time_units.get(unit.lower(), 0)

    return total_seconds

def send_email(message):
    sender = credentials.sender_email
    receiver = credentials.receiver_email
    password = credentials.my_password

    subject = 'Assignment Due'

    mail_content = f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp-mail.outlook.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, mail_content)
    server.quit()
    print('Email Sent!')


my_courses = []

my_assignments = []

with requests.Session() as s:
    r = requests.get(login_url)
    mycookies = r.cookies
    soup = BeautifulSoup(r.text, 'html.parser')
    logintoken_input = soup.find('input', {'name': 'logintoken'})
    logintoken =  logintoken_input.get('value')
    data['logintoken'] = logintoken
    s.post(login_url,cookies=mycookies, data=data)
    homepage = s.get('https://lms.iitmandi.ac.in/')
    home_soup = BeautifulSoup(homepage.text, 'html.parser')
    # print(home_soup)
    enrolled_courses = home_soup.find_all(class_='coursename')
    # print(enrolled_courses)

    for link in enrolled_courses:
        courses_links = link.find_all('a', href=True)
        
        for link in courses_links:
            href_value = link['href']
            my_courses.append(href_value)

    for course in my_courses:
        course_page = s.get(course)
        course_page_soup = BeautifulSoup(course_page.text, 'html.parser')
        title = course_page_soup.title.string
        # print(title)
        assignment = course_page_soup.find_all(class_='activity activity-wrapper assign modtype_assign hasinfo')
        # print(assignment)
        
        for ass_link in assignment:
            course_pages = ass_link.find_all('a', href=True)
            # print(course_pages)

            for ass_link in course_pages:
                ass_page = ass_link['href']
                # print(ass_page) # Prints url of assignment page.
                # my_assignments.append(ass_page)
                # print(my_assignments)
                ass_status = s.get(ass_page)
                ass_status_soup = BeautifulSoup(ass_status.text, 'html.parser')
                ass_title = ass_status_soup.title.string
                # print(ass_title)
                status = ass_status_soup.find_all('td')
                
                for tag in status:
                    if 'remaining' in tag.text:
                        print(ass_title.strip())
                        tag_text=tag.text.strip()[:-10]
                        # print(tag_text)
                        print(' |')
                        print(' ----->','Assignment Due by',tag_text,'\n')
                        
                        if convert_time_to_seconds(tag_text) > 21600:
                            print('Sending Reminder Email ...')
                            message = 'Hola Bro, Your assignment titled "' + ass_title +'" is yet to be submitted. And time remaining is '+ tag_text
                            send = send_email(message)
                            

                        else:
                            print("No due assignment in next 6 hrs")

                    elif 'overdue' in tag.text:
                        print(ass_title.strip())
                        print(' |')
                        print(' ----->','Assignment Overdue','\n')
                    else:
                        pass
