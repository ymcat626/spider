# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By


# 通用方法find_element()
browser = webdriver.Firefox()
browser.get('https://www.taobao.com')
input_first = browser.find_element(By.ID, 'q')
print(input_first)
browser.close()
