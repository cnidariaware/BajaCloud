from GetSchedulePackager import getSchedulePackager
from postSelectAppointment import SelectAppointment
import json

if __name__ == "__main__":
    print("hello")
    print(json.dumps(getSchedulePackager(), indent=4))
    print(json.dumps(SelectAppointment("10:00 am"), indent=4))