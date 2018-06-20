# coding: utf-8

from pyquery import PyQuery as pq


# parent()用来获取父节点
html = '''
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html">third item</a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
'''
doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)
