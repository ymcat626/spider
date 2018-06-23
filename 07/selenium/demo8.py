# coding: utf-8

from selenium import webdriver
from selenium.webdriver import ActionChains


# 使用get_attribute()来获取节点的属性
browser = webdriver.Firefox()
url = 'https://www.zhihu.com'
browser.get(url)
logo = browser.find_element_by_class_name('Icon--logo')
print(logo)
print(logo.get_attribute('class'))
