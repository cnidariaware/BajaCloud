

def SelectAppointment (appointmentTime):
    status = mockWriteFunction(appointmentTime)
    res = {"isBase64ENcoded": "false",
            "statusCode": 200,
            "body": ""}
    if status:
        res["body"] = {"Success": True}
    else:
        res["body"] = {"Success": False}
    return res



def mockWriteFunction(appTime):
    return 0