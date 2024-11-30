from WriteDB import AppendAppointment
from email_validator import validate_email, EmailNotValidError


def SelectAppointment (appointmentJson):
    """ 
    packages up a response for a http request

    ``appointmentJSON``: ``JSON``
    The appointment date and time details

    ``returns``: ``json``
    Returns the status of the booking confirmation

    ``Develop in part by``: Brock T

    ``Contact``: darkicewolf50@gmail.com
    """
    """
    {
        "intervieweeName": "Alice Johnson",
        "date": "2024-09-16",
        "startTime": "10:30:00",
        "intervieweeEmail": "darkicewolf50@gmail.com"
    }
    """
    try:
        validEmail = validate_email(appointmentJson["intervieweeEmail"], check_deliverability=True)
        if validEmail:
            status = AppendAppointment(date=appointmentJson["date"], start_time=appointmentJson["startTime"], interviewee_name=appointmentJson["intervieweeName"], interviewee_email=appointmentJson["intervieweeEmail"])
            
            if status:
                resBody = {"Success": True, "validEmail": "true"}
            else:
                resBody = {"Success": False, "validEmail": "true"}
            
            # resBody["message"] = appointmentJson for testing
            return resBody
        
    except EmailNotValidError as e:
        return {"Success": False, "validEmail": "false"}

if __name__ == "__main__":
    print(SelectAppointment("10:00 AM"))