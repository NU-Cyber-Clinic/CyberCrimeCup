import requests


class Session:
    def __init__(self, url):
        self.session = self.create_session(url)
        
    def create_session(self, url):
        api_key = "CHANGE_ME"

        s = requests.session()
        s.get(url + '?mykey=' + api_key)

        return s

    def get_cookie(self):
        return "PHPSESSID=" + self.session.cookies.get_dict()["PHPSESSID"]


url = "http://1.cybertrial.co.uk/"
sess = Session(url)
print(sess.get_cookie())
