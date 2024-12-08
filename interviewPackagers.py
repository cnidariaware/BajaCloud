from ReadDB import ReadDatabase


def getSchedulePackager():
    """ 
    Packages up the response for a http response

    ``REQUIRES``: None

    ``PROMISES``: ``JSON`` http response ready

    ``Develop in part by``: Brock T

    ``Contact``: darkicewolf50@gmail.ocm

    """
    return {
            "interviewDates": ReadDatabase()
        }

from WriteDB import AppendAppointment
from email_validator import validate_email, EmailNotValidError


def SelectAppointment (appointmentJson):
    """ 
    Packages up a response for a http request

    ``REQUIRES``: ``JSON`` with the data of interviewee name, date, starttime and  interviewee email
    
    ``PROMISES``: ``JSON`` Returns if the booking was a success

    ``Developed in part by``: Brock

    ``Contact``: darkicewolf50@gmail.com

    """
    """
    Example of an incoming http post body
    {
        "intervieweeName": "Brock",
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

