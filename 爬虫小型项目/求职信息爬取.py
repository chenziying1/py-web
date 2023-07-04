# -*- coding: utf-8 -*-
# time:2022/11/16 8:14
# file 求职信息爬取.py
# outhor:czy
# email:1060324818@qq.com


import random
import re
import requests
from bs4 import BeautifulSoup
import json
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''
要实现的功能：
1.用字典存储配置信息
2.新增爬取前程无忧求职网站的功能
'''


dict_job_title=[]
dict_job_salary=[]
dict_job_text=[]

#0.组件最开始的urlBOSS直聘
def start_urls_Boss():
    targets = ['100010000', '101010100', '101020100', '101280100', '101280600', '101210100', '101030100', '101110100',
               '101190400', '101200100', '101230200', '101250100', '101270100', '101180100', '101040100']
    target = ['全国', '北京', '上海', '广州', '深圳', '杭州', '天津', '西安', '苏州', '武汉', '厦门', '长沙', '成都', '郑州', '重庆']
    urls = []
    for i in targets:
        for j in range(1, 10):
            ans2 = 'https://www.zhipin.com/web/geek/job?query=python&city={0}&page={1}'.format(i, j)
            urls.append(ans2)
    return urls

#0.1组建智联招聘的爬取
def start_urls_zhiping():
    targets = ['530','531','532','533','534','535','536','537','538','539']
    urls = []
    for i in targets:
        for j in range(1, 2):
            ans2 = 'https://sou.zhaopin.com/?jl={0}&kw=Python&p={1}'.format(i, j)
            urls.append(ans2)
    return urls

#0.2组建前程无忧的爬取
def start_urls_piancheng():
    targets = ['000000','010000','020000','030000','040000','050000','060000','070000','080000','090000','100000']
    urls = []
    for i in targets:
        for j in range(1, 6):
            ans2 = 'https://search.51job.com/list/{0},000000,0000,00,9,99,python,2,{1}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='.format(i, j)
            urls.append(ans2)
    return urls

#8.通过爬虫正常访问网页的手段获取页面源码
def get_job(url):
    proxy = {
        'http': '47.95.199.44:80'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)  # ,proxies=proxy
        if response.status_code == 200 and "滑动验证" not in response.text:
            response.encoding = response.apparent_encoding
            print("爬取成功")
            return response.text
        else:
            response = requests.get(url, headers=headers,proxies=proxy)
            if response.status_code == 200 and "滑动验证" not in response.text:
                response.encoding = response.apparent_encoding
                print("爬取成功")
                return response.text
    except requests.ConnectionError as e:
        print('Error', e.args)

#1.通过webdriver暴力获取加载后的页面源码
def get_job2(url):
    browser = webdriver.Edge("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\msedgedriver.exe")
    try:
        browser.get(url)
        time.sleep(10)
        pageSource = browser.page_source
    except Exception as e:
        print("url出错" + str(e))
        return url+"失败!"
    #必须放在这里，用来等待加载完成
    if pageSource != "" and "正在加载" not in pageSource:
        print("爬取成功")
    else:
        print("爬取失败")
    return pageSource

#2.保存文件
def save_txt(file,filename):
    with open(filename,"a+",encoding="utf-8") as f:
        f.seek(0,2)
        f.write(file)
    f.close()

#3.从保存的文件中获取需要的信息
def chafeng(filename,url_name):
    global dict_job_text
    global dict_job_salary
    global dict_job_title
    try:
        if url_name == "boss直聘":
            with open(filename, 'r', encoding='utf-8') as f:
                # 职位名
                job_title = re.findall('<span class="job-name">(.*?)</span>', f.read())
                # 薪资
                job_salary = re.findall('<span class="salary">(.*?)</span>', f.read())
                # 职位描述
                job_text = re.findall('<ul class="tag-list">(.*?)</ul>', f.read())
                for i in range(len(job_text)):
                    target = job_text.pop(0)
                    target = target.replace("<li>"," ")
                    target = target.replace("</li>", " ")
                    job_text.append(target)
        elif url_name == "智联招聘":
            with open(filename, 'r', encoding='utf-8') as f:
                #清洗数据
                target = f.read().replace("\\"," ")
                target = target.replace("\n          ", " ")
                # 职位名
                job_title = re.findall('<span style="color: #FF5959;">Python</span>(.*?)</span>', target)
                # 薪资
                job_salary = re.findall('<p class="iteminfo__line2__jobdesc__salary">(.*?) <!----></p>', target)
                # 职位描述
                job_text1 = re.findall('<li class="iteminfo__line2__jobdesc__demand__item">(.*?)</li>', target)
                job_text2 = re.findall('<div class="iteminfo__line3__welfare__item">(.*?)</div>', target)
                job_text = job_text1+job_text2
        elif url_name == "前程无忧":
            with open(filename, 'r', encoding='utf-8') as f:
                # 清洗数据,这里获取到的是类似于json一样的数据要用json的处理方式
                target = f.read().replace("\\", " ")
                # 职位名
                job_title = re.findall('"job_name":"(.*?)","job_title"', target)
                # 薪资
                job_salary = re.findall('"providesalary_text":"(.*?)","workarea"', target)
                # 职位描述
                job_text1 = re.findall('"attribute_text":\[(.*?)\],"companysize_text"', target)
                job_text = job_text1

        f.close()
        dict_job_title = job_title
        dict_job_text = job_text
        dict_job_salary = job_salary
        return
    except Exception as e:
        print(str(e))

#5.储存入csv中
def csv_data():
    with open("data.csv","w+",encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in range(len(dict_job_title)):
            ans = dict_job_title[row]+dict_job_salary[row]+dict_job_text[row]
            writer.writerow(ans)
    print("储存完成！")
    f.close()

#6.储存到字典中
def dicts_data():
    dicts_job_title = {}
    for i in dict_job_title:
        if i in dicts_job_title:
            dicts_job_title[i] += 1
        else:
            dicts_job_title[i] = 1
    dicts_job_salary = {}
    for i in dict_job_salary:
        if i in dicts_job_salary:
            dicts_job_salary[i] += 1
        else:
            dicts_job_title[i] = 1
    dicts_job_text = {}
    for i in dict_job_text:
        if i in dicts_job_text:
            dicts_job_text[i] += 1
        else:
            dicts_job_text[i] = 1
    return dicts_job_title,dicts_job_salary,dicts_job_text

#7.用字典存储配置信息
dicts_type = {"智联招聘":"智联招聘.txt","boss直聘":"boss直聘.txt","前程无忧":"前程无忧.txt"}
dicts_urls = {"智联招聘":start_urls_zhiping(),"boss直聘":start_urls_Boss(),"前程无忧":start_urls_piancheng()}
#4.主程序，程序从这里启动
def mian():
    name = input("请输入你想爬取的招聘网站:")
    filename = dicts_type[name]
    urls = dicts_urls[name]
    for url in urls:
        print('爬取', url)
        #job_text = get_job2(url=url)
        try:
            job_text = get_job(url=url)
            save_txt(job_text, filename)
            time.sleep(3)
        except Exception as e:
            print(str(e))
        finally:
            continue
    chafeng(filename, name)
    #csv_data()

#chafeng("前程无忧.txt","前程无忧")
mian()
print(dict_job_title)
print("一共"+str(len(dict_job_title))+"个职位")
print(dict_job_salary)
print("一共"+str(len(dict_job_salary))+"个职位")
print(dict_job_text)
print("一共"+str(len(dict_job_text))+"个职位")

#1.最大的问题在于一旦次数过多，boss直聘会直接禁ip
#2.爬取的数据不够，30条一页，一个地区10页，15个地区，只有4500条数据，远远不够
#3.获取到了之后，如何进行分析，拆解？
#4.获取前程无忧被滑动验证码卡住了



