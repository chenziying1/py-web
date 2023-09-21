# -*- coding: utf-8 -*-
# time:2023/7/25 22:08
# file test2.py
# outhor:czy
# email:1060324818@qq.com
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://cqchengshigengxin.com/index"

paths = "D:\\egde\\edgedriver_win64 (2)\\msedgedriver.exe"
options = webdriver.EdgeOptions()
options.use_chromium = True  # 使用 Chromium 内核
driver = webdriver.Edge(options=options,executable_path=paths)
driver.get(url)

# 等待加载完成
time.sleep(20)
# 获取页面上所有的文本信息
try:
    driver.get("http://cqchengshigengxin.com/csgx/xmxx/details/13e789e1ab09412e9044d32b4a3cdb79")
    full_page_text = driver.execute_script("return document.documentElement.innerText")
    with open("templates.txt","w",encoding="utf-8") as f:
        f.write(full_page_text)
    f.close()
    full_page_text=full_page_text.replace('\t', '\n')
    full_page_text = full_page_text.replace(' ', '\n')
    text_list = [t.strip() for t in full_page_text.split('\n') if t.strip()]
    # 查找具有给定id属性的td元素
    td_element = driver.find_element(By.ID, 'qyzc')
    """
    <td id="bjzfys"></td>
    <td id="czbz"></td>
    <td id="qyzc">11000</td>
    <td id="yhdk"></td>
    <td id="qtjrtz"></td>
    <td id="jmcz"></td>
    <td id="qtqd"></td>
    <td id="dd"></td>
    """
    # 获取td元素的完整标签
    td_outer_html = td_element.get_attribute('outerHTML')
    print(td_outer_html)
    print(text_list)
except Exception as e:
    print(f"Error: {e}")

# 关闭浏览器
driver.quit()


"""
用id方式获取资金来源
用join的方式编辑地块信息与 result = ''.join(lst[lst.index('备注说明'):lst.index('资金来源')+1])
商业信息表如何搞呢？
"""

