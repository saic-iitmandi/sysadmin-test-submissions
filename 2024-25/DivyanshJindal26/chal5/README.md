# What the code does
- When the user inputs all the required details, the script first checks if it is more than or less than 15 days since that. Basically calculates the time difference between now and 15d from bus date. 
- If it is more than 15 days (meaning we can't book right now), the code will pause until it is exactly 15 days. Essentially stops the script until we can book the ticket
- When we can book the ticket, the code automatically uses selenium to start a chrome window, and logs into the LDAP using the credentials stored in the .env file.
- Then it navigates to the bus booking page and selects the date from the calender.
- The code checks if the date of bus is on the current page of the calender (while also checking the month), and if it is, it chooses the date. If the date of the bus is NOT present on that page meaning its in the other months, it starts scrolling thru the pages by clicking next until we find the date.
- Then it selects the pre-defined route. And waits for 1s to give time for the webpage to reload with the timings.
- Then it checks if the timing if available for our specific bus. If it is, it selects that and again wait for 1s to reload the page. If it isn't, it errors out and stops the script/
- After that, it selects the LAST bus on the bus list. If there are 2 available buses it selects the second one because the 2nd bus only is visible if the first one is 75% full.
- Upon selecting the bus, the bus layout opens and then sorts the seat numbers which are all not disabled aka free to book. 
- It checkmarks that seat and then saves it. And also handles the alert sent by the browser. 
- If alert says the bus isn't booked, the code tries to book it again and again because we know for a fact that it is available to book lol.
- If everything goes well, itll book the ticket and send the email to the user who is the owner of the LDAP account containing all the details along with ticket number and bus number etc.

# how i avoid polling.
- I calculate the time from the bus booking start date. The bus booking starts exactly 15 days before the date and time of the bus.
- I used the timedelta function to check if it has been more or less than the 15 day deadline from the bus.
- If it is more than 15d, I time.sleep() the code for the remaining time in seconds to just stop all the execution so that it doesn't take resources in the background.

# video