 this question required lots of debugging and research from internet
so I first started with researching on how to interact with webpages I found about ‘selenium’ library which allowed us to do the same,
I used wsl for this, Installed the chrome driver and did all the necessary settings that I found online

then I started coding but before that I had to know how the bus booking website behaves
So I booked a bus myself first
these are the steps I saw were happening
1. We go to the OAS website where it asks for LDAP login, I noted down the id of the input boxes of ID and password from the view page source panel
2. Then we click login button so found its id as well 
3. The site loads and we appear on a blank home page with few links around
4. Then we go to the seat booking site
5. We choose the Date first , noted its id
6. Then the route, noted its ID
7. Then there is a slight delay
8. After that the timing drop down gets activated, it was a bit interesting because each time had its unique value for example “6:00 PM had value of 7” so I spent a bit of time and made a excel sheet of times, their values and their availability on specific routes for future reference

9. After choosing the time we choose the bus (the bus no. didn’t matter much because we can choose any bus that was available on the drop down)
10. After that we choose the seat no., the seat no were checkboxes fortunately their ids corresponded to their no. so didn’t had to use much of my brain there
11. After all that we click save button
12. We get an alert  message saying “Seat booking successful”
After all this I had most of the information I needed to do this
But first I needed to learn selenium library, so did some research and learnt a bit It wasn’t much but it was enough for me to be able to read selenium codes
I used chatgpt for it to write start of my code so I could get a skeleton of what I needed to do
Then I started writing the code 
after I wrote the first code and ran it, the actions were too fast that the website couldn’t keep up and it caused for many errors so I decided to put in some delays in between
So then I opened the booking portal again, and tried to measure delays that were happening when we performed the actions
The optimal delay I found was about 5 seconds between each interaction so it can work even on choppy internet (that 5 second did made testing a lot more longer that it frustrated me but it was necessary)
I tested again after lots of debugging and testing 
things worked fine after like 1 day of hard work
then for the email part I used some tutorials on youtube and it worked decently
but things went south when I tried to integrate in my main script
there was an error first that “unexpected Alert” ,I couldn’t understand at first and was confused what to do, after a long while I tried again and found something in the alert message, it was the same alert that happened after we pressed the save button and it was interfering with my email attempts 
So I used chatgpt to fix it quickly
but then again there was a weird error “stale element reference” I didn’t use my brain at this point and just searched the error, found articles but didn’t get anything from it
Used chatgpt again to ask what is the error it told me that I was trying to access something that disappeared after I clicked save due to the website being dynamic, I was using that in my email message composition 
I facepalmed about how idiotic I was, then I quickly saved the thing I wanted before the website changed and it worked like a charm :D



NOW  to automate it I can put in a script that can keep the python file activated at all times but I don’t understand how that approach will work and take input from user
Another approach might be to use cron that can run the script every set interval of time still I don’t know how that will work because user might need to book seat before or after


the only case where automation can work is either we use some crazy ai that can predict when the user will need (ofcourse that will be like hell to code)
Other case might be like if there is someone who goes to say for example “North to mandi” every 15 days at like 5:00 PM then it might be possible to use anacron to schedule the script execution every 15 days to book the ticket that I will book anyways
If I get time I will integrate such specific scenario in my script but for now it is semi automatic bus booking system

also I did notice some things that the booking portal opens 15 days before, I had less time left but I can also put that time checker after the date input that if time greater than 15 days it will show not possible and ask for date again


I used environment variables to secure my id passwords, I will upload the script and environment file without any id password so you will need to put your details in it before running it
also in the script at line 78 you will need to change the driver path
I used wsl to run it
also I can't upload the .env file here I guess
So if you want to run it please use this format of env file
save the .env file in the same directory as the script.py and please download chrome driver for it to work

LOGIN_ID= 

PASSWORD= 

SENDER_EMAIL=

SENDER_PASSWORD=

RECEIVER_EMAIL=


for demo video

https://drive.google.com/file/d/1cvn3LU1uzDc1PvhcsOjx3_Fm9XQJPo-m/view?usp=drive_link
