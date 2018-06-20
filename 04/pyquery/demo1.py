# coding: utf-8


# 字符串初始化
html = '''
    <div>
        <ul>
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html">third item</a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('li'))
