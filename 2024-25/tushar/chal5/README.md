# Bus Booking Automation for IIT Mandi

## Overview

This script automates the process of booking a bus seat on the IIT Mandi bus booking system

1. **Automated Booking**:

   - Monitors the bus booking system for availability at a specified date and time.
   - Automatically selects the desired path and books a seat once the booking window opens.

2. **Parameter-Based Configuration**:

   - Accepts inputs for:
     - Booking opening date and time.
     - Desired bus path (e.g., "North Campus -To- Mandi (via South)").

3. **Polling Avoidance**:

   - Uses a scheduled task to trigger the booking process precisely at the specified time, avoiding continuous polling of the website. retries afther  ```RETRY_INTERVAL```

4. **Security**:

   - Sensitive data such as login credentials is stored securely using environment variables.
      - Add the following variables to the `.env` file:
     ```env
     EMAIL=your-email@example.com
     PASSWORD=your-email-password
     LDAP_USERNAME=your-booking-username
     LDAP_PASSWORD=your-booking-password
     ```

5. **Email Notifications**:

   - Sends a confirmation email with booking details upon successful booking.

---

## Usage

1. Configure booking parameters:

   - Open the script file and update the following variables:
     ```python
     BOOKING_URL = "https://oas.iitmandi.ac.in/InstituteProcess/Common/Login.aspx"
     SEAT_BOOKING_URL = "https://oas.iitmandi.ac.in/InstituteProcess/Facility/BusSeatReservation.aspx"

     # Booking parameters
     bus_path = "North Campus -To- Mandi (via South)"
     booking_time = "07:00 AM"
     booking_date = "2025-01-20"  # Specify the date when bookings open
     ```

2. Run the script:

   ```bash
   python bus_booking.py
   ```

3. The script will:

   - Wait until the specified booking date and time.
   - Log in to the booking system.
   - Book a seat for the specified path.
   - Send a confirmation email with booking details.

---
