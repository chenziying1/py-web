# -*- coding: utf-8 -*-
# time:2022/12/2 12:09
# file bili爬取.py
# outhor:czy
# email:1060324818@qq.com
import re
import requests
import time
import os

#0.爬取页面内容
def req_neirong(url):
    headers = {
        "Host":"search.bilibili.com",
        "Referer": "https://www.bilibili.com/",
        "cookie":"buvid3=9C2C2A01-8F33-3EB7-4E95-69516C7329E262245infoc; _uuid=2DAFA42A-4E12-10D3C-E1095-6107582B14C2763571infoc; buvid4=390CD9D5-F37B-87C4-1C75-31AEB6367EC365688-022081523-2Wa52aDfPGcJBBUIWFYNVKDlpxfD+5svtwGbzdvZAmA0Dzbb+IMU8Q==; buvid_fp_plain=undefined; b_nut=100; CURRENT_FNVAL=4048; rpdid=0z9Zw2XICq|aSwKUHv|3VEO|3w1OWbZv; i-wanna-go-back=-1; b_ut=7; nostalgia_conf=-1; CURRENT_QUALITY=16; fingerprint=7006f44cf7baefa9f792d89e8860bac2; b_lsid=D10314B88_184DC253839; buvid_fp=7006f44cf7baefa9f792d89e8860bac2; innersign=0; sid=5nrognq6; PVID=2",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
    }

    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        print("爬取 ",url," 成功")
        time.sleep(5)
        return res
    else:
        print("爬取失败")
        return "Crawl failed"

#1.爬取图片内容
def req_neirong2(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
    }

    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        print("爬取 ", url, " 成功")
        time.sleep(3)
        return res
    else:
        print("爬取失败")
        return "Crawl failed"


#1.分析显示页面,保存视频及图像链接
images = []
urls = []
names = []
def fenxi(text):
    global images,urls,names

    images=re.findall('<source srcset="//(.*?)"',text)
    urls=re.findall('<a href="//(.*?)"',text)
    names=re.findall('<h3 class="bili-video-card__info--tit" title="(.*?)"',text)

    a = len(images)
    while a > 0:
        target = images.pop(0)
        a -= 1
        if '.avif' in target:
            continue
        else:
            images.append(target)


    for i in ".*/-+~!@#$%^&*()_+}{:\"?><;',.":
        for j in range(len(names)):
            names[j] = names[j].replace(i," ")


#2.保存到本地文件
def file_save(filename,text):
    if os.path.exists(filename):
        return
    with open(filename,"w+",encoding="utf-8")as f:
        f.write(text)
    f.close()

#3.进行url构建
def url_goujian():
    req_url = [
        "https://search.bilibili.com/all?keyword=sour rin&from_source=webtop_search&spm_id_from=333.1007&search_source=5"]
    for i in range(2,35):
        url = "https://search.bilibili.com/all?keyword=sour+rin&from_source=webtop_search&spm_id_from=333.1007&search_source=3&page={0}&o={1}"\
                .format(i,30*(i-1))
        req_url.append(url)
    print("url构建完毕")
    return req_url

#4.构建文件名
def filename_goujian():
    file_path = "./bili_txt/"
    filename_list = []
    for i in range(1,35):
        name = "第{}页.books".format(i)
        filename = file_path+name
        filename_list.append(filename)
    print("文件名构建完毕")
    return filename_list

#5.发起访问请求获取图片
def huoqu_qicture():
    for i in range(len(images)):

        imagesurl = "https://"+images[i]
        print(imagesurl)
        contents = req_neirong2(imagesurl).content
        picture_name = "./images/"+names[i]+".webp"

        #如果已经请求过了，则不再请求
        if os.path.exists(picture_name):
            continue

        with open(picture_name,"wb")as f:
            f.write(contents)
            print("图片保存完成")
        f.close()
        time.sleep(1)


req_url=url_goujian()
filename_list=filename_goujian()
for i in range(len(req_url)):
    text = req_neirong(req_url[i]).text
    file_save(filename_list[i],text)
    with open(filename_list[i],encoding="utf-8")as f:
        fenxi(f.read())
    print(images,len(images))
    print(urls,len(urls))
    print(names,len(names))
    #huoqu_qicture()



