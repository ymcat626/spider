# coding: utf-8

import requests


r = requests.get('https://github.com/favicon.ico')
print(r.text)
print(r.content)