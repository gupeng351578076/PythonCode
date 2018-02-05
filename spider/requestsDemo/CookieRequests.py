__author__ = 'mocy'
import requests
# s = requests.session()
# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

s = requests.session()
s.headers.update({'x-test':'true'})
r = s.get('http://httpbin.org/headers',headers={'x-test2':'true'})
# r = s.get('http://httpbin.org/headers',headers={'x-test2':None})
print(r.text)