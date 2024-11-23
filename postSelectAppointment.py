import json
import datetime

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
    res = {"statusCode": 200,
        "isBase64ENcoded": "false",
        "headers": {
            "Content-Type": "application/json",  # Specify content type
            "X-IsBase64Encoded": "false"  # Indicating that the body is not base64 encoded
        },
        "body": ""}
    
    if status:
        res["body"] = {"Success": True}
    else:
        res["body"] = {"Success": False}
    
    return json.dumps(res)

def mockWriteFunction(appTime):
    return 0

if __name__ == "__main__":
    print(SelectAppointment("10:00 AM"))