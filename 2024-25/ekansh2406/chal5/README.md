# Automatic Bus Booking and Email Sending Program

I have developed a program that automates the process of bus booking and sending confirmation emails. This program streamlines the booking process and ensures that users receive timely email notifications regarding their bookings.

## Features

### **Automated Bus Booking**
The program automates the bus booking process by **automatically opening the OAS website**, making it quick and efficient.

### **Credentials Stored in .env File**
User credentials are securely stored in a **`.env` file**, ensuring that sensitive information is kept safe.

### **Quick Booking**
The bus is booked within **14 seconds** when the file is run, providing a fast and reliable booking experience. Currently, it will book only seat no.1, but we can modify the code to book any empty seat.

### **Email Notifications**
Users receive confirmation emails for their bookings using the **Gmail API**, ensuring they are promptly informed about their reservations.

## Gmail API Integration

To send confirmation emails, the program integrates with the Gmail API. This requires setting up credentials and authorizing the application to send emails on behalf of the user. Detailed steps to set up the Gmail API are as follows:

1. **Create a Project in Google Cloud Console**: Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project.
2. **Enable Gmail API**: In the API Library, search for "Gmail API" and enable it for your project.
3. **Create Credentials**: Go to the "Credentials" tab and create OAuth 2.0 Client IDs. Download the credentials file.
4. **Authorize the Application**: Run the program to generate a token file by following the on-screen instructions to authorize access to your Gmail account.

## Hosting and Task Scheduling

The program will not book buses if the booking is open and the code is not running. To ensure continuous operation, you need to host the program on a server and use a task scheduler to run it at regular intervals.

### Hosting the Program

1. **Choose a Hosting Service**: Select a hosting service that supports your programming environment (e.g., AWS, Heroku, or any other cloud service).
2. **Deploy the Program**: Upload your program files to the hosting service and configure it to run the program.

### Using Cloud Task Scheduler

1. **Cloud Task Scheduler**: You can  use cloud-based task schedulers like Google Cloud Scheduler or AWS CloudWatch Events to run the program 15 days before the booking opens.

By following these steps, you can ensure that the bus booking process is automated and runs continuously without manual intervention.
