from faker import Faker
from random import randint
import requests
import time

fake = Faker('en_US')
url = "http://localhost:3008/api/authAdmin/register"
time1 = time.time()
def register():
    for _ in range(100):
        my_dic = {"firstname": fake.first_name(),
                  "lastname": fake.last_name(),
                  "username":fake.first_name() + str(randint(100000, 990000)),
                  "email": fake.email(),
                  "password": randint(1000, 9999),
                  "isadmin": 0
                  }
        print(my_dic)
        response = requests.post(url, my_dic)
        print(response.json())
        print(response.status_code)
        if (response.status_code == 200):
            print(response.json())
            with open('test_user.txt', "a") as f:
                f.writelines(str(my_dic))
                f.write('\n')
                f.close()

#register()
time2 = time.time()

delta = time2 - time1
print(delta)




