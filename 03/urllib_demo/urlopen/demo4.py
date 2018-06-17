# coding: utf-8

import urllib.request


# timeout参数，用于设置超时时间
response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
print(response.read())
