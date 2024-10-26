import yaml
import json

with open("./MockDB/schedule.yaml", "r") as scheduleyml:
    ymlschedule = yaml.safe_load(scheduleyml)

def getSchedulePackager():
    res = {"isBase64ENcoded": "false",
            "statusCode": 200,
            "body": ymlschedule}
    return res
