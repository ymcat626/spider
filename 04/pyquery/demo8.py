# coding: utf-8

from pyquery import PyQuery as pq


html = '''
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html">third item</a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul
    </div>
'''
# 获取属性
# 第一种方法
doc = pq(html)
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))

# 第二种方法
print(a.attr.href)
