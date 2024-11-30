import json
import datetime
import requests

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


    status = mockWriteFunction(appointmentJson)
    
    if status:
        resBody = {"Success": True, "message": ""}
    else:
        resBody = {"Success": False, "message": ""}
    
    resBody["message"] = appointmentJson["message"]
    return resBody

def mockWriteFunction(appTime):
    return 0

if __name__ == "__main__":
    print(SelectAppointment("10:00 AM"))