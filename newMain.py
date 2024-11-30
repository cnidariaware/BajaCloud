import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def get_root():
    res = {"message": "Hello World"}

    # Return the response with the custom header
    return JSONResponse(
        headers={
            "isBase64Encoded": "false",  # Header Modification
        },
        content={
            "body": res
        }, 
        
        # status_code=200 commented out just to show how to change it if you wanted
        )


    #     # Set headers
    # headers = {
    #     "isBase64Encoded": "false",  # Header Modification
    # }

from GetSchedulePackager import getSchedulePackager

@app.get("/getSchedule")
def getSchedule():
    
    res = getSchedulePackager()

    return JSONResponse(
        headers={
            "isBase64Encoded": "false",  # Header Modification
        },
        content={
            "body": res
        }, 
        
        # status_code=200 commented out just to show how to change it if you wanted
        )

from postSelectAppointment import SelectAppointment

@app.post("/SelectInterview")
def postSelectInterview(request):

    res = SelectAppointment(request)

    return JSONResponse(
        headers={
            "isBase64Encoded": "false",  # Header Modification
        },
        content={
            "body": res
        }, 
        
        # status_code=200 commented out just to show how to change it if you wanted
        )