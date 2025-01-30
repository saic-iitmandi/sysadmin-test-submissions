## **Challenge 5 - Bus Booking Automation**

I have done last year sysadmin-test so I am familiar with _MIMEText, MIMEMultiPart_ and other libraries. Hence it is a bit easy for me.

## Script Flow:
- I used _MIMEText_ (for email sending), Selenium and chrome web driver (for interacting with the browser) and can not forget to use `load_dotenv` library to handle login credentials.
- Set up environment variables for LDAP-credentials.
- Defined a send confirmation email function which starts executing when the bus seat booking is confirmed.
- Send email about bus booking confirmation and details about the date, timings and seat number etc.
- A function to handle the travel date selector as it opens a calendar when clicked from which we have to select the date.
- Defined a function to automate booking
- Opens the browser with the LDAP Login page link and fills the credentials.
- After successful, login opens the bus booking link with web driver use.
- Fill each details like Travel date, route, schedule, bus no., seat no. etc.
- I have implemented a scheduler function which trigger the automate booking function only when the time reaches.
- Finally, secure a ticket in the bus for you and send you confirmation email with details.

## Issues Faced
1. Alert Message Pop Up ->  alert message is disturbing the script by poping up when the successful booking is done. 
- Resolved by assigning alert message in the script from web driver alerts library and clicking it after successful booking. 
2. Calendar Issue -> travel date input field do not take text input it pops up calendar and we have to select the date from that calendar. 
- Resolved this issue by creating a function which access the calendar div container and each date ids and click the date when its matches with our input date. 
1. Reload issue -> In the website schedule, bus no. are dropdown with <select></select> options but these reload only after filling the previous fields route and travel date. 
- Resolved by using web driver wait library for reload and _EC.presence_of_element_located()_ for knowing the presence of the <select></select> options in the schedule, bus no. dropdown.

## Improvements

- In the email confirmation details have all the parameters but the schedule, bus no. have values in the form of index selected in the dropdown but it can easily be improved upon by linking it with HTML ids.
- Till now calendar do not have method to loop through months as I have not linked the next HTML button id to the function due to too many labs and project works.

## Idea For Implementation
- As IIT Mandi bus booking is open always and has no time for the booking portal to open for only next 1 month or 2 months. So, I am thinking to make a web page or app(insti app may be) where we can provide a button which when clicked trigger the  script and book the ticket for you and email you for your confirmation details.

