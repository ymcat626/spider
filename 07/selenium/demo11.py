# coding: utf-8

from selenium import webdriver


# 隐式等待
browser = webdriver.Firefox()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)
