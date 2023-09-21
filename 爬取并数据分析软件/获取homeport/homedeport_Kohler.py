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
import requests
from bs4 import BeautifulSoup
import os


# ----------------------------

def get_urlandcookie():
    a, b = [], []
    file_path = os.path.join(os.path.dirname(__file__), "cookie.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        b = f.readline()
        b = b.strip()
    f.close()

    file_path = os.path.join(os.path.dirname(__file__), "homedeport_Kohler_url.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        a = f.readlines()
    f.close()

    return a, b


def get():
    a, b = get_urlandcookie()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Cookie': b,
    }

    sql_data = []
    while len(a) > 0:
        url = a[0].strip()
        print(url)
        if url == "":
            a.pop(0)
            continue
        try:
            response = requests.get(url, headers=headers)
            with open("1.txt", "w+", encoding="utf-8") as f:
                f.write(response.text)
            f.close()
        except:
            print("456")
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
            pingfeng = soup.find('div', class_='ratings-reviews__accordion-subheader').find_all('span')[0].get_text(
                strip=True)
            if "US" in pingfeng:
                data["产品评分"] = "无评分"
            else:
                data["产品评分"] = pingfeng
        except:
            pass

        try:
            shoujia = soup.find('div', class_='price-format__large price-format__main-price').find_all('span')[
                1].get_text(strip=True)
            data["目前售价"] = shoujia
        except:
            pass

        try:
            pinglunshuliang = soup.find('div', class_='ratings-reviews__accordion-subheader').find_all('span')[
                1].get_text(strip=True)
            data["评论数量"] = pinglunshuliang
        except:
            pass

        try:
            img_tag = soup.find('button', class_='mediagallery__imgblock').find('img')['src']
            data["主图"] = img_tag
        except:
            pass

        try:
            mingcheng = soup.find_all('h1', class_='sui-h4-bold sui-line-clamp-unset')[0].get_text(strip=True)
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
            ans2 = re.findall(
                '<h2 class="sui-font-regular sui-text-xs sui-leading-normal sui-tracking-normal sui-normal-case sui-line-clamp-unset sui-text-left">(.*?)</h2>',
                response.text)[5]
            data['sku'] = ans2
        except:
            pass

        sql_data.append(data)
        print(data)
        a.pop(0)

    for data in sql_data:
        file_path = os.path.join(os.path.dirname(__file__), "homedeport.db")
        db_file = file_path
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT 目前售价, 本次更新review数量 FROM homedeport_Kohler WHERE 商品名称 = ?", (data['商品名称'],))
        row = cursor.fetchone()
        if row:
            print("目前售价:", row[0])
            print("本次更新review数量:", row[1])
            cursor.execute("UPDATE homedeport_Kohler SET 目前售价 = ? WHERE 商品名称 = ?", (data['目前售价'], data['商品名称']))
            cursor.execute("UPDATE homedeport_Kohler SET 本次更新review数量 = ? WHERE 商品名称 = ?",
                           (data['评论数量'], data['商品名称']))
            cursor.execute("UPDATE homedeport_Kohler SET 上次同步前售价 = ? WHERE 商品名称 = ?", (row[0], data['商品名称']))
            cursor.execute("UPDATE homedeport_Kohler SET 上次同步时数量 = ? WHERE 商品名称 = ?", (row[1], data['商品名称']))
            cursor.execute("UPDATE homedeport_Kohler SET 更新时间 = ? WHERE 商品名称 = ?", (data['更新时间'], data['商品名称']))
        else:
            insert_query = (
                "INSERT INTO homedeport_HOROW (sku,主图, 目前售价, 上次同步前售价, 本次更新review数量, 上次同步时数量, 更新时间, 直达的落地页, 产品评分, 商品名称) "
                "VALUES (?,?, ?, '', ?, '', ?, ?, ?, ?)")
            cursor.execute(insert_query,
                           (data['sku'], data['主图'], data['目前售价'], data['评论数量'], data['更新时间'], data['直达的落地页'],
                            data['产品评分'],
                            data['商品名称']))
        conn.commit()

        cursor.close()
        conn.close()


get()

