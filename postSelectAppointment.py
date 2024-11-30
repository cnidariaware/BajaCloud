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

    print(appointmentJson)

    status = mockWriteFunction(appointmentJson)
    
    if status:
        resBody = {"Success": True}
    else:
        resBody = {"Success": False}
    
    return {
            "statusCode": 200,
            "isBase64ENcoded": "false",
            "body": json.dumps(resBody)
        }

def mockWriteFunction(appTime):
    return 0

if __name__ == "__main__":
    print(SelectAppointment("10:00 AM"))