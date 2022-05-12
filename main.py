from faker import Faker
from random import randint
import requests
import time

fake = Faker('en_US')
url = "http://localhost:3008/api/authAdmin/register"
time1 = time.time()
for _ in range(10):
    my_dic = {"firstname" : fake.first_name(),
              "lastname": fake.last_name(),
              "username": fake.first_name()+str(randint(10, 99)),
              "email": fake.email(),
              "password": randint(1000, 9999),
              "isadmin": False
              }
    print(my_dic)
    response = requests.post(url, my_dic)
    print(response.json())
    print(response.status_code)
    if(response.status_code == 200):
        print(response.json())
        with open('readme.txt', "a") as f:
            f.writelines(str(my_dic))
            f.write('\n')
            f.close()

time2 = time.time()
delta = time2 - time1
print(delta)



# file= open("C:\\Users\\hamed\\PycharmProjects\\test_api\\readme.txt",'r')
# json_input = file.read()
# requests_json = json.loads(file.read())
# print(requests_json)
