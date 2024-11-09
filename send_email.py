import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(interviewee_email="darkicewolf50@gmail.com", interviewee_name="brock", date="y", start_time="x"):
    """ 
    Sends an email notification to the interviewee and a static Gmail account.
    
    ``REQUIRES``: interviewee_email (str), interviewee_name (str), date (str), start_time (str)
    ``PROMISES``: Sends an email to interviewee and static email on successful appointment booking.
    """
    # Define static email for notifications and Gmail credentials
    static_email = "uofcbaja.noreply@gmail.com"
    gmail_user = "uofcbaja.noreply@gmail.com"
    gmail_apppassword = "pver lpnt upjd zvld"

    # Create message object
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = f"{interviewee_email}, {static_email}"
    msg['Subject'] = "Interview Appointment Confirmation"

    # Message body
    body = (f"Dear {interviewee_name},\n\n"
            f"Your interview has been scheduled on {date} at {start_time}.\n"
            "Please ensure to be available at the designated time.\n\n"
            "Best regards,\nYour Interview Team")
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Setup the server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_apppassword)
        server.sendmail(gmail_user, [interviewee_email, static_email], msg.as_string())
        server.quit()
        print(f"Email sent successfully to {interviewee_email} and {static_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

send_email()
