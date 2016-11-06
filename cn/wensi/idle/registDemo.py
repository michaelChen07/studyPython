#encoding=utf-8
import requests
import json

print "register------"
data = json.dumps({'username': 'wqcz250801', 'password': 'a12345678', 'email': 'lily@qq.com'}) #需每次修改username
r = requests.post('http://103.36.173.17:8080/register/', data = data)
print r.status_code
print r.text
print type(r.json())
print str(r.json())
