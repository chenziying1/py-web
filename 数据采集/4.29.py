# -*- coding: utf-8 -*-
# time:2023/4/29 16:40
# file 4.29.py
# outhor:czy
# email:1060324818@qq.com

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.PhantomJS(executable_path='D:\\BaiduNetdiskDownload\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get('https://pythonscraping.com/pages/itsatrap.html')
#assert "Monty Python" in driver.title
links = driver.find_elements_by_tag_name("a")
for link in links:
    if not link.is_displayed():
        print("The link " + link.get_attribute("href") + " is a trap")

fields = driver.find_elements_by_tag_name("input")
for field in fields:
    if not field.is_displayed():
        print("Do not change value of "+field.get_attribute("name"))
