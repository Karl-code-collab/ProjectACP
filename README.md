# BetaMax - Blood Donation Management System

BetaMax is a comprehensive Blood Donation Management System built with Python, designed to streamline the process of blood donation and requests. The system aligns with UN Sustainable Development Goal 3 (Good Health and Well-being) by facilitating efficient blood donation management.

## SDG Alignment

This project primarily supports **SDG 3: Good Health and Well-being** by:
- Facilitating efficient blood donation management
- Connecting blood donors with those in need
- Streamlining the blood request process
- Managing blood stock inventory effectively

## Features

### For Donors
- Registration and login system
- Profile management
- Blood donation status tracking
- Communication with administrators

### For Requestors
- Registration and login system
- Blood request management
- Urgency level specification
- Status tracking of requests

### For Administrators
- Comprehensive dashboard
- Donor management
- Request processing
- Stock monitoring
- Message management

### General Features
- Real-time blood stock monitoring
- User-friendly interface
- Secure authentication system
- Status tracking system


## How to Use

### For Donors
1. Launch the application and click on "Donate Blood"
2. If you're a new user, click on "Register Now!" to create an account
3. Fill in your personal details, including name, contact information, age, gender, and blood type
4. After registration or login, you'll see your donor dashboard
5. Check your donation status and any messages from administrators
6. Use the "Message Admin" button to communicate with administrators

### For Requestors
1. Start the application and select "Request Blood"
2. New users should register by clicking "Register Now!"
3. Provide necessary information, including blood type needed and urgency level
4. Once logged in, you can view your request status on the dashboard
5. Use the messaging feature to contact administrators for updates or questions

### For Administrators
1. Click on "Manage (Admin only)" from the main menu
2. Log in using admin credentials (default: Username - Admin, Password - missnakita)
3. Navigate through different sections:
   - Requests: Process blood requests and update their status
   - Donors: Manage donor information and update donation statuses
   - Stocks: Monitor current blood inventory levels
   - Messages: Respond to queries from donors and requestors
4. Use the refresh button to update information in real-time
5. Edit or delete user records as needed

### Checking Blood Availability
1. From the main menu, click on "Check Availability"
2. View the current stock levels for all blood types without needing to log in

## System Components

1. **BloodDonationSystem**: The main class that initializes the application and manages the overall flow.
2. **Admin**: Handles administrative functions like managing donors, requests, and blood stocks.
3. **Donor**: Manages donor registration, login, and donation processes.
4. **Requestor**: Handles blood request submissions and tracking.
5. **Stocks**: Manages the blood inventory system.

## Database Structure

The system uses a MySQL database with the following main tables:
- `donor_users`: Stores donor information
- `req_users`: Stores requestor information
- `admin`: Stores admin login credentials
- `donor_message` and `requestor_message`: Store messages from donors and requestors

## Acknowledgments

- Thanks to all contributors who have helped to improve this system.
- Special thanks to the open-source community for providing the tools and libraries used in this project.

## Technologies Used

- **Python** - Core programming language
- **tkinter** - GUI framework
- **customtkinter** - Modern UI components
- **MySQL** - Database management
- **mysql-connector-python** - Database connectivity

## Libraries and Dependencies

```python
import tkinter as tk
import customtkinter as ctk
import mysql.connector
import re