from concurrent.futures import ThreadPoolExecutor
import requests
from timer import timer
import time
import json
import random
URL = 'http://localhost:3008/api/authAdmin/login'
from main import register

with open('test_user.txt') as f:
    lines = f.readlines()
print("Done")
def fetch(session, url):
    global lines
    data = lines[random.randint(0, len(lines))].strip().replace("'", "\"")
    data = json.loads(data)
    with session.post(url, data) as response:
        print(response.json())




time1 = time.time()


@timer(1, 1)
def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session]*100, [URL]*100)
            executor.shutdown(wait=True)


time2 = time.time()
delta = time2 - time1
print(delta)
