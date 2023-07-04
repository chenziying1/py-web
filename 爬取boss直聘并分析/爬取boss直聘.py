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


def get_page(url):
    cookie = 'wd_guid=3f319504-2887-4ee3-b92f-799516dbf45b; historyState=state; _bl_uid=1nl987be8qsjw2gyOvX6vn9qF7ey; wt2=D4p-tJtlg0POIOZSgEvEIbCS2Cg52Ck1J9GLiy7XmhywhKHRVLngaaNoTGWpDurj-7yA1CzscNls6BYxNKbxgYw~~; wbg=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1661430630,1661452564,1661827801,1661831717; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1661831734; __g=-; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3Dpython%25E7%2588%25AC%25E8%2599%25AB%26city%3D100010000&s=3&friend_source=0; __c=1661831743; __a=20752938.1661401335.1661827824.1661831743.27.5.3.27; geek_zp_token=V1RNgjE-T62FhvVtRvyRwQKimy5TvRwSo~; __zp_stoken__=951feLAQQUD4kLFcDYnELRzAjR0l7JGYCWAUFW0YpATUxVwcoCGk8Fho8FxoKdQFcJU4BNBkBaRxVGklbQGJpPGxHCzIMIWQOPC0PQHl4e118KV8sBBhBaDJ1RU08OxI2ez8UHw0SXVtWAHA9PjBMGnxgMi1jeAUUcA9CG35cViNUIT1VBh1mAD1KMAZ%2BAiA%2FIEQ3PFohIQ%3D%3D'
    #Referer = 'https://www.zhipin.com/web/geek/job?query=python&city=101040100'
    #https://www.zhipin.com/web/geek/job?query=python%E7%88%AC%E8%99%AB&city=101020100
    '''
    proxy = {
        'http':'223.96.90.216:8085'
    }
    '''

    headers = {

              'Cookie':cookie,
              #'Referer':Referer,
              'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
              }
    try:
        response = requests.get(url,headers=headers)#,proxies=proxy
        if response.status_code == 200:
            time.sleep(4)
            response.encoding = response.apparent_encoding
            return response.text
    except requests.ConnectionError as e:
        print('Error', e.args)


def get_joblist(url):
    job_lists = []
    html = get_page(url)
    print(html)
    
    #1.已经获取到了第一页的信息（总页面），接下来应该是获取主页面的url列表
    data = json.loads(html)
    datas = data['zpData']['jobList']

    for i in datas:
        securityId = i['securityId']
        encryptJobId = i['encryptJobId']
        lid = i['lid']

        urls = 'https://www.zhipin.com/job_detail/{}.html?lid={}&securityId={}'.format(encryptJobId,lid,securityId)

        job_lists.append(urls)
    return job_lists
    

def get_job(html):

    soup = BeautifulSoup(html, 'lxml')
    job_all = soup.find_all('div', class_="info-primary")
    if (job_all == []):
        print("cookie已过期")
    #print(job_all)
    
    try:
        # 职位名
        job_title = re.findall('<h1 title="(.*?)"',html)[0]
        # 薪资
        job_salary = soup.find('span', class_="salary").string
        # 公司
        job_company1 = soup.find_all('div', class_="company-info")[1].a['href']
        job_company2 = soup.find_all('div', class_="company-info")[1].a['title']
        # 职位描述
        job_text = soup.find('div', class_="text").text
    
        dicts = {
                '职位名':job_title,
                '薪资':job_salary,
                '公司1':job_company1,
                '公司2':job_company2,
                '职位描述':job_text,
                }
        print(job_title)
        print(job_salary)
        print(job_company2)

        return dicts
        
    except Exception as e:
        print(str(e))
        
def get_job2(url):
          browser = webdriver.Edge("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\msedgedriver.exe")
          browser.get(url)
          time.sleep(10)
          pageSource = browser.page_source
          return pageSource
        


          
def save(dicts):
    f = open('numbers.csv', 'a+')
    fnames = ['职位名','薪资','公司1','公司2','职位描述']
    writer = csv.DictWriter(f, fieldnames=fnames)
    #writer.writeheader()
    try:
        writer.writerow(dicts)
        print('成功存入一条数据!')
    except Exception as e:
        print(str(e))
    finally:
        f.close()
        return
    




def start_urls():
          targets = ['100010000','101010100','101020100','101280100','101280600','101210100','101030100','101110100','101190400','101200100','101230200','101250100','101270100','101180100','101040100']
          target = ['全国','北京','上海','广州','深圳','杭州','天津','西安','苏州','武汉','厦门','长沙','成都','郑州','重庆']
          urls = []
          for i in targets:
                  for j in range(1,4):
                            ans2 = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=python%E7%88%AC%E8%99%AB&city={0}&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page={1}&pageSize=30'.format(i,j)
                            urls.append(ans2)
          return urls



urls = start_urls()
for url in urls:
          job_lists = get_joblist(url=url)
          for i in job_lists:
              print('爬取 ',i)
              #html = get_page(i)
              #print(html)
              #dicts = get_job(html)
              html = get_job2(i)
              #print(html)
              dicts = get_job(html)
              save(dicts)
              time.sleep(2)

    
    

    
