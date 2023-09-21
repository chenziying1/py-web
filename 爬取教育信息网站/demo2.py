# -*- coding: utf-8 -*-
# time:2023/7/23 11:20
# file demo2.py
# outhor:czy
# email:1060324818@qq.com
import json
import re

import chardet
import requests
from bs4 import BeautifulSoup

url = 'https://www.educationagentsguide.com/china/nanning_sino-oveseas_consultants_co_ltd_nanning_education_agents.htm'

# 发送HTTP GET请求并获取响应内容
response = requests.get(url)
encoding = chardet.detect(response.content)['encoding']
html = response.content.decode(encoding)

# 解析HTML文档并提取所需内容
soup = BeautifulSoup(html, 'html.parser')
td_list = soup.find_all('td')
h1_text = soup.find('h1', {'align': 'center'}).text

# 格式化处理文本内容
td_text_list=[]
for td in td_list:
    for text in td.strings:
        target = text.strip()
        if target == '' or 'Qualifications' in target or target == "|" or "Qualification" in target or '\n\t' in target \
                or target == "Website:" or target == "Message:" or target == "Telephone:":
            continue
        else:
            td_text_list.append(target)
h1_text = h1_text.strip()

json_data = {'title': h1_text, 'Address': '该页面未显示地址信息', 'Website': '该页面未显示网址信息',
             'Email': '该页面未显示邮件信息', 'phone': '该页面未显示电话信息'}
pattern = re.compile(r'^(\d{3}-|\(\d{3}\) )?\d{3}-\d{4}$')
pattern2 = re.compile(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')
pattern3 = re.compile(r'^https?://(?:\d{1,3}\.){3}\d{1,3}|\b(?:\d{1,3}\.){2}\d{1,3}\b')
address_pattern = r"[A-Za-z\s\d,&]+,\s[A-Za-z\s\d,&]+,\s[A-Za-z\s\d,&]+,\s\d{6},\s[A-Za-z\s]+"

for i in range(len(td_text_list)):
    if td_text_list[i] == "Address" or "Address" in td_text_list[i]:
        # Extracting address from the list
        address = re.sub('Education Agents', '', td_text_list[i + 1]).strip()
        json_data["Address"] = address
    elif td_text_list[i] == "Website" or "website" in td_text_list[i]:
        # Extracting website from the list
        website = td_text_list[i + 1].strip()
        json_data["Website"] = website
    elif td_text_list[i] == "Email" :
        # Extracting email from the list
        email = td_text_list[i + 1].strip()
        json_data["Email"] = email
    elif "Telephone" in td_text_list[i] or "Tel" in td_text_list[i] or "Ph" in td_text_list[i]:
        # Extracting phone number from the list
        phone = td_text_list[i + 1].strip()
        json_data["phone"] = phone
    elif re.match(pattern,td_text_list[i]):
        phone = td_text_list[i].strip()
        json_data["phone"] = phone
    elif re.match(pattern2,td_text_list[i]):
        email = td_text_list[i].strip()
        json_data["Email"] = email
    elif re.match(address_pattern,td_text_list[i]):
        address = re.sub('Education Agents', '', td_text_list[i]).strip()
        json_data["Address"] = address
    elif re.match(pattern3,td_text_list[i]):
        website = td_text_list[i].strip()
        json_data["Website"] = website


# Printing the JSON data
print(td_text_list)
print(json_data)
print(h1_text)




