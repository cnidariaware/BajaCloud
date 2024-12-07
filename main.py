import json
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def get_root():
    """
    This does nothing, allows for pings to check for life

    ``REQUIRES``: ```None`` Nothing

    ``PROMISES``: ``JSON`` returns a short message in the body

    ``Develop in part by``: Brock

    ``Contact``: darkicewolf50@gmail.com

    """

    res = {"message": "Hello I am alive, this does nothing"}

    # Return the response with the custom header
    return JSONResponse(
        headers={
            "isBase64Encoded": "false",  # Header Modification
        },
        content={
            "body": res # Ensure res is a dict or do json.dumps to enusre it is stringified
        }, 
        
        # status_code=200 commented out just to show how to change it if you wanted
        )


from GetSchedulePackager import getSchedulePackager

@app.get("/getAppointments")
async def getAppointments():
    """
    checks for all available slots in the database

    ``REQUIRES``: ```None`` Nothing

    ``PROMISES``: ``JSON`` returns all of the avaialbe slots by date then time

    ``Develop in part by``: Brock

    ``Contact``: darkicewolf50@gmail.com

    """
    
    res = getSchedulePackager()

    return JSONResponse(
        headers={
            "isBase64Encoded": "false",  # Header Modification
        },
        content={
            "body": res # Ensure res is a dict or do json.dumps to enusre it is stringified
        }, 
        
        # status_code=200 commented out just to show how to change it if you wanted
        )

from postSelectAppointment import SelectAppointment

class Appointment(BaseModel):
    """
    The formatted

    ``REQUIRES``: Correct Format

    ``PROMISES``: Formatted class, needs to be converted into dict os that it can be used in another file

    ``Develop in part by``: Brock

    ``Contact``: darkicewolf50@gmail.com

    """
    intervieweeName: str
    date: str 
    startTime: str
    intervieweeEmail: str


@app.post("/SelectInterview")
async def postSelectInterview(rawRequest: Appointment):
    """
    Books an interview, first checks if the slot is valid

    ``REQUIRES``: ```Appointment`` A specifically formatted request

    ``PROMISES``: ``JSON`` returns if the booking was successful or not

    ``Develop in part by``: Brock

    ``Contact``: darkicewolf50@gmail.com

    """

    requestDict = {key: str(value) for key, value in rawRequest.dict().items()}
    res = SelectAppointment(requestDict)

    return JSONResponse(
        headers={
            "isBase64Encoded": "false",  # Header Modification
        },
        content={
            "body": res # Ensure res is a dict or do json.dumps to enusre it is stringified
        }, 
        
        # status_code=200 commented out just to show how to change it if you wanted
        )