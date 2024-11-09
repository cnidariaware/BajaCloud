import json
import datetime

def SelectAppointment (appointmentTime:datetime):
    """ 
    packages up a response for a http request

    ``appointmentTime``: ``timedate``
    The appointment date and time details

    ``returns``: ``json``
    Returns the status of the booking confirmation

    ``Develop in part by``: Brock T

    ``Contact``: darkicewolf50@gmail.com
    """

    status = mockWriteFunction(appointmentTime)
    res = {"isBase64ENcoded": "false",
            "statusCode": 200,
            "body": ""}
    if status:
        res["body"] = {"Success": True}
    else:
        res["body"] = {"Success": False}
    return json.dumps(res)



def mockWriteFunction(appTime):
    return 0