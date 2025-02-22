import pandas as pd
import json
from openpyxl import load_workbook
from .send_email import send_email
from filelock import FileLock 


"""
TODO update names to be more clear
TODO try to remove pandas  
"""
def ReadDatabase(file_path, lock_path):
    """ 
    Reads the Database to retrieve available interview slots

    ``REQUIRES``: ``File_Path`` ``Lock_Path`` where the file and lock are located
    
    ``PROMISES``: JSON (Available interview slots)

    ``Developed by``: Ahmad, Brock

    ``Contact``: ahmad.ahmad1@ucalgary.ca, darkicewolf50@gmail.com
    """   
    
    # Use a file-based lock for thread-safe and process-safe access
    with FileLock(lock_path):
        # Load the Excel file into a pandas DataFrame with specific columns
        df = pd.read_excel(file_path, usecols=['Date', 'Start Time Slot', 'Slot', 'Interviewee Name (What to call them)', 'Interviewee Email', 'Meeting Duration'], sheet_name="Interview TimeTable")

    # Initialize the dictionary to store structured data for available slots
        interview_data = {}

    # Process each row in the DataFrame to structure data by date and time
    for _, row in df.iterrows():
        # Convert Date and Start Time to string format for easier comparison
        date = str(row['Date']).split(" ")[0]  # Extract the date part

        start_time = str(row['Start Time Slot'])
            
        # Calculate the slot capacity and current number of interviewees
        slot_capacity = int(row['Slot']) if not pd.isna(row['Slot']) else 0
        interviewee_names = [name.strip() for name in str(row['Interviewee Name (What to call them)']).split(',') if name.strip()]
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

def AppendAppointment(file_path, date, start_time, interviewee_name, interviewee_email):
    """ 
    Appends a new appointment with the interviewee's name and email if the slot is available.

    ``REQUIRES``: ``File_Path`` ``str`` date, ``str`` start_time, ``str`` interviewee_name, ``str`` interviewee_email
    
    ``PROMISES``: ``None`` Updates the Excel file with the new interviewee's name and email if there is an available slot. Returns Bool.

    ``Developed by``: Ahmad, Brock

    ``Contact``: ahmad.ahmad1@ucalgary.ca, darkicewolf50@gmail.com
    """
    
    lock_path = file_path + ".lock"

    available_slots = ReadDatabase(file_path, lock_path)

    # Check if the requested slot is available in the `available_slots` structure
    if date in available_slots and start_time in available_slots[date]:
        with FileLock(lock_path):  # Ensure process-safe access to the file
            # Load workbook and select "Interview TimeTable" for updating appointments
            workbook = load_workbook(file_path)
            sheet = workbook["Interview TimeTable"]
            df = pd.read_excel(file_path, sheet_name="Interview TimeTable")

            # Find and update the row that matches the provided date and start time
            for index, row in df.iterrows():
                row_date = str(row['Date']).split(" ")[0]
                row_start_time = str(row['Start Time Slot'])

                if row_date == date and row_start_time == start_time:
                    # Current entries for names and emails, and append new data with comma and space
                    current_names = str(row['Interviewee Name (What to call them)']).strip()
                    current_emails = str(row['Interviewee Email']).strip()
                    
                    updated_names = f"{current_names}, {interviewee_name}" if current_names != "nan" else interviewee_name
                    updated_emails = f"{current_emails}, {interviewee_email}" if current_emails != "nan" else interviewee_email

                    # Update the cells with new names and emails
                    name_cell = sheet.cell(row=index + 2, column=df.columns.get_loc('Interviewee Name (What to call them)') + 1)
                    email_cell = sheet.cell(row=index + 2, column=df.columns.get_loc('Interviewee Email') + 1)
                    name_cell.value = updated_names
                    email_cell.value = updated_emails

                    status_cell = sheet.cell(row=index + 2, column=df.columns.get_loc('Status') + 1)
                    status_cell.value = "Unknown"

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
    import datetime
    year_donation = int(str(datetime.datetime.now().year)[2:]) + 1 # gets the last two digits of the current year then adds 1 for the current season
    # name based off the 2025 naming system
    # Define the path to the Excel file and the lock file
    file_name = f"./Interviews/OR{year_donation}-L-Interview Data.xlsx"
    lock = file_name + ".lock"

    print("Available Slots:")
    available_slots = ReadDatabase(file_path=file_name, lock_path=lock)
    print(json.dumps(available_slots, indent=4))

    # Test Case 1: Append to an available slot on 2024-09-16 at 10:30:00
    date_1 = "9/16/2024"
    start_time_1 = "10:30:00"
    interviewee_name_1 = "Alice Johnson"
    interviewee_email_1 = "ahmadmuhammadofficial@gmail.com"
    print(f"\nTest Case 1: Trying to book {date_1} at {start_time_1} for {interviewee_name_1} ({interviewee_email_1})")
    AppendAppointment(file_name, date_1, start_time_1, interviewee_name_1, interviewee_email_1)

    # Test Case 2: Append to an available slot on 2024-09-17 at 13:30:00
    date_2 = "9/17/2024"
    start_time_2 = "13:30:00"
    interviewee_name_2 = "Bob Smith"
    interviewee_email_2 = "bob.smith@example.com"
    print(f"\nTest Case 2: Trying to book {date_2} at {start_time_2} for {interviewee_name_2} ({interviewee_email_2})")
    AppendAppointment(file_name, date_2, start_time_2, interviewee_name_2, interviewee_email_2)

    # Test Case 3: Attempting to book at 10:30:00 on 2024-09-16 for a different interviewee
    date_3 = "9/16/2024"
    start_time_3 = "10:30:00"
    interviewee_name_3 = "Charlie Brown"
    interviewee_email_3 = "charlie.brown@example.com"
    print(f"\nTest Case 3: Trying to book {date_3} at {start_time_3} for {interviewee_name_3} ({interviewee_email_3})")
    AppendAppointment(file_name, date_3, start_time_3, interviewee_name_3, interviewee_email_3)

# Run tests
if __name__ == "__main__":
    run_tests()
