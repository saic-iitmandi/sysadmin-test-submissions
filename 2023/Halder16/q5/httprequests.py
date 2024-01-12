import requests as requests
import lxml.html
import time

def crt_wbpg(stuff): #writes the response into a webpage we can see...
    f = open(r'C:/Users/sohan/Desktop/code/challenge_5/testing.html','w',errors='ignore')
    for i in stuff:
        f.write(i)
    f.close()

username = '***'
password = '***'
login_url = 'https://lms.iitmandi.ac.in/login/index.php'
target_url = 'https://lms.iitmandi.ac.in/my/courses.php'

# we need to address the user agent for some reason idk
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# Start session and get login form.
session = requests.session()
login = session.get(login_url, headers=headers)
time.sleep(5)

# Get the hidden elements and put them in our form.
login_html = lxml.html.fromstring(login.text)
hidden_elements = login_html.xpath('//form//input[@type="hidden"]')
form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}

# including the username and the password into the form
form['username'] = username
form['password'] = password # the form is now complete

resp = session.post(login_url, data=form)
time.sleep(5)

if resp.url != login_url : # this means we have logged in, because otherwise we'd still be at the login page
    content_resp = session.get(target_url)
    if content_resp.status_code == 200: # that is, if the target_url is loaded successfully
            page_content = content_resp.text
            crt_wbpg(page_content)
    else:
         print('something went wrong...')

# at this point im assuming the problem arises because im 'rewriting' the html to see the page somehow? - problem solved