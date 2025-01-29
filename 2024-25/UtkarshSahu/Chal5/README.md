Okay so this is an interesting question with practical application. And this was my first question which I was able to solve (second question to be attempted after 1st Q).
So first I searched about how is this to be done. 
For automation, I had to use a web driver. So I setup the ChromeDriver and used Selenium. I tried some commands to get my hand on driver. \
I stored my credentials in .env and tried loggin in OAS. All works fine.

The issues start while filling up the form
1. The Bus booking website allows the users to type in whatever date they like, regardless of whether it is a valid date or not.
2. For date, I first used send_keys() function, but that did not give good results. Appeared broken. So I directly set the value of date using execute_script(). For this problem, I even approached Piyush Bhaiyas.
3. For seat number, I checked serial wise which seat was empty, and selected it.
4. One of the practical problem I was facing was that the dropdown menu of lets say time, appears after you have selected the route. So when I ran the script to fill the form, I found my internet wasn't as fast and it took some time (1 sec) to load the timings. And within that time, the script command had seemingly executed without giving any result. So I put a sleep of some interval between two stages while filling the form.
5. Next I added a schedular (using apscheduler and BlockingScheduler). Modified the date and time format to make it compatible.
6. For sending confirmation email, I used yagmail. I first encountered error for auth. I had to turn on 2FA and go for App Password. Only then was it working. I can't say why.
7. Finally, I was able to book a bus using the script.

Since we had to avoid polling, I ensured that the script shall be run once only, at the time of booking window opening, using apscheduler.