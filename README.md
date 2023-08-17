# Car Rental Management System

This is a simple Car Rental Management System implemented using Python's `tkinter` for GUI, MySQL for database management, and object-oriented programming principles.

## Features

- **Rent a Car:** Users can input their name, Aadhar card details, required car model, and the number of days they need the car for. Upon submission, the information is stored in the database, and a confirmation bill is displayed.

## Usage

1. Install the required dependencies. You'll need Python and the `mysql-connector-python` library to be installed.
   
   ```bash
   pip install mysql-connector-python
   ```

2. Set up the MySQL database:
   - Make sure you have MySQL server installed and running.
   - Open the `data_base` function in the code and update the `host`, `user`, and `password` variables with your MySQL credentials.
   - Run the script to create the necessary database and table structure.

3. Run the main script:
   - Execute the script, and a GUI window will appear.
   - Choose between "RENT" and "Deposit" buttons to interact with the system.

## How to Use

1. **Rent a Car:**
   - Click on the "RENT" button.
   - Input your name, Aadhar card details, required car model, and the number of days you need the car for.
   - Click the "Submit" button to store your information and get a confirmation bill.

2. **Deposit:**
   - (Functionality not implemented in the provided code snippet.)

3. **Exit:**
   - Click on the "Exit" button to close the application.

## Note

- The provided code is a simplified implementation and may require additional features, error handling, and security measures for real-world usage.
- This code snippet doesn't include the functionality for depositing a car back to the agency.

Feel free to fork and enhance the code for your specific needs or integrate additional features like returning cars, managing bookings, etc.
