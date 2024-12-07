import openpyxl
import yaml
import json
import datetime
from openpyxl.styles import Font, Border, Side


def NoSheet():
    # sheet with an example properites
    yamlraw = """
Recruitment Responses:
  - Frist Name (What we should call them): Steve
  - Last Name: the Bug
  - Ucalgary Email: steve.the.bug@ucalgary.ca
  - What Subsystem/SubTeam are you interested in?: |
      Chassis 
      Ergonomics
      Suspension
      Steering
      Powertrain
      Final Drive
      Any Mechanical
      Business - Content Creation
      Business - Business Relations
      Software
  - Major: General (1st Year)
  - Academic Year: 1st
  - Why are you interested in joining UCalgary BAJA?: Example Interest
  - Where did you hear about us?: Testing
  - Are you available for team meetings/work days? Saturdays 10 am - 4 pm: Yes #add condiftional formatting for no to make whole line red
Interview TimeTable:
  - Date: 9/16/2024
  - Meeting Duration: 30 min
  - Start Time Slot: 10:00:00 AM
  - Slot: 1
  - Interviewee Name (What to call them): Steve
  - Interviewee Email: steve.the.bug@ucalgary.ca
  - Category (if not general): Test
  - Interviewer(s) Name(s): Example
  - Status: Dropdown (Options in datahelp) #default is Unkown
Data Helper:
  - Status Dropdown:
      - Unknown
      - Done
      - No Show
      - Cancelled/Moved
    """

    yamlsheet = yaml.safe_load(yamlraw)

    print(json.dumps(yamlsheet, indent=4))

    year_donation = int(str(datetime.datetime.now().year)[2:]) + 1 # gets the last two digits of the current year then adds 1 for the current season
    file_name = f"OR{year_donation}-L-Interview Data.xlsx" # name based off the 2025 naming system

    sheet_names = [name for name in yamlsheet.keys()]

    # border style
    border = Border(
        left=Side(style='medium'),
        right=Side(style='medium'),
        top=Side(style='medium'),
        bottom=Side(style='medium')
    )

    # create workbook in memory
    work_book = openpyxl.Workbook()
    
    if len(sheet_names) > 0:
        # remove default sheet
        default_sheet = work_book.active
        work_book.remove(default_sheet)

        for sheet_name, title_list in yamlsheet.items():
            # add standard sheets
            sheet = work_book.create_sheet(sheet_name)

            titles =  [list(title.keys())[0] for title in title_list]

            for col_num, title in enumerate(titles, start=1):
                cell  = sheet.cell(row=1, column=col_num)
                cell.value = title

                cell.font = Font(bold=True)
                cell.border = border

            

    # save to storage
    work_book.save(file_name)

if __name__ == "__main__":
    NoSheet()