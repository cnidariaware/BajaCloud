import openpyxl
import yaml
import json

yamlraw = """
    Interview TimeTable:
        - Date: Null
        - Meeting Duration: 30 min
        - Start Time Slot: Null
        - Interviewee Name: Null
        - Interviewee Email: Null
        - Category (if not general): Null
        - Interviewer(s) Name(s): Null
        - Status: Dropdown (Options in datahelp)
    Recruitment Responses:
        - Frist Name (What we should call them): Null
        - Last Name: Null
        - Ucalgary Email: Null
        - What Subsystem/SubTeam are you interested in?: Null
        - Major: Null
        - Academic Year: Null
        - Why are you interested in joining UCalgary BAJA?: Null
        - Where did you hear about us?: Null
        - Are you available for team meetings/work days? Saturdays 10 am - 4 pm: Null #add condiftional formatting for no to make whole line red
    Data Help:
        - Status Dropdown:
            - Unknown
            - Done
            - No Show
            - Cancelled/Moved
    """

yamlsheet = yaml.safe_load(yamlraw)

print(json.dumps(yamlsheet, indent=4))