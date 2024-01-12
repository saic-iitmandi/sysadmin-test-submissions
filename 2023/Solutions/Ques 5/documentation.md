# Assignment Reminder Script Documentation

## Introduction

The Assignment Reminder script automates the process of sending email reminders for upcoming assignments. The script extracts information about assignments from a specified source, calculates the time until the submission deadline, and sends email reminders accordingly.

## Steps Followed

### 1. Information Collection

The script collects assignment information, including course, title, and deadline. This information serves as the basis for calculating the time until submission.

### 2. Email Body Creation

A function is implemented to create the email body dynamically. The email body includes details about the upcoming assignment, such as course, title, and the remaining time until the submission deadline.

### 3. Time Calculation Function

The script contains a function to calculate the time remaining until the submission deadline. This function is crucial for determining when to send email reminders.

### 4. HTML Data Parsing Function

To extract assignment details from the source, a function is implemented to parse HTML data. This function ensures accurate retrieval of information for further processing.

### 5. Using Playwright in Sync Mode

Playwright is utilized in synchronous mode to collect assignment information from the specified source. This step ensures efficient and reliable extraction of data.

### 6. Email Sender Function

An email sender function is implemented to automate the process of sending email reminders. This function utilizes a specified email server and includes functionality for dynamic email body creation.

### 7. Time-Based Email Sending

The script checks the time until the submission deadline and sends email reminders:
   - **6 hours before the deadline**: A reminder email is sent to inform users about the upcoming assignment.
   - **After the deadline**: If an assignment is overdue, a notification is printed, providing details about the course and assignment title.

## Usage

1. Clone the repository.
2. Install dependencies: `pip install playwright`
3. Customize the script based on your specific use case, including email server configuration and assignment data source.
4. Run the script: `script.py`

## Dependencies

- Python 3
- Playwright

## Configuration

Edit the script to configure the following:

- Email server details (SMTP server, port, credentials).
- Assignment data source (URL or any other source).

## Important Notes

- Ensure proper permissions and authorization for accessing the assignment data source.
- Customize the script according to your specific requirements and use case.
- This script is a template and may need adjustments based on the specifics of your environment and use case.
  
# learning outcomes 
learned a lot about website structure. `
Gain proficiency in using Python for scripting and automation.
Recognize the benefits of automation in repetitive tasks, such as sending email reminders for upcoming assignments.
Develop knowledge and understanding of web scraping techniques using Playwright.
Learn how to parse HTML data to extract relevant information.
also learned to do documentation with this

thankyou all i have learned a lot of things in just few days bcs of this test 
