from concurrent.futures import ThreadPoolExecutor
import requests
from timer import timer
import time
import json
import random
URL = 'http://localhost:3008/api/authAdmin/login'
# with open('readme.txt', "r") as f:
#     for line in f:
#         lines = f.readlines()
#         print(lines)
    # for line in f:

    # line = random.choice(result)
    # print(line)
    # lines = random.choices(result, k=150)
    # print(lines[0][5])
    # f.close()


    # for line in result:
    #     for _ in range(150):
    #         word = random.choices(line, k=150)
    #         print(word)
    #         # print(word[5])
    #         # print(word[9])
    # f.close()


def fetch(session, url):
    data = {"username": "Justin60", "password": 7300}
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