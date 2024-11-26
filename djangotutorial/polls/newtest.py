import json
from django.http import HttpResponse

def index(request):
    ymlschedule = {"message": False}
    res = {
            "statusCode": 200,
            "isBase64ENcoded": "false",
            "body": json.dumps(ymlschedule)
        }
    return HttpResponse(json.dumps(res))