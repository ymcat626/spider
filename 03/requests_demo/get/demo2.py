# coding: utf-8

import requests


r = requests.get('http://httpbin.org/get')
print(r.text)
