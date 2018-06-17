# coding: utf-8

import urllib.request
import urllib.parse


# urllib.parse.urlencode()可以将参数从字典转换为字符串
# bytes()转字节流
data = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response)
print(response.read().decode('utf-8'))
