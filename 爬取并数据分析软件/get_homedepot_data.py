# -*- coding: utf-8 -*-
# time:2023/7/30 8:26
# file get_amzon.py
# outhor:czy
# email:1060324818@qq.com

from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

with open("获取home商品数据/homedeport_data.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
f.close()


while len(a) > 0:
    url = a[0].strip()
    paths = "D:\\egde\\edgedriver_win64 (2)\\msedgedriver.exe"
    options = webdriver.EdgeOptions()
    options.use_chromium = True  # 使用 Chromium 内核
    driver = webdriver.Edge(options=options, executable_path=paths)
    driver.get(url)
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,600.0347900390625)")
    driver.execute_script("window.scrollTo(0,1213.8001708984375)")
    driver.execute_script("window.scrollTo(0,1600.8001708984375)")
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
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
        span_tags = soup.find('div', class_='ratings-reviews__accordion-subheader').find_all('span')
        text_data = [span.get_text() for span in span_tags]
        data["产品评分"] = text_data[0]
        data["评论数量"] = text_data[2]
    except:
        pass

    try:
        span_tags = soup.find('div', class_='price-format__large price-format__main-price').find_all('span')
        text_data  = [span.get_text() for span in span_tags[:2]]
        shoujia = "".join(text_data)
        data["目前售价"] = shoujia
    except:
        pass

    try:
        img_tag = soup.find('button', class_='mediagallery__imgblock').find('img')['src']
        data["主图"] = img_tag
    except:
        pass

    try:
        h1_tag = soup.find('h1', class_='sui-h4-bold sui-line-clamp-unset')
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

    if "DeerValley" in mingcheng or "DEERVALLEY" in url:
        with open("获取home商品数据/home_DeerValley.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "TOTO" in mingcheng or "TOTO" in url:
        with open("获取home商品数据/home_TOTO.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Swiss Madison" in mingcheng or "Swiss-Madison" in url:
        with open("获取home商品数据/home_Swiss_Madison.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "American Standard" in mingcheng or "American-Standard" in url:
        with open("获取home商品数据/home_American_Standard.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Kohler" in mingcheng or "KOHLER" in url:
        with open("获取home商品数据/home_Kohler.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "HOROW" in mingcheng or "HOROW" in url:
        with open("获取home商品数据/home_HOROW.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "MOHOME" in mingcheng or "MOHOME" in url:
        with open("home_MOHOME.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Fine Fixtures" in mingcheng or "FINE-FIXTURES" in url:
        with open("获取home商品数据/home_Fine_Fixtures.txt", "a+", encoding="utf-8") as f:
            f.write(str(data) + "\n")
            print(str(data))
        f.close()
        a.pop(0)
    elif "Woodbrige" in mingcheng or "WOODBRIDGE" in url:
        with open("获取home商品数据/home_Woodbrige.txt", "a+", encoding="utf-8") as f:
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


