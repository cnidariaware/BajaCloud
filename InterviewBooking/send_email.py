import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import pytz  # For timezone handling

"""
TODO add
"""
def send_email(interviewee_email="darkicewolf50@gmail.com", interviewee_name="brock", date="2024-1-10", start_time="10:00:00", location ="ENC25"):
    """ 
    Sends an email notification to the interviewee and to the uofcbaja account
    
    ``REQUIRES``: ``str`` interviewee_email, ``str`` interviewee_name, ``str`` date, ``str`` start_time

    ``PROMISES``: ``EMAIL`` Sends an email to interviewee and static email on successful appointment booking.

    ``Developed by``: Ahmad

    ``Contact``: ahmad.ahmad1@ucalgary.ca
    """
    # Define static email for notifications and Gmail credentials
    static_email = "uofcbaja@gmail.com"
    gmail_user = "uofcbaja.noreply@gmail.com"
    gmail_apppassword = "pver lpnt upjd zvld"

    # Define Mountain Standard Time
    mst = pytz.timezone("America/Edmonton")  # MST with Daylight Savings considered

    # Parse the input date and time, localize to MST
    start_datetime = mst.localize(datetime.strptime(f"{date} {start_time}", "%Y-%m-%d %H:%M:%S"))
    end_datetime = start_datetime + timedelta(minutes=30)

    # Format date and time for the calendar URLs
    start_time_google = start_datetime.strftime("%Y%m%dT%H%M%S")  # Google Calendar (Local time without Z)
    end_time_google = end_datetime.strftime("%Y%m%dT%H%M%S")  # Google Calendar (Local time without Z)
    outlook_start = start_datetime.isoformat()  # Outlook Calendar (ISO local time)
    outlook_end = end_datetime.isoformat()  # Outlook Calendar (ISO local time)

    # Create message object
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = f"{interviewee_email}, {static_email}"
    msg['Subject'] = "Interview Appointment Confirmation"

    # Message body
    body = f'''
<html lang="en-US">
	<head>
		<title>Interview Invitation</title>
	</head>
	<body>
		<p>Dear {interviewee_name},</p>
		<p>Your interview has been scheduled on {date} at {start_time}</p>
		<p>Please ensure to be available at the designated time.</p>
		<table
			role="presentation"
			border="0"
			cellpadding="0"
			cellspacing="0"
			style="width: 100%; margin: 20px 0">
			<tr>
				<td
					align="center"
					style="width: 48%; margin-right: 1%">
					<a
						href="https://calendar.google.com/calendar/render?action=TEMPLATE&text=UCalgary+Baja+Interview+with+{interviewee_name}&dates={start_time_google}/{end_time_google}&details=Interview+with+UCalgary+Baja+Team&location={location}"
            target="_blank"
						style="
							text-decoration: none;
							display: inline-block;
							background-color: #376fc9;
							color: white;
							padding: 10px 20px;
							font-family: Arial, sans-serif;
							font-size: 14px;
							border-radius: 4px;
							border: 2px solid grey;
						">
						<img
							src="https://res.cloudinary.com/dpgrgsh7g/image/upload/v1745094071/google-calendar-svgrepo-com_vkmq2n.png"
							alt="Google Calendar"
							style="
								vertical-align: middle;
								height: 40px;
								margin-right: 10px;
							" />
						Add to Google Calendar
					</a>
				</td>
				<td
					align="center"
					style="width: 48%; margin-left: 1%">
					<a
						href="https://outlook.live.com/calendar/0/deeplink/compose?subject=UCalgary+Baja+Interview+with+{interviewee_name}&body=Interview+with+UCalgary+Baja+Team&location={location}&startdt={outlook_start}&enddt={outlook_end}"
            target="_blank"
						style="
							text-decoration: none;
							display: inline-block;
							background-color: #376fc9;
							color: white;
							padding: 10px 20px;
							font-family: Arial, sans-serif;
							font-size: 14px;
							border-radius: 4px;
							border: 2px solid grey;
						">
						<img
							src="https://res.cloudinary.com/dpgrgsh7g/image/upload/v1745094071/ms-outlook-svgrepo-com_idmyw0.png"
							alt="Outlook Logo"
							style="
								vertical-align: middle;
								height: 40px;
								margin-right: 10px;
							" />
						Add to Outlook Calendar
					</a>
				</td>
			</tr>
		</table>
		<p>Best regards,</p>
		<p>UCalgary Baja Interview Team</p>
		<img
			src="https://res.cloudinary.com/dpgrgsh7g/image/upload/v1733003224/UCalgaryBAJA_Logo-2024_mpmljh.png"
			alt="UCalgary Baja Logo"
			height="120svh" />
		<p>
			If you need to change the date or cancel please email
			<a href="mailto:uofcbaja@gmail.com">uofcbaja@gmail.com</a>
			or reply all to this email
		</p>
	</body>
</html>
'''
    
    msg.attach(MIMEText(body, 'html'))

    try:
        # Setup the server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_apppassword)
        server.sendmail(gmail_user, [interviewee_email, static_email], msg.as_string())
        server.quit()
        # print(f"Email sent successfully to {interviewee_email} and {static_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
  send_email()
