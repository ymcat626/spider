# coding: utf-8

from selenium import webdriver
import time


# 使用execute_script来调用js
browser = webdriver.Firefox()
browser.get('https://www.zhihu.com')
time.sleep(1)
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
