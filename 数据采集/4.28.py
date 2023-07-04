# -*- coding: utf-8 -*-
# time:2023/4/28 17:54
# file 4.28.py
# outhor:czy
# email:1060324818@qq.com

from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='D:\\BaiduNetdiskDownload\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()