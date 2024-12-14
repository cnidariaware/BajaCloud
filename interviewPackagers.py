from ReadDB import ReadDatabase


def getSchedulePackager(file_name):
    """ 
    Packages up the response for a http response

    ``REQUIRES``: ``File_Path`` where the file is

    ``PROMISES``: ``JSON`` http response ready

    ``Develop in part by``: Brock T

    ``Contact``: darkicewolf50@gmail.ocm

    """
    return {
            "interviewDates": ReadDatabase(file_path=file_name)
        }

from WriteDB import AppendAppointment
from email_validator import validate_email, EmailNotValidError


def SelectAppointment (file_name, appointmentJson):
    """ 
    Packages up a response for a http request

    ``REQUIRES``: ``File_Path`` ``JSON`` where the file is, json has the data of interviewee name, date, starttime and  interviewee email
    
    ``PROMISES``: ``JSON`` Returns if the booking was a success

    ``Developed in part by``: Brock

    ``Contact``: darkicewolf50@gmail.com

    """
    """
    Example of an incoming http post body
    {
        "intervieweeName": "Brock",
        "date": "9/16/2024",
        "startTime": "11:00:00",
        "intervieweeEmail": "darkicewolf50@gmail.com"
    }
    """
    try:
        validEmail = validate_email(appointmentJson["intervieweeEmail"], check_deliverability=True)
        if validEmail:
            status = AppendAppointment(file_path=file_name, date=appointmentJson["date"], start_time=appointmentJson["startTime"], interviewee_name=appointmentJson["intervieweeName"], interviewee_email=appointmentJson["intervieweeEmail"])
            
            if status:
                resBody = {"Success": True, "validEmail": "true"}
            else:
                resBody = {"Success": False, "validEmail": "true"}
            
            # resBody["message"] = appointmentJson for testing
            return resBody
        
    except EmailNotValidError as e:
        return {"Success": False, "validEmail": "false"}

