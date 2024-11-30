import yaml
import json

with open("./MockDB/schedule.yaml", "r") as scheduleyml:
    ymlschedule = yaml.safe_load(scheduleyml)

def getSchedulePackager():
    """ 
    Formats and allows for the

    ``REQUIRES``: None

    ``PROMISES``: ``JSON`` http response ready

    ``Develop in part by``: Brock T

    ``Contact``: darkicewolf50@gmail.ocm

    """
    
    return {
            "interviewDates": json.dumps(ymlschedule)
        }

