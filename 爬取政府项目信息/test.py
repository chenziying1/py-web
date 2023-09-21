# -*- coding: utf-8 -*-
# time:2023/7/25 19:46
# file test.py
# outhor:czy
# email:1060324818@qq.com
import requests
from bs4 import BeautifulSoup

url = "http://cqchengshigengxin.com/csgx/xmxx/details/f9c7997c191f44a0842a0d74e60c8b7c"
with open("cookie.txt","r",encoding="utf-8" ) as f:
    a = f.readline()
    a = a.strip()
f.close()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookie': a,
    'Host': 'cqchengshigengxin.com',
    'Referer': 'http://cqchengshigengxin.com/csgx/xmxx/zf',
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')
text = soup.get_text()
text_list = [t.strip() for t in text.split('\n') if t.strip()]


# 使用BeautifulSoup解析网页
soup2 = BeautifulSoup(response.content, 'html.parser')

# 获取所有表格元素
tables = soup2.find_all('table')

# 获取所有被<span>标签包裹的文本
spans = soup2.find_all('span')

# 获取页面中的所有文本信息
for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        tds = row.find_all('td')
        for td in tds:
            # 判断td标签内是否有文本，如果没有则使用td.string获取标签内部的文本
            if td.text.strip() == '':
                text_list.append(td.string.strip())
            else:
                text_list.append(td.get_text().strip())
for span in spans:
    text_list.append(span.get_text().strip())


print(text_list)

