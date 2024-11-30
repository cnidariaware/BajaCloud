from WriteDB import AppendAppointment


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


    status = AppendAppointment(date=appointmentJson["date"], start_time=appointmentJson["startTime"], interviewee_name=appointmentJson["intervieweeName"], interviewee_email=appointmentJson["intervieweeEmail"])
    
    if status:
        resBody = {"Success": True}
    else:
        resBody = {"Success": False}
    
    # resBody["message"] = appointmentJson for testing
    return resBody

if __name__ == "__main__":
    print(SelectAppointment("10:00 AM"))