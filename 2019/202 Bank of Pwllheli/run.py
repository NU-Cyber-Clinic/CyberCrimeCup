import requests
import time
import datetime

while True:
	url = "http://202.cybertrial.co.uk/account"

	#payload = "pay_amount=99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999&pay_name=N.%20Null&pay_sortcode=10-20-20&pay_account=10001218&pay_reference=Food"
	headers = {
		#'Content-Type': "application/x-www-form-urlencoded",
		'Cookie': "PHPSESSID=eo9qs1vp3shikcu24fjoogukma"
	}

	response = requests.request("POST", url, headers=headers)

	#print(response.text)
	print("Req " + str(datetime.datetime.now().time()))
	time.sleep(2)