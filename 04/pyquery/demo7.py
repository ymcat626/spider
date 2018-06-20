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
doc = pq(html)

# 对于单个节点，直接打印输出即可
li = doc('.item-0.active')
print(li)
print(type(li))

# 对于多个节点的结果，我们就需要遍历
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))
