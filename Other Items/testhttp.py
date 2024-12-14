import json
import requests
import timeit

def BenchMarkServer():
    rawRes = requests.get("http://localhost:8080/getAppointments")
    res = json.loads(rawRes.text)
    #print(json.dumps(res, indent=1))

def BenchMarkDjango():
    rawRes = requests.get("http://127.0.0.1:8000/getAppointments")
    res = json.loads(rawRes.text)
    #print(json.dumps(res, indent=1))

if __name__ == "__main__":
    test = 1
    if test:
        djangoTime = timeit.timeit(stmt=BenchMarkDjango, number=1000)
        # pythonTime = timeit.timeit(stmt=BenchMarkServer, number=10)
        print(f"FastAPI: {djangoTime}\nPython: ")
    
    reqbody = {
        "body": {"message": "hello"}
    }
    # rawRes = requests.post("http://localhost:8000/SelectInterview", reqbody)
