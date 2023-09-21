# -*- coding: utf-8 -*-
# time:2023/7/28 8:42
# file wayfair.py
# outhor:czy
# email:1060324818@qq.com
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


target_list = ['https://www.wayfair.com/brand/bnd/deervalley-b50937.html',
                'https://www.wayfair.com/brand/bnd/deervalley-b50937.html?curpage=2',
                'https://www.wayfair.com/brand/bnd/deervalley-b50937.html?curpage=3',
               "https://www.wayfair.com/brand/bnd/toto-b972.html",
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=2',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=2',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=3',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=4',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=5',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=6',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=7',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=8',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=9',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=10',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=11',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=12',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=13',
                'https://www.wayfair.com/brand/bnd/toto-b972.html?curpage=14',
               'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html',
                'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html?curpage=2',
                'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html?curpage=3',
                'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html?curpage=4',
                'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html?curpage=5',
                'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html?curpage=6',
                'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html?curpage=7',
                'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html?curpage=8',
                'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html?curpage=9',
                'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html?curpage=10',
                'https://www.wayfair.com/brand/bnd/swiss-madison-b43688.html?curpage=11',
               'https://www.wayfair.com/brand/bnd/american-standard-b903.html',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=2',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=3',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=4',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=5',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=6',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=7',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=8',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=9',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=10',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=11',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=12',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=13',
                'https://www.wayfair.com/brand/bnd/american-standard-b903.html?curpage=14',
               'https://www.wayfair.com/brand/bnd/kohler-b819.html',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=2',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=3',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=4',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=5',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=6',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=7',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=8',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=9',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=10',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=11',
                'https://www.wayfair.com/brand/bnd/kohler-b819.html?curpage=12',
                'https://www.wayfair.com/brand/bnd/horow-b62399.html',
                'https://www.wayfair.com/brand/bnd/horow-b62399.html?curpage=2',
                'https://www.wayfair.com/brand/bnd/mohome-b63429.html',
                'https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html',
                "https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html?curpage=2",
                "https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html?curpage=3",
                "https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html?curpage=4",
                "https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html?curpage=5",
                "https://www.wayfair.com/brand/bnd/fine-fixtures-b38322.html?curpage=6",
               'https://www.wayfair.com/keyword.php?keyword=Woodbrige']

for i in target_list:
    headers = {
        'cookie': 'CSNUtId=23e17d3a-6076-9566-352a-432dc55ee602; ExCSNUtId=23e17d3a-6076-9566-352a-432dc55ee602; vid=23e17d3a-6076-9566-352a-432dc55ee602; SFSID=404051738ada9a0c684f43245f4fe7a7; canary=0; WFDC=DSM; serverUAInfo=%7B%22browser%22%3A%22Google%20Chrome%22%2C%22browserVersion%22%3A89.04389114%2C%22OS%22%3A%22Windows%22%2C%22OSVersion%22%3A%2210%22%2C%22isMobile%22%3Afalse%2C%22isTablet%22%3Afalse%2C%22isTouch%22%3Afalse%7D; _pxhd=a8eb65dfb04a827ef94744fbffb32d7a6a5a3cccdd64e37013f92f53bcf05891:7f4eb201-9cf0-11eb-ae26-fb9eaee6d2f3; CSNPersist=page_of_visit%3D2; CSN=g_countryCode%3DUS%26g_zip%3D67346%26CLVW%3D305; categoryId=45974; _pxvid=7f4eb201-9cf0-11eb-ae26-fb9eaee6d2f3; _px3=44cd92501c3ef2b4b422580a232bac226cf7091bcdae52768f4b376813d5e5af:vZGlSrQi/BrNr6MyNkDZs2IfFM/CGOu6gtEq5rbzbh3x3hUV2vZNni3S2gvgdYWXEXiP8rjmEClCs/+W6+Icyg==:1000:JfNA/ZCmtKEcqsxF6ni+pRxODERn3B94d8U+2l+m+kn5GXRAKADx6e751NnLATlskTLYCfL5msgiM3tNzJlJ+djvUaga/E3RMuDgpXHDacIQYyM+CH0VLIRRn7gkxECcCvyk1tZBAErHvSMwLthzHlSeRXHLtoG8inJTFZamyTM=',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'referer': 'https://www.wayfair.com/',
        'upgrade-insecure-requests': '1'
    }
    response = requests.get(i, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    product_links = soup.find_all('a', {'class': '_1yxeg5wb_713'})
    jump_links = [link['href'] for link in product_links]
    print(jump_links)
    print("--------------------------")
    if len(jump_links) > 0:
        with open("../资源/wayfair_url.txt", "a+", encoding="utf-8") as f:
            f.write(str(jump_links) + "\n")
        f.close()