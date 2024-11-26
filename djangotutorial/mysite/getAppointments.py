import json
from django.http import HttpResponse
from .methods.GetSchedulePackager import getSchedulePackager


def index(request):
    res = getSchedulePackager()
    return HttpResponse(json.dumps(res))