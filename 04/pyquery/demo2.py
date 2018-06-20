# coding: utf-8

from pyquery import PyQuery as pq

# 初始化还可以是url链接
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))
