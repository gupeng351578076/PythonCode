__author__ = 'mocy'
#coding:UTF-8
import requests
# headers = {'Content-type':'application/json'}
# resp = requests.get('https://github.com/timeline.json',headers=headers)
# print(resp.text)

payload = {"key1":"value1","key2":"value2"}
headers = {'Content-type':'application/json'}
resp = requests.post('https://www.github.com/',data=payload,headers=headers)
print(resp.text)