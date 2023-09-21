# -*- coding: utf-8 -*-
# time:2023/7/30 8:26
# file get_amzon.py
# outhor:czy
# email:1060324818@qq.com

from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup

with open("amzon_data.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
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
            with open("获取home商品数据/cookie失效.txt", "a+", encoding="utf-8") as f:
                f.write(str(url) + "\n")
            f.close()
            a.pop(0)
            continue

    if "DeerValley" in mingcheng or "DeerValley" in url:
        with open("amzon_DeerValley.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "TOTO" in mingcheng or "TOTO" in url:
        with open("amzon_TOTO.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Swiss Madison" in mingcheng or "Swiss+Madison" in url:
        with open("资源/amzon_Swiss_Madison.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "American Standard" in mingcheng or "American+Standard" in url:
        with open("amzon_American_Standard.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Kohler" in mingcheng or "Kohler" in url:
        with open("amzon_Kohler.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "HOROW" in mingcheng or "HOROW" in url:
        with open("amzon_HOROW.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "MOHOME" in mingcheng or "MOHOME" in url:
        with open("amzon_MOHOME.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Fine Fixtures" in mingcheng or "Fine+Fixtures" in url:
        with open("amzon_Fine_Fixtures.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Woodbrige" in mingcheng or "Woodbrige" in url:
        with open("amzon_Woodbrige.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    else:
        with open("获取home商品数据/名称不正确.txt", "a+", encoding="utf-8") as f:
            f.write(str(url) + "\n")
        f.close()
        a.pop(0)
        print(url + "名称不正确，失败")
'''
更新时间 nowtime
直达的落地页 url
产品评分 <span class="a-size-base a-color-base"> 3.4 </span>
目前售价 <span class="a-price-whole">153<span class="a-price-decimal">.</span></span>
评论数量 <span id="acrCustomerReviewText" class="a-size-base">21 评论</span>
主图 <img alt="TOTO LT221#01 17 X 13 矩形 UC LAV 英寸,棉白色" src="https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX679_.jpg" data-old-hires="https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SL1500_.jpg" onload="markFeatureRenderForImageBlock(); if(this.width/this.height > 1.3){this.className += ' a-stretch-horizontal'}else{this.className += ' a-stretch-vertical'};this.onload='';setCSMReq('af');if(typeof addlongPoleTag === 'function'){ addlongPoleTag('af','desktop-image-atf-marker');};setCSMReq('cf')" data-a-image-name="landingImage" class="a-dynamic-image a-stretch-horizontal" id="landingImage" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX522_.jpg&quot;:[307,522],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX425_.jpg&quot;:[250,425],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX569_.jpg&quot;:[335,569],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX355_.jpg&quot;:[209,355],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX679_.jpg&quot;:[400,679],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX450_.jpg&quot;:[265,450],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX466_.jpg&quot;:[274,466]}" style="max-width: 393px; max-height: 302px;">

<div id="imgTagWrapperId" class="imgTagWrapper" style="height: 302.308px;">
	            <img alt="TOTO LT221#01 17 X 13 矩形 UC LAV 英寸,棉白色" src="https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX679_.jpg" data-old-hires="https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SL1500_.jpg" onload="markFeatureRenderForImageBlock(); if(this.width/this.height > 1.3){this.className += ' a-stretch-horizontal'}else{this.className += ' a-stretch-vertical'};this.onload='';setCSMReq('af');if(typeof addlongPoleTag === 'function'){ addlongPoleTag('af','desktop-image-atf-marker');};setCSMReq('cf')" data-a-image-name="landingImage" class="a-dynamic-image a-stretch-horizontal" id="landingImage" data-a-dynamic-image="{&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX522_.jpg&quot;:[307,522],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX425_.jpg&quot;:[250,425],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX569_.jpg&quot;:[335,569],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX355_.jpg&quot;:[209,355],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX679_.jpg&quot;:[400,679],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX450_.jpg&quot;:[265,450],&quot;https://m.media-amazon.com/images/I/61MEFUwEclL._AC_SX466_.jpg&quot;:[274,466]}" style="max-width: 393px; max-height: 302px;"> <div id="magnifierLens" style="position: absolute; background-image: url(&quot;https://m.media-amazon.com/images/G/01/apparel/rcxgs/tile._CB483369110_.gif&quot;); cursor: pointer; width: 216px; height: 31px; left: 126px; top: 114.469px;"></div></div>
'''

