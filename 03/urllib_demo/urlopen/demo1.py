# coding: utf-8
import urllib.request

# 使用urllib.request的urlopen方法
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))

# <class 'http.client.HTTPResponse'>
print(type(response))
