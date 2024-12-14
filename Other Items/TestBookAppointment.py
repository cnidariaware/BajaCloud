from WriteDB import AppendAppointment

def TestBookAppointment():
    date_1 = "2024-09-16"
    start_time_1 = "10:30:00"
    interviewee_name_1 = "Alice Johnson"
    interviewee_email_1 = "ahmadmuhammadofficial@gmail.com"
    print(f"\nTest Case 1: Trying to book {date_1} at {start_time_1} for {interviewee_name_1} ({interviewee_email_1})")
    AppendAppointment(date_1, start_time_1, interviewee_name_1, interviewee_email_1)

TestBookAppointment()  