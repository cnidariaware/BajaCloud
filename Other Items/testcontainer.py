import requests
import json

if __name__ == "__main__":
    getres = requests.get("http://bajacloud.ddnsking.com:43443/getAppointments")
    print(getres)
    print(json.dumps(json.loads(getres.text), indent=4))
    # example of a request
    # postdata = {
    #     "intervieweeName": "Brock",
    #     "date": "2024-09-16",
    #     "startTime": "11:00:00",
    #     "intervieweeEmail": "darkicewolf50@gmail.com"
    #     }
    # res = requests.post("http://bajacloud.ddnsking.com:43443/SelectInterview", json.dumps(postdata))
    # print(res)
    # print(res.text)