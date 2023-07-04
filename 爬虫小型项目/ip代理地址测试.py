# -*- coding: utf-8 -*-
# time:2022/11/15 15:34
# file ip代理地址测试.py
# outhor:czy
# email:1060324818@qq.com


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromeOptions = webdriver.ChromeOptions()

browser = webdriver.Edge("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\msedgedriver.exe")
    browser.get(url)
    #必须放在这里，用来等待加载完成
    time.sleep(10)
    pageSource = browser.page_source
    if pageSource != "":
        print("爬取成功")
    return pageSource

# 设置代理
chromeOptions.add_argument("--proxy-server=http://202.20.16.82:10152")
# 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
browser = webdriver.Chrome(chrome_options = chromeOptions)

# 查看本机ip，查看代理是否起作用
browser.get("http://httpbin.org/ip")
print(browser.page_source)

# 退出，清除浏览器缓存
browser.quit()