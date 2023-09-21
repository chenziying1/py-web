# -*- coding: utf-8 -*-
# time:2023/6/1 13:30
# file index.py
# outhor:czy
# email:1060324818@qq.com


"""
需求：爬取https://www.mandaoo.com/里面的动漫视频

1.指定动漫
步骤：
    1.创造url
    2.爬取html文件
    3.解析html文件，拿到url链接
    4.保存文件
"""
import re
import time

import  requests


import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#1.创造url
def create_url(data_url):
    urls = [data_url]
    for i in range(1,15):
        new_url = data_url[:-6]+str(i)+".html"
        urls.append(new_url)
    return urls

#2.爬取html文件
def paqu_html(url):
    driver = webdriver.Edge(executable_path='msedgedriver.exe')
    driver.get(url)
    driver.set_window_size(1296, 696)
    driver.switch_to.frame(0)
    driver.switch_to.frame(0)
    time.sleep(7)
    element = driver.find_element(By.CSS_SELECTOR, "#a1 > .dplayer-controller-mask")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.CSS_SELECTOR, "#a1 .dplayer-video")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.ID, "a1").click()
    driver.find_element(By.CSS_SELECTOR, ".dplayer-icon > svg").click()
    driver.find_element(By.CSS_SELECTOR, ".dplayer-icon > svg > path").click()
    driver.find_element(By.CSS_SELECTOR, ".dplayer-icon > svg").click()
    html = driver.page_source
    driver.close()
    return html



#3.解析html文件，拿到url链接
def jiexi_html(text):
    text = str(text)
    url = re.findall('<video class="dplayer-video dplayer-video-current" webkit-playsinline="" x-webkit-airplay="allow" playsinline="" preload="metadata" src="(.*?)\n',text)[0]
    return url

#4.保存文件
def save_file(url,filename):
    file_mp4 = requests.get(url).content
    with open(filename+".mp4","wb+") as f:
        f.write(file_mp4)
    f.close()
    return

data_url = "https://www.mandaoo.com/man_v/99196-0-0.html" #起始url地址
urls = create_url(data_url)
a = 0
for i in urls:
    a += 1
    html_text = paqu_html(i)
    url = jiexi_html(html_text)
    save_file(url, "天体的秩序"+str(a))





