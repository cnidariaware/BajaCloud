import pandas as pd
import yaml

# Load the YAML file
with open("./interview_database.yaml", 'r') as file:
    interview_data = yaml.safe_load(file)

# Access the nested structure within 'Data'
flattened_data = []
for date, date_info in interview_data['Data'].items():
    meeting_duration = date_info.get('Meeting Duration')
    
    for start_time_info in date_info.get('Meeting Start Times', []):
        for start_time, meeting_info in start_time_info.items():
            interviewer_name = meeting_info['Interviewer'][0].get('Name')
            interviewer_email = meeting_info['Interviewer'][1].get('Email')
            interviewee_name = meeting_info['Interviewee'][0].get('Name')
            interviewee_email = meeting_info['Interviewee'][1].get('Email')
            category = meeting_info.get('Category')
            status = meeting_info.get('Status')
            slot = meeting_info.get('Slot')
            
            # Add flattened row to list
            flattened_data.append({
                'Date': date,
                'Meeting Duration': meeting_duration,
                'Start Time': start_time,
                'Interviewer Name': interviewer_name,
                'Interviewer Email': interviewer_email,
                'Interviewee Name': interviewee_name,
                'Interviewee Email': interviewee_email,
                'Category': category,
                'Status': status,
                'Slot': slot
            })

# Convert to DataFrame if flattened data is not empty
if flattened_data:
    df = pd.DataFrame(flattened_data)
    # Write the DataFrame to an Excel file
    df.to_excel("interview_database.xlsx", index=False)
    print("Data has been written to interview_database.xlsx")
else:
    print("No data found to write.")
