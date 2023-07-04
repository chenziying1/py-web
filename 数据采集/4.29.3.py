# -*- coding: utf-8 -*-
# time:2023/4/29 18:16
# file 4.29.3.py
# outhor:czy
# email:1060324818@qq.com
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

"""driver = webdriver.PhantomJS(executable_path='D:\\BaiduNetdiskDownload\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get("http://pythonscraping.com/pages/files/form.html")

fristnameField = driver.find_element_by_name("firstname")
lastnameField = driver.find_element_by_name("lastname")
submitButton = driver.find_element_by_id("submit")"""

def 方法1():
    fristnameField.send_keys("Ryan")
    lastnameField.send_keys("Mitchell")
    submitButton.click()

def 方法2():
    actions = ActionChains(driver).click(fristnameField).send_keys("Ryan").click(lastnameField).send_keys("Mitchell").send_keys(Keys.RETURN)
    actions.perform()

"""方法2()
print(driver.find_element_by_tag_name("body").text)
driver.close()"""

driver = webdriver.PhantomJS(executable_path='D:\\BaiduNetdiskDownload\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
driver.get('http://www.pythonscraping.com/')
driver.get_screenshot_as_file('pythonscraping.png')
