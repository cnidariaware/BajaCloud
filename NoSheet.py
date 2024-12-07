import openpyxl
import yaml
import json
import datetime
from openpyxl.styles import Font, Border, Side, PatternFill
from openpyxl.formatting.rule import FormulaRule


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
  - Are you available for team meetings/work days? Saturdays 10 am - 4 pm: "No" #add condiftional formatting for no to make whole line red
Interview TimeTable:
  - Date: 9/16/2024
  - Meeting Duration: 30 min
  - Start Time Slot: 10:00:00 AM
  - Slot: 1
  - Interviewee Name (What to call them): Steve
  - Interviewee Email: steve.the.bug@ucalgary.ca
  - Category (if not general): Test
  - Interviewer(s) Name(s): Example
  - Status: Dropdown (Options in datahelp) #default is Unknown
Data Helper:
  - Status Dropdown:
      - Unknown
      - Done
      - No Show
      - Cancelled/Moved
  - How to Add Dropdown: Go into data, click data validation, select list then select the area you want to get values from in the formula spot
    """

    yamlsheet = yaml.safe_load(yamlraw)

    # print(json.dumps(yamlsheet, indent=4))

    year_donation = int(str(datetime.datetime.now().year)[2:]) # gets the last two digits of the current year then adds 1 for the current season
    file_name = f"OR{year_donation + 1}-L-Interview Data.xlsx" # name based off the 2025 naming system

    # border style
    border = Border( # defualt behaviour is thin
        left=Side(style='thin'), 
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    # for conditional formatting
    red_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")

    # create workbook in memory
    work_book = openpyxl.Workbook()
    
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


        example_data = [list(data.values())[0] for data in title_list]

        for col_num, data in enumerate(example_data, start=1):
            if isinstance(data, list):
                row_num = 2
                for item in data:
                    cell = sheet.cell(row=row_num, column=col_num)
                    cell.value = item
                    row_num += 1
            else:
                cell  = sheet.cell(row=2, column=col_num)
                cell.value = data
                if data == "Dropdown (Options in datahelp)":
                    cell.value = "Unknown"

        if sheet.title == "Recruitment Responses":
            sheet.conditional_formatting.add("A2:I2", FormulaRule(formula=['=$I2="No"'], fill=PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")))




            

    # save to storage
    work_book.save(file_name)

if __name__ == "__main__":
    NoSheet()