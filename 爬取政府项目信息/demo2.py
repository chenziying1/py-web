# -*- coding: utf-8 -*-
# time:2023/7/26 12:43
# file demo2.py
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
# self.driver.find_element(By.NAME, "username").send_keys("17754928264")
# self.driver.find_element(By.NAME, "password").send_keys("gujiguji0830")
time.sleep(20)
# 获取页面上所有的文本信息
try:
    with open("url.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        for url in lines:
            driver.get(url)
            full_page_text = driver.execute_script("return document.documentElement.innerText")

            full_page_text=full_page_text.replace('\t', '\n')
            full_page_text = full_page_text.replace(' ', '\n')
            text_list = [t.strip() for t in full_page_text.split('\n') if t.strip()]

            text_list.append("下面是资金来源")
            try:
                # 查找具有给定id属性的td元素
                td_element1 = driver.find_element(By.ID, 'bjzfys')
                td_element2 = driver.find_element(By.ID, 'czbz')
                td_element3 = driver.find_element(By.ID, 'qyzc')
                td_element4 = driver.find_element(By.ID, 'yhdk')
                td_element5 = driver.find_element(By.ID, 'qtjrtz')
                td_element6 = driver.find_element(By.ID, 'jmcz')
                td_element7 = driver.find_element(By.ID, 'qtqd')
                td_element8 = driver.find_element(By.ID, 'dd')

                # 获取td元素的完整标签
                td_outer_html1 = td_element1.get_attribute('outerHTML')
                td_outer_html2 = td_element2.get_attribute('outerHTML')
                td_outer_html3 = td_element3.get_attribute('outerHTML')
                td_outer_html4 = td_element4.get_attribute('outerHTML')
                td_outer_html5 = td_element5.get_attribute('outerHTML')
                td_outer_html6 = td_element6.get_attribute('outerHTML')
                td_outer_html7 = td_element7.get_attribute('outerHTML')
                td_outer_html8 = td_element8.get_attribute('outerHTML')

                text_list.append(td_outer_html1)
                text_list.append(td_outer_html2)
                text_list.append(td_outer_html3)
                text_list.append(td_outer_html4)
                text_list.append(td_outer_html5)
                text_list.append(td_outer_html6)
                text_list.append(td_outer_html7)
                text_list.append(td_outer_html8)
            except Exception as e:
                print(f"Error: {e}")

            with open("data2.txt", "a+", encoding="utf-8") as f:
                f.write(str(text_list))
            f.close()

            print(text_list)
            print("-------------------------------")
except Exception as e:
    print(f"Error: {e}")

# 关闭浏览器
driver.quit()




