from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from NoSheet import NoSheet
import datetime
import os

year_donation = int(str(datetime.datetime.now().year)[2:]) + 1 # gets the last two digits of the current year then adds 1 for the current season
# name based off the 2025 naming system
# Define the path to the Excel file and the lock file
file_name = f"./Interviews/OR{year_donation}-L-Interview Data.xlsx"
if not os.path.isfile(file_name):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    NoSheet(file_name)

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


from interviewPackagers import getSchedulePackager

@app.get("/getAppointments")
async def getAppointments():
    """
    checks for all available slots in the database

    ``REQUIRES``: ``None`` Nothing

    ``PROMISES``: ``JSON`` returns all of the avaialbe slots by date then time

    ``Develop in part by``: Brock

    ``Contact``: darkicewolf50@gmail.com

    """
    
    res = getSchedulePackager(file_name)

    return JSONResponse(
        headers={
            "isBase64Encoded": "false",  # Header Modification
        },
        content={
            "body": res # Ensure res is a dict or do json.dumps to enusre it is stringified
        }, 
        
        # status_code=200 commented out just to show how to change it if you wanted
        )

from interviewPackagers import SelectAppointment

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

    ``REQUIRES``: ``Appointment`` A specifically formatted request

    ``PROMISES``: ``JSON`` returns if the booking was successful or not

    ``Develop in part by``: Brock

    ``Contact``: darkicewolf50@gmail.com

    """

    requestDict = {key: str(value) for key, value in rawRequest.dict().items()}
    res = SelectAppointment(file_name, requestDict)

    return JSONResponse(
        headers={
            "isBase64Encoded": "false",  # Header Modification
        },
        content={
            "body": res # Ensure res is a dict or do json.dumps to enusre it is stringified
        }, 
        
        # status_code=200 commented out just to show how to change it if you wanted
        )

