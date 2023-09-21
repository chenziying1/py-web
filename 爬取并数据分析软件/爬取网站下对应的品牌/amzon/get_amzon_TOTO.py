# -*- coding: utf-8 -*-
# time:2023/7/30 8:26
# file get_amzon.py
# outhor:czy
# email:1060324818@qq.com

import json
import sqlite3
from datetime import datetime
import time
import openpyxl
import requests
from bs4 import BeautifulSoup

#----------------------------

with open("amzon_TOTO_url.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
f.close()

with open("cookie.txt", "r", encoding="utf-8") as f:
    b = f.readline()
    b = b.strip()
f.close()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookie': b,
}

sql_data=[]
while len(a) > 0:
    url = a[0].strip()
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    if response.status_code != 200:
        continue
    data = {
        '更新时间': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        '直达的落地页': url,
        '产品评分': '无评分',
        '目前售价': '无售价',
        '评论数量': '无评论',
        '主图': '无主图',
        '商品名称': '无商品名称',
    }

    try:
        pingfeng = soup.find_all('span', class_='a-icon-alt')[0].get_text(strip=True)
        if "US" in pingfeng:
            data["产品评分"] = "无评分"
        else:
            data["产品评分"] = pingfeng
    except:
        pass

    try:
        shoujia = soup.find('span', class_='a-price-whole').get_text(strip=True)
        data["目前售价"] = shoujia
    except:
        pass

    try:
        pinglunshuliang = soup.find('span', id='acrCustomerReviewText').get_text(strip=True)
        data["评论数量"] = pinglunshuliang
    except:
        pass

    try:
        img_tag = soup.find('div', id='imgTagWrapperId').find('img')['src']
        data["主图"] = img_tag
    except:
        pass

    try:
        mingcheng = soup.find_all('span', class_='a-size-large product-title-word-break')[0].get_text(strip=True)
        data["商品名称"] = mingcheng
    except:
        try:
            mingcheng = soup.find_all('span', id='productTitle')[0].get_text(strip=True)
            data["商品名称"] = mingcheng
        except:
            with open("../cookie失效.txt", "a+", encoding="utf-8") as f:
                f.write(str(url) + "\n")
            f.close()
    sql_data.append(data)
    a.pop(0)


for data in sql_data:
    db_file = '../amzon.db'
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT 目前售价, 本次更新review数量 FROM amzon_TOTO WHERE 商品名称 = ?", (data['商品名称'],))
    row = cursor.fetchone()
    if row:
        print("目前售价:", row[0])
        print("本次更新review数量:", row[1])
        cursor.execute("UPDATE amzon_TOTO SET 目前售价 = ? WHERE 商品名称 = ?", (data['目前售价'], data['商品名称']))
        cursor.execute("UPDATE amzon_TOTO SET 本次更新review数量 = ? WHERE 商品名称 = ?", (data['评论数量'], data['商品名称']))
        cursor.execute("UPDATE amzon_TOTO SET 上次同步前售价 = ? WHERE 商品名称 = ?", (row[0], data['商品名称']))
        cursor.execute("UPDATE amzon_TOTO SET 上次同步时数量 = ? WHERE 商品名称 = ?", (row[1], data['商品名称']))
        cursor.execute("UPDATE amzon_TOTO SET 更新时间 = ? WHERE 商品名称 = ?", (data['更新时间'], data['商品名称']))
    else:
        insert_query = ("INSERT INTO amzon_TOTO (主图, 目前售价, 上次同步前售价, 本次更新review数量, 上次同步时数量, 更新时间, 直达的落地页, 产品评分, 商品名称) "
                        "VALUES (?, ?, '', ?, '', ?, ?, ?, ?)")
        cursor.execute(insert_query,
                       (data['主图'], data['目前售价'], data['评论数量'], data['更新时间'], data['直达的落地页'], data['产品评分'],
                        data['商品名称']))
    conn.commit()

    cursor.close()
    conn.close()
