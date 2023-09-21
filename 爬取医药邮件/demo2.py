# -*- coding: utf-8 -*-
# time:2023/8/3 12:33
# file demo2.py
# outhor:czy
# email:1060324818@qq.com

import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_email_addresses(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_addresses = re.findall(pattern, text)
    return email_addresses
emails = {}
next_url = "https://onlinelibrary.wiley.com/doi/10.1111/cxo.12839"
paths = "D:\\egde\\edgedriver_win64 (2)\\msedgedriver.exe"
driver = webdriver.Edge(executable_path=paths)
driver.get(next_url)
html = driver.page_source
email_addresses2 = extract_email_addresses(html)
emails[next_url] = email_addresses2
print(emails)
