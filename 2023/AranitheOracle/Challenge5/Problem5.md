# SAIC SysAdminTest'23

## Challenge5 - Scripting

Here we are tasked to create a script to retrieve all the assignments which have submission deadlines in the future and don't have any submission till now and send email reminders about them.
_____________________________________________

First of all for the email services it is already mentioned in [Challenge2/Problem2.md](https://github.com/AranitheOracle/SysAdminTest-23/blob/main/Challenge2/Problem2.md) and use the same python script [emailautomation.py](https://github.com/AranitheOracle/SysAdminTest-23/blob/main/Challenge2/emailautomation.py) .

Initially I thought of creating a python script for logging into https://lms.iitmandi.ac.in/ . So I used service of `twill` module and for that purpose took help from (https://stackoverflow.com/questions/2680185/how-to-log-in-to-a-website-using-installed-twill) ,
(https://twill.readthedocs.io/en/latest/examples.html) . It failed. So I moved onto using the `selenium` module.

~~~python
from selenium import webdriver
from selenium.webdriver.common.by import By
# create webdriver object
driver = webdriver.Chrome()
driver.get("https://lms.iitmandi.ac.in/login/index.php")
driver.maximize_window()
element = driver.find_element(By.ID ,"username")
element.send_keys("yourusername")
ps=driver.find_element(By.ID ,"password")
ps.send_keys("yourpassword")
button = driver.find_element(By.ID, "loginbtn")
button.click()
IC = driver.find_element(By.LINK_TEXT, "IC152 Introduction to Python and Data Science (DS-I)")
IC.click()
~~~

In the above code we can just add a for loop to loop over the assignments and checking the submission details.
(https://selenium-python.readthedocs.io/index.html) , (https://www.geeksforgeeks.org/selenium-python-tutorial/) Using these I was able to login into the website and get into the course. But couldn't complete the end steps.

Then more of googling helped me to find website scraping using Python. Websites like (https://discuss.python.org/t/login-to-a-website-for-scraping/16862/2) , (https://www.geeksforgeeks.org/python-web-scraping-tutorial/) , (https://www.zenrows.com/blog/web-scraping-login-python#waf-protected-websites) helped me to increase my knowledge. So we can use `requests` and `beautifulsoup4` libraries to get into the website and the get the required data. 

Another method can be using `PyAutoGUI` . This method will be over strenous . But we can automate mouse movements and automating keyboard to atfirst login into the site then going to the specific course and then going and checking the submission details.
<https://www.geeksforgeeks.org/gui-automation-using-python/>