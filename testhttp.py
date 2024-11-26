import json
import requests
import timeit

def BenchMarkServer():
    rawRes = requests.get("http://localhost:8080")
    res = json.loads(rawRes.text)
    #print(json.dumps(res, indent=1))

def BenchMarkDjango():
    rawRes = requests.get("http://localhost:8000/polls/test")
    res = json.loads(rawRes.text)
    #print(json.dumps(res, indent=1))

if __name__ == "__main__":
    djangoTime = timeit.timeit(stmt=BenchMarkDjango, number=10)
    pythonTime = timeit.timeit(stmt=BenchMarkServer, number=10)
    print(f"Django: {djangoTime}\nPython: {pythonTime}")