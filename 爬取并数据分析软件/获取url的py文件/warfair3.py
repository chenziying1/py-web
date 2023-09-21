# -*- coding: utf-8 -*-
# time:2023/7/29 12:26
# file warfair3.py
# outhor:czy
# email:1060324818@qq.com
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

target_list = [
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=10',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=11',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=12',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=13',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=14',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=2',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=3',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=4',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=5',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=6',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=7',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=8',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=9',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=10',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=11',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=12',
                'https://www.wayfair.com/brand/bnd/horow-b62399.html',
                'https://www.wayfair.com/brand/bnd/horow-b62399.html?curpage=2',
                'https://www.wayfair.com/brand/bnd/mohome-b63429.html',
                'https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html',
                "https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html?curpage=2",
                "https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html?curpage=3",
                "https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html?curpage=4",
                "https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html?curpage=5",
                "https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html?curpage=6",
               'https://www.wayfair.com/keyword.php?keyword=Woodbrige']

# 打开网站
while len(target_list) > 0:
    paths = "D:\\egde\\edgedriver_win64 (2)\\msedgedriver.exe"
    options = webdriver.EdgeOptions()
    options.use_chromium = True  # 使用 Chromium 内核
    driver = webdriver.Edge(options=options,executable_path=paths)
    driver.get(target_list[0])
    time.sleep(20)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    product_links = soup.find_all('a', {'class': '_1yxeg5wb_713'})
    jump_links = [link['href'] for link in product_links]
    print(jump_links)
    print("--------------------------")
    if len(jump_links) > 0:
        with open("../资源/wayfair_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(jump_links) + "\n")
        f.close()
        target_list.pop(0)
        time.sleep(3)
        print(len(target_list))
    else:
        driver.quit()
        time.sleep(3)

