from GetSchedulePackager import getSchedulePackager
from postSelectAppointment import SelectAppointment
import json

if __name__ == "__main__":
    print(getSchedulePackager())
    print(SelectAppointment("10:00 am"))