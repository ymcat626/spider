# coding: utf-8

from urllib.request import urlparse


result = urlparse('http://www.baidu.com/index.html#comment', allow_fragments=False)
print(result)
print(result.scheme, result[0], result.netloc, result[1])