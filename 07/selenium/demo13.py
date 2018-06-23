# coding: utf-8

from selenium import webdriver
import time


# back()和forward()
browser = webdriver.Firefox()
browser.get('https://www.baidu.com')
browser.get('https://www.taobao.com')
browser.get('https://www.zhihu.com')
browser.back()
time.sleep(1)
browser.forward()
