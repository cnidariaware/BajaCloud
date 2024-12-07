import pandas as pd
import json
from openpyxl import load_workbook
from send_email import send_email
from filelock import FileLock 

# Define the path to the Excel file and the lock file
file_path = "./interview_database.xlsx"
lock_path = "./interview_database.xlsx.lock"  # Lock file for synchronization

"""
TODO chnage to dynamic file name
    year_donation = int(str(datetime.datetime.now().year)[2:]) + 1 # gets the last two digits of the current year then adds 1 for the current season
    file_name = f"OR{year_donation}-L-Interview Data.xlsx" # name based off the 2025 naming system
"""
def ReadDatabase():
    """ 
    Reads the Database to retrieve available interview slots.

    ``REQUIRES``: None
    
    ``PROMISES``: JSON (Available interview slots)

    ``Developed by``: Ahmad

    ``Contact``: ahmad.ahmad1@ucalgary.ca
    """
    # Use a file-based lock for thread-safe and process-safe access
    with FileLock(lock_path):
        # Load the Excel file into a pandas DataFrame with specific columns
        df = pd.read_excel(file_path, usecols=['Date', 'Start Time', 'Slot', 'Interviewee Name', 'Interviewee Email', 'Meeting Duration'])

    # Initialize the dictionary to store structured data for available slots
    interview_data = {}

    # Process each row in the DataFrame to structure data by date and time
    for _, row in df.iterrows():
        # Convert Date and Start Time to string format for easier comparison
        date = str(row['Date']).split(" ")[0]  # Format date to YYYY-MM-DD
        start_time = str(row['Start Time'])
        
        # Calculate the slot capacity and current number of interviewees
        slot_capacity = int(row['Slot']) if not pd.isna(row['Slot']) else 0
        interviewee_names = [name.strip() for name in str(row['Interviewee Name']).split(',') if name.strip()]
        interviewee_count = len(interviewee_names) if interviewee_names != ["nan"] else 0

        # Check if there are available slots for more interviewees
        if interviewee_count < slot_capacity:
            # Organize data by date and time, keeping track of available slots and meeting duration
            if date not in interview_data:
                interview_data[date] = {}
            interview_data[date][start_time] = {
                'Meeting Duration': row['Meeting Duration'],
                'Available Slots': slot_capacity - interviewee_count
            }

    return interview_data

def AppendAppointment(date, start_time, interviewee_name, interviewee_email):
    """ 
    Appends a new appointment with the interviewee's name and email if the slot is available.

    ``REQUIRES``: date (str), start_time (str), interviewee_name (str), interviewee_email (str)
    
    ``PROMISES``: Updates the Excel file with the new interviewee's name and email if there is an available slot. Returns Bool.

    ``Developed by``: Ahmad

    ``Contact``: ahmad.ahmad1@ucalgary.ca
    """
    available_slots = ReadDatabase()
    
    # Check if the requested slot is available in the `available_slots` structure
    if date in available_slots and start_time in available_slots[date]:
        with FileLock(lock_path):  # Ensure process-safe access to the file
            # Load workbook and select "Sheet1" for updating appointments
            workbook = load_workbook(file_path)
            sheet = workbook["Interview Timetable"]
            df = pd.read_excel(file_path)

            # Find and update the row that matches the provided date and start time
            for index, row in df.iterrows():
                row_date = str(row['Date']).split(" ")[0]
                row_start_time = str(row['Start Time'])

                if row_date == date and row_start_time == start_time:
                    # Current entries for names and emails, and append new data with comma and space
                    current_names = str(row['Interviewee Name']).strip()
                    current_emails = str(row['Interviewee Email']).strip()
                    
                    updated_names = f"{current_names}, {interviewee_name}" if current_names != "nan" else interviewee_name
                    updated_emails = f"{current_emails}, {interviewee_email}" if current_emails != "nan" else interviewee_email

                    # Update the cells with new names and emails
                    name_cell = sheet.cell(row=index + 2, column=df.columns.get_loc('Interviewee Name') + 1)
                    email_cell = sheet.cell(row=index + 2, column=df.columns.get_loc('Interviewee Email') + 1)
                    name_cell.value = updated_names
                    email_cell.value = updated_emails

                    workbook.save(file_path)
                    send_email(interviewee_email, interviewee_name, date, start_time)
                    return True

    # If no slots available, return that the slot is unavailable
    return False


def run_tests():
    """ 
    Executes test cases to verify appointment scheduling and slot availability.

    ``REQUIRES``: None
    
    ``PROMISES``: Prints test outcomes to validate successful booking or slot unavailability.
    """
    print("Available Slots:")
    available_slots = ReadDatabase()
    print(json.dumps(available_slots, indent=4))

    # Test Case 1: Append to an available slot on 2024-09-16 at 10:30:00
    date_1 = "2024-09-16"
    start_time_1 = "10:30:00"
    interviewee_name_1 = "Alice Johnson"
    interviewee_email_1 = "ahmadmuhammadofficial@gmail.com"
    print(f"\nTest Case 1: Trying to book {date_1} at {start_time_1} for {interviewee_name_1} ({interviewee_email_1})")
    AppendAppointment(date_1, start_time_1, interviewee_name_1, interviewee_email_1)

    # Test Case 2: Append to an available slot on 2024-09-17 at 13:30:00
    date_2 = "2024-09-17"
    start_time_2 = "13:30:00"
    interviewee_name_2 = "Bob Smith"
    interviewee_email_2 = "bob.smith@example.com"
    print(f"\nTest Case 2: Trying to book {date_2} at {start_time_2} for {interviewee_name_2} ({interviewee_email_2})")
    AppendAppointment(date_2, start_time_2, interviewee_name_2, interviewee_email_2)

    # Test Case 3: Attempting to book at 10:30:00 on 2024-09-16 for a different interviewee
    date_3 = "2024-09-16"
    start_time_3 = "10:30:00"
    interviewee_name_3 = "Charlie Brown"
    interviewee_email_3 = "charlie.brown@example.com"
    print(f"\nTest Case 3: Trying to book {date_3} at {start_time_3} for {interviewee_name_3} ({interviewee_email_3})")
    AppendAppointment(date_3, start_time_3, interviewee_name_3, interviewee_email_3)

# Run tests
if __name__ == "__main__":
    run_tests()
