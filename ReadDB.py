import pandas as pd

def ReadDatabase():
    # Load the updated Excel file into a pandas DataFrame
    excel_file_path = "./interview_database.xlsx"
    df = pd.read_excel(excel_file_path)

    # Initialize the dictionary to store the structured data
    interview_data = {}

    # Group the DataFrame by Date, Start Time, and Slot for organization
    for _, row in df.iterrows():
        date = row['Date']
        start_time = row['Start Time']
        slot = int(row['Slot']) if not pd.isna(row['Slot']) else 0

        # Initialize nested structure if not present
        if date not in interview_data:
            interview_data[date] = {}
        if start_time not in interview_data[date]:
            if len(str(row['Interviewee Name']).split()) != slot:
                interview_data[date][start_time] = {
                    'Meeting Duration': row['Meeting Duration'],
                }
    # Print the structured dictionary in JSON format for readability
    return interview_data