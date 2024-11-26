import json
from django.http import HttpResponse
from .methods.postSelectAppointment import SelectAppointment


def index(request):
    res = SelectAppointment(request)
    return HttpResponse(json.dumps(res))