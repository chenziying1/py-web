# -*- coding: utf-8 -*-
# time:2023/7/30 8:26
# file get_amzon.py
# outhor:czy
# email:1060324818@qq.com
import re
from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

a = []
with open("资源/wayfair_url.txt", "r", encoding="utf-8") as f:
    for line in f:
        a += (eval(line.strip()))
f.close()

with open("资源/cookie.txt", "r", encoding="utf-8") as f:
    b = f.readline()
    b = b.strip()
f.close()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookie': b,
}

while len(a) > 0:
    url = a[0].strip()
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {
        '更新时间': datetime.now().strftime("%H:%M:%S"),
        '直达的落地页': url,
        '产品评分': '无评分',
        '目前售价': '无售价',
        '评论数量': '无评论',
        '主图': '无主图',
        '商品名称': '无商品名称',
    }

    try:
        shuliang = soup.find('span', class_='ProductRatingNumberWithCount-count ProductRatingNumberWithCount-count--link').get_text(strip=True)
        data["评论数量"] = shuliang
    except:
        pass

    try:
        pingfeng = soup.find('span',class_='ProductRatingNumberWithCount-rating').get_text(strip=True)
        data["产品评分"] = pingfeng
    except:
        pass

    try:
        pattern = r'"price":(\d+\.\d+)'
        shoujia = re.search(pattern, response.text)
        price = float(shoujia.group(1))
        data["目前售价"] = price
    except:
        pass

    try:
        img_tag = soup.find('img', class_='_15bab5p1_6101')['src']
        data["主图"] = img_tag
    except:
        pass

    try:
        h1_tag = soup.find('h1', class_='kzv0b81yc_6101 _1yimfeh6_6101 _1yimfehd_6101 _1yimfehj_6101')
        mingcheng = h1_tag.get_text()
        data["商品名称"] = mingcheng
    except:
        try:
            mingcheng = soup.find_all('span', id='productTitle')[0].get_text(strip=True)
            data["商品名称"] = mingcheng
        except:
            with open("获取home商品数据/cookie失效.txt", "a+", encoding="utf-8") as f:
                f.write(str(url) + "\n")
            f.close()
            a.pop(0)
            continue

    if "DeerValley" in mingcheng or "deervalley" in url:
        with open("wayfair_DeerValley.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "TOTO" in mingcheng or "toto" in url:
        with open("wayfair_TOTO.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Swiss Madison" in mingcheng or "swiss-madison" in url:
        with open("wayfair_Swiss_Madison.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "American Standard" in mingcheng or "american-standard" in url:
        with open("wayfair_American_Standard.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Kohler" in mingcheng or "kohler" in url:
        with open("wayfair_Kohler.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "HOROW" in mingcheng or "horow" in url:
        with open("wayfair_HOROW.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "MOHOME" in mingcheng or "mohome" in url:
        with open("wayfair_MOHOME.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Fine Fixtures" in mingcheng or "fine-fixtures" in url:
        with open("wayfair_Fine_Fixtures.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Woodbrige" in mingcheng or "woodbrige" in url:
        with open("wayfair_Woodbrige.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    else:
        with open("名称不正确.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
        f.close()
        a.pop(0)
        print(url + "名称不正确，失败")


