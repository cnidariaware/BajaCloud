import yaml
import json

with open("./MockDB/schedule.yaml", "r") as scheduleyml:
    ymlschedule = yaml.safe_load(scheduleyml)

def getSchedulePackager():
    """ 
    What function does

    ``REQUIRES``: None

    ``PROMISES``: What function returns if applicable

    ``Develop in part by``: Brock T

    ``Contact``: darkicewolf50@gmail.ocm

    """
    res = {
           "isBase64ENcoded": "false",
            "statusCode": 200,
            "body": ymlschedule
        }
    return json.dumps(res)
