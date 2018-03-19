__author__ = 'mocy'
import json
l = ['iplaypython', [1, 2, 3], {'name', 'xiaoming'}]
encoded_json = json.dumps(l)
print(repr(l))
print(encoded_json)
