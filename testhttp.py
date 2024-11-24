import json
import requests
import timeit

def BenchMark():
    rawRes = requests.get("http://localhost:8080/getAppointments")
    res = json.loads(rawRes.text)
    # print(json.dumps(res, indent=1))

if __name__ == "__main__":

    print(timeit.timeit(
                    stmt=BenchMark,
                    number=10))
