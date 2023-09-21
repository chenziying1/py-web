# -*- coding: utf-8 -*-
# time:2023/8/1 11:49
# file index.py
# outhor:czy
# email:1060324818@qq.com

import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#--------------------------------------------------------------
# 爬取页面的headers
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }


#--------------------------------------------------------------
# 获取具体页面的url
html_content = requests.get('https://pubmed.ncbi.nlm.nih.gov/?term=human&page=1').text
soup = BeautifulSoup(html_content, 'html.parser')
a_list = soup.find_all('a', class_='docsum-title')
href_value = []

for i in a_list:
    href_value.append("https://pubmed.ncbi.nlm.nih.gov"+i['href'])


#-----------------------------------------------------------------
# 校验是否是真的邮箱地址
def extract_email_addresses(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_addresses = re.findall(pattern, text)
    return email_addresses


#-----------------------------------------------------------------
# 获取外部连接
def find(next_url):
    html_content = requests.get(next_url,headers = headers).text
    soup = BeautifulSoup(html_content, 'html.parser')
    email = soup.find('a',class_="oemail").get_text(strip=True)
    return email


#-----------------------------------------------------------------
for url in href_value:
    try:
        html_content = requests.get(url,headers = headers).text
        soup = BeautifulSoup(html_content, 'html.parser')
        span_contents = [li.get_text() for li in soup.find_all('li') ]

        emails = {}
        for text in span_contents:
            email_addresses = extract_email_addresses(text)
            if email_addresses:
                for email in email_addresses:
                    emails[url] = email

        if emails:
            print(emails)
        else:
            try:
                next_url = soup.find('a',class_="id-link")['href']
                email_addresses = find(next_url)
                emails[url] = email_addresses
                print(emails)
            except:
                next_url = soup.find('div', class_="full-text-links-list").find('a')['href']
                paths = "D:\\egde\\edgedriver_win64 (2)\\msedgedriver.exe"
                driver = webdriver.Edge(executable_path=paths)
                driver.get(next_url)
                html = driver.page_source
                email_addresses2 = extract_email_addresses(html)
                emails[url] = email_addresses2
                print(emails)
                driver.close()

    except:
        print("是外部连接")



