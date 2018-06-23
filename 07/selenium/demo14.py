# coding: utf-8

from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://www.zhihu.com')
print(browser.get_cookies())
cookie = {
    'name': 'name',
    'domain': 'www.zhihu.com',
    'value': 'germey',
}
browser.add_cookie(cookie)
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
