# Import the requests and BeautifulSoup modules
import requests
from bs4 import BeautifulSoup
from cred5 import*

# Define the URL, username and password
url = "https://lms.iitmandi.ac.in/login/index.php"
username = lms_user
password = lms_password

# Create a requests session object
session = requests.Session()

# Get the login page and parse the HTML response
response = session.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the login form and the hidden input fields
form = soup.find("form", class_="login-form")
hidden_inputs = form.find_all("input", type="hidden")

# Create a payload dictionary with the username, password and the hidden input values
payload = {
    "username": username,
    "password": password
}
for hidden_input in hidden_inputs:
    payload[hidden_input["name"]] = hidden_input["value"]

# Post the payload to the login page and check the status code
response = session.post(url, data=payload, cookies=session.cookies)
response.raise_for_status()

# Get the page source of the logged in page
page_source = response.text

#-----------------------------------------------------------------
soup3 = BeautifulSoup(page_source, "lxml")
# Find all the 'a' tags with the class 'coursename'
courses = soup3.find_all('h3', class_='coursename')
urls=[]
course_names=[]
for course in courses:
    course_name=course.text.strip()
    course_url=course.a['href']
    urls.append(course_url)
    course_names.append(course_name)
# print(urls) 
# print(course_names)   
#------------------------------
A=['Pending assignments']
B=['Course Names']
C=['Time-status']

# Import the requests module
import requests
for URL in urls:
#URL='https://lms.iitmandi.ac.in/course/view.php?id=3314'
# Get the response object from the URL, passing the session object as an argument
    response = requests.get(URL, cookies=session.cookies)
        # Get the source code from the response object
    source_code = response.text

    from bs4 import BeautifulSoup

    # Create a BeautifulSoup object with the HTML code and the 'lxml' parser
    soup2 = BeautifulSoup(source_code, 'lxml')

    all_link = soup2.find_all("a", class_="aalink stretched-link")

    # Loop through the assignments and get the link and the text
    link_all=[]
    name_all=[]
    for i in all_link:
        link = i["href"] # get the link attribute
        link_all.append(link)
        text = i.span.text.strip() 
        name_all.append(text)# get the text inside the span tag
    # print the link and the text
    # print(link_all)
    # print(name_all)    
    import requests
    def is_assignment(url):
        return 'assign' in url

    # Filter the list of URLs using the function
    assignments = filter(is_assignment, link_all)

    # Loop through the filtered list
    link_ass=[]
    name_ass=[]
    for assignment in assignments:
        # Get the HTML content of the URL using requests
        html = requests.get(assignment).text
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # Find the name of the assignment inside the 'h2' tag with the class 'page-header-headings'
        ass_name=name_all[link_all.index(assignment)]
        # Print the name and the link of the assignment
        link_ass.append(assignment)
        name_ass.append(ass_name)

    # print(name_ass)    

    for url in link_ass[:len(link_ass)+1]:
        # Get the HTML content of the URL using the session
        response = requests.get(url, cookies=session.cookies)
        html = response.text
        
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        # Find the information in the HTML code using the 'tbody' tag
        info = soup.find("tbody")
        # Find the time remaining in the info using the 'td' tag with the class 'earlysubmission' or 'latesubmission'
        submit_status = info.find("td", class_='cell c1 lastcol').text.strip()
        
        if (submit_status=='No submissions have been made yet') :
            A.append(name_ass[link_ass.index(url)])
            B.append(course_names[urls.index(URL)])
            
    
from tabulate import tabulate

# Zip the lists into pairs
data = list(zip(A, B))

# Create the table
table = tabulate(data, headers="firstrow", tablefmt="grid",colalign=("left", "left"))
#print(table)

#-------------------------------------------------------SENDING MAIL
import yagmail

def send_email(subject, body, to_email):
    # Set up your Gmail credentials
    gmail_user = user_email
    gmail_password = user_password  # 16 letter password generated

    # Set up the connection to Gmail
    yag = yagmail.SMTP(gmail_user, gmail_password)

    # Compose the email
    email_subject = subject
    email_body = body

    # Send the email
    yag.send(to=to_email, subject=email_subject, contents=email_body)

# Example usage
script_output = table
send_email("Pending Assignment Reminder..!!", script_output, target_email)
# print(script_output)


