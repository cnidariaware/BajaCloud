import pandas as pd
import json
def ReadDatabase():
    """ 
    Reads the Database

    ``REQUIRES``: None
    
    ``PROMISES``: JSON (Interview Avaiable Slots)

    ``Develop in part by``: Ahmad

    ``Contact``: ahmad.ahmad1@ucalgary.ca

    """
    # Load the updated Excel file into a pandas DataFrame
    excel_file_path = "./interview_database.xlsx"
    df = pd.read_excel(excel_file_path)

    # Initialize the dictionary to store the structured data
    interview_data = {}

    # Group the DataFrame by Date, Start Time, and Slot for organization
    for _, row in df.iterrows():
        date = str(row['Date'])
        start_time = str(row['Start Time'])
        slot = int(row['Slot']) if not pd.isna(row['Slot']) else 0
        #Returns amount of interviewees in the slot and if it's empty it will return 0
        interviewee_amount = len(str(row['Interviewee Name']).split()) if str(row['Interviewee Name']) != "nan" else 0
        
        # Check if the slot is available for an interviewee to attend
        avaliable_slots = interviewee_amount != slot
        if avaliable_slots:
            # Initialize nested structure if not present
            if date not in interview_data:
                interview_data[date] = {}
            #Adds the start time and duration if not present
            if start_time not in interview_data[date]:
                    interview_data[date][start_time] = {
                        'Meeting Duration': row['Meeting Duration'],
                    }
    return interview_data
