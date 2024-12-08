import pandas as pd
import json
from filelock import FileLock, Timeout
import time

from NoSheet import NoSheet
import datetime
import os


"""
TODO update to possibly not use pandas and update to use the new template
TODO update name of function to be more clear
"""

def ReadDatabase():
    """ 
    Reads the database for which slots are available

    ``REQUIRES``: ``None``
    
    ``PROMISES``: ``JSON`` Interview Available Slots

    ``Developed in part by``: Ahmad, Brock

    ``Contact``: ahmad.ahmad1@ucalgary.ca, darkicewolf50@gmail.com

    """

    year_donation = int(str(datetime.datetime.now().year)[2:]) + 1 # gets the last two digits of the current year then adds 1 for the current season
    # name based off the 2025 naming system
    # Define the path to the Excel file and the lock file
    excel_file_path = f"OR{year_donation}-L-Interview Data.xlsx"
    lock_file_path = f"OR{year_donation}-L-Interview Data.xlsx.lock"

    if not (os.path.isfile(excel_file_path) or os.path.isfile(lock_file_path)):
        NoSheet()
    else:
        # Retry parameters
        max_retries = 60  # Maximum number of retries if the file is locked
        retry_interval = 0.5  # Wait time (in seconds) between retries

        retries = 0
        while retries < max_retries:
            try:
                # Attempt to acquire a shared read (non-blocking) access
                with FileLock(lock_file_path, timeout=0):  # Non-blocking, checks if the lock exists
                    # Load the Excel file into a pandas DataFrame
                    df = pd.read_excel(excel_file_path)

                    # Initialize the dictionary to store the structured data
                    interview_data = {}

                    # Group the DataFrame by Date, Start Time, and Slot for organization
                    for _, row in df.iterrows():
                        date = str(row['Date'])
                        start_time = str(row['Start Time'])
                        slot = int(row['Slot']) if not pd.isna(row['Slot']) else 0

                        # Returns the number of interviewees in the slot; returns 0 if empty
                        interviewee_amount = len(str(row['Interviewee Name']).split()) if str(row['Interviewee Name']) != "nan" else 0

                        # Check if the slot is available for an interviewee to attend
                        available_slots = interviewee_amount != slot
                        if available_slots:
                            # Initialize nested structure if not present
                            if date not in interview_data:
                                interview_data[date] = {}
                            # Add the start time and duration if not present
                            if start_time not in interview_data[date]:
                                interview_data[date][start_time] = {
                                    'Meeting Duration': row['Meeting Duration'],
                                }
                    return interview_data  # Successfully read the database

            except Timeout:
                # File is locked; wait and retry
                retries += 1
                print(f"File is locked, retrying ({retries}/{max_retries})...")
                time.sleep(retry_interval)

        # If max retries are exceeded, raise an error
        raise RuntimeError("Unable to access the database after multiple attempts due to a file lock.")

# Example usage of the ReadDatabase function
if __name__ == "__main__":
    try:
        data = ReadDatabase()
        print(json.dumps(data, indent=4))
    except RuntimeError as e:
        print(e)
