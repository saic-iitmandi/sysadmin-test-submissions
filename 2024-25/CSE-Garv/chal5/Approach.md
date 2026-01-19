### **Approach:**

#### **1. Scheduling vs. Polling:**
Instead of continuously polling the booking website to check when the booking window opens (which would consume unnecessary resources), we use **APScheduler** to schedule a task that runs at the precise time required. This avoids unnecessary looping or waiting, reducing CPU usage and making the process efficient.

---

#### **2. How the Solution Works:**
1. **Input and Validation:**
   - The user provides the desired booking date and time in `YYYY-MM-DD` and `AM/PM` formats.
   - The script calculates **15 days before the booking date** and determines whether the booking should happen immediately or be scheduled for a later time.

2. **Blocking Scheduler (APScheduler):**
   - If the current date is more than 15 days before the booking date, the `BlockingScheduler` is used to schedule the booking task at the calculated time. 
   - The `BlockingScheduler` keeps the script running and executes the booking process precisely at the scheduled time.

3. **Immediate Execution:**
   - If the current date is within 15 days of the booking date, the script skips scheduling and directly executes the booking process.

4. **Precise Execution Using APScheduler:**
   - APScheduler's **`date` trigger** is used to run the task once at the exact specified time. This ensures precision without manual intervention.

---

#### **3. Handling the Booking Task:**
- When the booking process starts (either immediately or at the scheduled time):
  - The script interacts with the booking website using **Selenium WebDriver** to:
    - Log in to the site.
    - Select the appropriate dropdown options (e.g., bus route, time).
    - Confirm the seat booking.
  - After successfully booking, an email notification is sent to the user.

---

#### **4. Security Measures:**
- **Avoid Hardcoded Credentials:**
  - Credentials (email, app password) are stored securely in environment variables using the `python-decouple` library.
- **Application-Specific Passwords:**
  - The script uses application-specific passwords for email notifications to avoid exposing the primary email account.

---

#### **5. Notifications:**
Once the booking is successful, the script sends an email confirmation to notify the user of the booking status, along with the bus details. This ensures that the user is informed without needing to manually check the system.

---

### **Advantages of This Approach:**

1. **Resource-Efficient:**
   - By scheduling tasks instead of polling, CPU and memory usage is minimized.

2. **Precision:**
   - APScheduler ensures that the booking task runs at the exact time without delays or manual intervention.

3. **Scalability:**
   - The approach can be easily extended to handle multiple bookings at different times.

4. **User-Friendly:**
   - The script automatically calculates the correct time to book based on the user-provided input, eliminating manual effort.

---

### **Key Scenarios Handled:**

| **Scenario**                   | **Behavior**                                                                                  |
|--------------------------------|----------------------------------------------------------------------------------------------|
| Current date is > 15 days before booking | Task is scheduled for 15 days before the booking date at the specified time.              |
| Current date is ≤ 15 days before booking | Task executes immediately, booking the seat right away.                                   |
| Invalid date or time provided  | The script handles validation errors and prompts the user to re-enter valid input.          |

