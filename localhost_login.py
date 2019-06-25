from lxml.html import fromstring
import requests

s=requests.Session()
r=s.get('http://127.0.0.1:8081/PrivEscalation/')

page=fromstring(r.text)
inputs=page.forms[0].inputs

for input in inputs:
    if input.type=='text':
        username=input.name
        if input.type=='password':
         password=input.name

payload = {username: 'admin', password: 'admin'}

s.post('http://127.0.0.1:8081/PrivEscalation/j_security_check', data=payload)