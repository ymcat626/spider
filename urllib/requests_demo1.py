# coding: utf-8
import requests

r = requests.get('http://httpbin.org/get')
# r = requests.get('https://www.baidu.com')
print(r.text)