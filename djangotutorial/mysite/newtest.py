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
    '''
