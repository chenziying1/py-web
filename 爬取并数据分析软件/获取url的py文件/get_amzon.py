# -*- coding: utf-8 -*-
# time:2023/7/30 8:26
# file get_amzon.py
# outhor:czy
# email:1060324818@qq.com


# <a class="a-link-normal s-no-outline" href="/-/zh/sspa/click?ie=UTF8&amp;spc=MTo4NDQwNjQ1MzIyMzczODI1OjE2OTA2NzY3MjI6c3BfbXRmOjIwMDA0MTQ2Njc3NjA5ODo6MDo6&amp;url=%2Fdp%2FB096QSSP6T%2Fref%3Dsr_1_25_sspa%3Fkeywords%3DAmerican%2BStandard%26qid%3D1690676722%26sr%3D8-25-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1"><div class="a-section aok-relative s-image-square-aspect"><img class="s-image" src="https://m.media-amazon.com/images/I/81GmJBTf7NL._AC_UL400_.jpg" srcset="https://m.media-amazon.com/images/I/81GmJBTf7NL._AC_UL400_.jpg 1x, https://m.media-amazon.com/images/I/81GmJBTf7NL._AC_UL600_FMwebp_QL65_.jpg 1.5x, https://m.media-amazon.com/images/I/81GmJBTf7NL._AC_UL800_FMwebp_QL65_.jpg 2x, https://m.media-amazon.com/images/I/81GmJBTf7NL._AC_UL1000_FMwebp_QL65_.jpg 2.5x, https://m.media-amazon.com/images/I/81GmJBTf7NL._AC_UL1200_FMwebp_QL65_.jpg 3x" alt="赞助广告- AMERICAN MUTT TOOLS 17 件折叠内六角扳手套装 – 内六角扳手套装 公制和标准 SAE 折叠六角扳手套装 – 重型小内六角扳手套装 – 内六角扳手套装 六角扳手套装" data-image-index="25" data-image-load="" data-image-latency="s-product-image" data-image-source-density="1"></div></a>
import requests
from bs4 import BeautifulSoup

with open("amzon_url.txt", "r", encoding="utf-8") as f:
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

for url in a:
    url = url.strip()
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    url_list = soup.find_all('a', class_='a-link-normal s-no-outline')
    for a_tag in url_list:
        href = a_tag.get('href')
        with open("amzon_data.txt","a+",encoding="utf-8") as f:
            f.write("https://www.amazon.com/"+href+"\n")
            print("https://www.amazon.com/"+href)
        f.close()

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