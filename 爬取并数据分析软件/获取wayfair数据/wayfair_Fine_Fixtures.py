# -*- coding: utf-8 -*-
# time:2023/8/7 7:01
# file get_amzon_American_Standard.py
# outhor:czy
# email:1060324818@qq.com

import json
import re
import sqlite3
from datetime import datetime
import time
import openpyxl
import requests
from bs4 import BeautifulSoup
import os
#----------------------------

a,b=[],[]
def get_urlandcookie():
    global a,b
    file_path = os.path.join(os.path.dirname(__file__), "cookie.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        b = f.readline()
        b = b.strip()
    f.close()

    file_path = os.path.join(os.path.dirname(__file__), "wayfair_Fine_Fixtures_url.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            # Remove leading and trailing whitespace characters
            line = line.strip()

            # Remove the enclosing square brackets and split by comma
            elements = line[1:-1].split(', ')
            ans = []
            for i in elements:
                ans.append(i.replace("'",""))
            # Convert each element to an integer
            a+=ans
    f.close()

    return a,b

def get():

    a,b = get_urlandcookie()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Cookie': b,
    }

    sql_data=[]
    while len(a) > 0:
        url = a[0].strip()
        print(url)
        if url == "":
            a.pop(0)
            continue
        try:
            response = requests.get(url, headers=headers, timeout=10)
        except:
            a.pop(0)
            continue
        time.sleep(3)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = {
            '更新时间': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            '直达的落地页': url,
            '产品评分': '无评分',
            '目前售价': '无售价',
            '评论数量': '无评论',
            '主图': '无主图',
            '商品名称': '无商品名称',
            'sku': '暂无',
        }

        try:
            pingfeng = soup.find_all('span', class_='ProductRatingNumberWithCount-rating')[0].get_text(strip=True)
            if "US" in pingfeng:
                data["产品评分"] = "无评分"
            else:
                data["产品评分"] = pingfeng
        except:
            pass

        try:
            shoujia = re.findall('"smallestPurchasableQtyPrice":(.*?),', response.text)[0].get_text(strip=True)
            data["目前售价"] = shoujia
        except:
            pass

        try:
            pinglunshuliang = soup.find('span', class_='ProductRatingNumberWithCount-count ProductRatingNumberWithCount-count--link').get_text(strip=True)
            data["评论数量"] = pinglunshuliang
        except:
            pass

        try:
            img_tag = soup.find('div', class_='_15bab5p0_6101').find('img')['src']
            data["主图"] = img_tag
        except:
            pass

        try:
            mingcheng = soup.find_all('h1', class_='kzv0b81yc_6101 _1yimfeh6_6101 _1yimfehd_6101 _1yimfehj_6101')[0].get_text(strip=True)
            data["商品名称"] = mingcheng
        except:
            try:
                mingcheng = soup.find_all('span', id='productTitle')[0].get_text(strip=True)
                data["商品名称"] = mingcheng
            except:
                with open("../cookie失效.txt", "a+", encoding="utf-8") as f:
                    f.write(str(url) + "\n")
                f.close()
        try:
            ans2 = re.findall('<span>SKU:(.*?)</span>', response.text)
            data['sku'] = ans2
        except:
            pass

        sql_data.append(data)
        print(data)
        a.pop(0)


    for data in sql_data:
        file_path = os.path.join(os.path.dirname(__file__), "wayfair.db")
        db_file = file_path
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT 目前售价, 本次更新review数量 FROM wayfair_Fine_Fixtures WHERE 商品名称 = ?", (data['商品名称'],))
        row = cursor.fetchone()
        if row:
            print("目前售价:", row[0])
            print("本次更新review数量:", row[1])
            cursor.execute("UPDATE wayfair_Fine_Fixtures SET 目前售价 = ? WHERE 商品名称 = ?", (data['目前售价'], data['商品名称']))
            cursor.execute("UPDATE wayfair_Fine_Fixtures SET 本次更新review数量 = ? WHERE 商品名称 = ?", (data['评论数量'], data['商品名称']))
            cursor.execute("UPDATE wayfair_Fine_Fixtures SET 上次同步前售价 = ? WHERE 商品名称 = ?", (row[0], data['商品名称']))
            cursor.execute("UPDATE wayfair_Fine_Fixtures SET 上次同步时数量 = ? WHERE 商品名称 = ?", (row[1], data['商品名称']))
            cursor.execute("UPDATE wayfair_Fine_Fixtures SET 更新时间 = ? WHERE 商品名称 = ?", (data['更新时间'], data['商品名称']))
        else:
            insert_query = ("INSERT INTO wayfair_Fine_Fixtures (sku,主图, 目前售价, 上次同步前售价, 本次更新review数量, 上次同步时数量, 更新时间, 直达的落地页, 产品评分, 商品名称) "
                            "VALUES (?,?, ?, '', ?, '', ?, ?, ?, ?)")
            cursor.execute(insert_query,
                           (data['sku'],data['主图'], data['目前售价'], data['评论数量'], data['更新时间'], data['直达的落地页'], data['产品评分'],
                            data['商品名称']))
        conn.commit()

        cursor.close()
        conn.close()

get()
