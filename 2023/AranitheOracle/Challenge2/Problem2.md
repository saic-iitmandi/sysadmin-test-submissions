# SAIC SysAdminTest'23

## Challenge 2 - Docker Monitoring & Scripting

Here we are tasked to monitor the docker containers and send an email to saic@students.iitmandi.ac.in when the container changes state from normal/running.

-----------------------------------------------------

### EmailAutomation
-----------------------------------------------------

So for the email automation script I took help from [GeekForGeeks](https://www.geeksforgeeks.org/how-to-send-automated-email-messages-in-python/). I used the services of [STMP2GO](https://www.smtp2go.com/).

The code for the email sender : [emailautomation.py](emailautomation.py). 

In the code `smtp.login('email', 'password')` and `smtp.sendmail(from_addr="email",to_addrs=to, msg=msg.as_string())` change the _email_ and _password_ to the email address of the sender and his password. If you have an account in a trusted **SMTP** server change the server name and port number in `smtp = smtplib.SMTP('mail.smtp2go.com', 2525)` . 

-----------------------------------------------------


### MonitoringContainers
-----------------------------------------------------

Now it was time for the monitoring part. Initially, I thought of shell scripting. Using docker commands of `(docker ps -a --format "{{.ID}}")` and `(docker ps -a --format "{{.Status}}")` to get the ID and Status so that when there is a Status change from UP to Exited it will run the [emailautomation.py] using `python3 emailautomation.py`. Things got a bit messy cause I guess my knowledge is too low (at least they are not zero due to [**Network Chuck**](https://youtube.com/playlist?list=PLIhvC56v63IKioClkSNDjW7iz-6TFvLwS&si=TlVexjvb_uF1X9xB)).

Then I was googling stuff about dockers and came to know we can code about dockers in **Python**. Just need to run `pip install docker` to install the docker module. One more search led me to: (https://github.com/docker/docker-py/tree/main
) which eventually led me to: (https://docker-py.readthedocs.io/en/stable/containers.html). Then little more surfing and scratching for details helped me gather all the information required to learn about the different functions of this module and its similarity to the docker commands. I also found a video : (https://youtu.be/YY_WCBf0b98?si=f-STl23_EbgOy7OX) which made it a little bit easier.

The code for monitoring : [monitor.py](monitor.py) .

Here I first imported the function I created for email automation. Wrote the basic syntax. The main task was to get the list of all containers. I used `docker.from_env().containers.list(all=True)` for the purpose which is similar to `docker ps -a` . Then use the command `.status` to get the current status and run an if statement using it. Then get all kinds of information about the container like name, ID, image, time exited, current status, etc. 

For scheduling purposes I used the ***time*** module of **python**. I created a pause by using `time.sleep(100)` so that the code runs every 100 seconds and monitor the changes in the docker containers. As a change is detected email will be successfully sent.

[Demonstration](Screenshots/demonstration.jpg) of email being received when container status changes.

