import json
from django.http import HttpResponse

def index(request):
    ymlschedule = {"message": False}
    res = {
            #"statusCode": 200, commented out because not needed django/wrapper will handle it
            "isBase64ENcoded": "false",
            "body": json.dumps(ymlschedule)
        }
    return HttpResponse(json.dumps(res), content_type='application/json')
    '''
    response =  HttpResponse(json.dumps(res), content_type='application/json')
    response['X-IsBase64Encoded'] = 'false'  # Custom header to indicate base64 encoding
    response.status_code = 200
    return response

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def index():
    ymlschedule = {"message": False}
    
    # Create the response body with multiple items
    res = {
        "body": {
            "Schedule": ymlschedule,  # FastAPI will automatically serialize the dictionary
            "message": "good",
        }
    }
    
    # Set custom headers
    headers = {
        "isBase64Encoded": "false",  # Custom header
    }
    
    # Return the response with the custom header
    return JSONResponse(
        content=res, 
        headers=headers,
        # status_code=200 commented out just to show how to change it if you wanted
        )

    '''
