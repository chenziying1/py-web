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
    cookie = 'wd_guid=6c7cfed0-2a0c-4539-b0dc-9bb727142350; historyState=state; _bl_uid=9Rlh17nz9ay314zaa8zj8gh1k466; _9755xjdesxxd_=32; YD00951578218230%3AWM_NI=%2BgTfpVzHLenRjcoGNdgmVBWLK%2FR%2BHDEKeqLdPIc9nmMjoln15q%2FC5MsiHHRsSnKc7Z%2B3Wp%2BYxGvpRUKXAXxQF7ga2pGAYIMOnGdq7r1LMdbzPApuawQ74S0TtU%2FcXspnVDM%3D; YD00951578218230%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee93f26398f5ad8eb47fb1928bb7c44b838e8e86c4549092b7aed93ab0ac82aab62af0fea7c3b92ae9b99c87f35eba988486ed5aaabda1a8cd70a5b39aa3d64889f19ecccb508795ab92cf709497addaed678fb6a18ded3bf7afe1a4b847b1b788a9d17991b28584b652e9ed9991aa53bc99ba91d15f89888fb9fb5b86e9a982b17c859f97aad045ae99ac92b67af3948385e172949fc096e47d93e9fcb4b360b88be184db79b4b29aa5d037e2a3; YD00951578218230%3AWM_TID=dacczoVObPVEAFVQFELQSaM3MMzhsJZu; sid=sem_pz_bdpc_dasou_title; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1661435794,1661454546; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1661454546; __zp_stoken__=ad34eLHkIHxR%2FOj0HTVFeLn06Uls%2FQBZtK399d1Q4UzZtfHs7Iw81UEUWJRgndWhGAkdEOlVAJmc7bDNHbCUjK2JAFCNaR2p6MWZ1TWhENlV9TwwGIwMWGmZ0JVYCbk1KTC8SSzoDejcoaRUpVmg7TyIIWHIxF3x4EBwlFHAJCQxkCnNCU3QMbyR6Ax1AV39DF1tnPHJHYQ%3D%3D; gdxidpyhxdE=g6IPq8HIaODKInZNwjWHUQ7Z1C2%2BP41%2FmxQXczmOg8m%5CadkGLzvwtSZxuOxCXvQMquINNroTeb0IXd%2B0w011KwxiBUrHoz4lqa6AIBEjm65Xsk1Q9kf9rCQdPMZXmVfE5tAVXg%2BSo1OqfHmBJ%2F3wDyiZ7whxZYK%2FZwYK1rhBhBW4wlbk%3A1661455462701; __c=1661454545; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3Dpython%26city%3D101040100&r=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.Ks0000azFUyZsov8Q1ZxcnDMbiSrM_J1SD0bFj5HDYWmj-3NPYR1B1g7t58DwiXgtg0-zdAjJ9AHOwfFMCEHL1nLAMmwd8h0cLsKPvft6rPqDdwEZXPUPOSk7s6nq8aPXF_U-anpVPq9ycBLqSWSIhO13Jn4rMU49Q90GRZvxhhlq4Evn2w2KYYZ1aKlZupz77TeQkmRxjzxr49OhrtryeBxPhBX.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1Tqpkko60IgP-T-qYXgK-5H00mywxIZ-suHY10ZIEThfqmhq1Tqpkko60ThPv5H00IgF_gv-b5HDdn1m3rjbLPj00UgNxpyfqnHfvnW0znHn0UNqGujYknHmzn1ndnsKVIZK_gv-b5HDzrjcv0ZKvgv-b5H00pywW5R9rffKspyfqP0KWpyfqn0KWThnqPjR3rHR%26dt%3D1661454532%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%26tpl%3Dtpl_12826_27888_0%26l%3D1536889740%26us%3DlinkVersion%253D1%2526compPath%253D10036.0-10032.0%2526label%253D%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkType%253D%2526linkText%253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258ABOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525EF%2525BC%25258C&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&s=3&friend_source=0&s=3&friend_source=0; __a=79126819.1661435800.1661435800.1661454545.8.2.4.4'
    Referer = 'https://www.zhipin.com/web/geek/job?query=python&city=101040100'
    '''
    proxy = {
        'http':'223.96.90.216:8085'
    }
    '''

    headers = {

              'Cookie':cookie,
              'Referer':Referer,
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
        # 职位标签
        job_tag1 = soup.find('p').string
        # 公司
        job_company1 = soup.find_all('div', class_="company-info")[1].a['href']
        job_company2 = soup.find_all('div', class_="company-info")[1].a['title']
        # 职位描述
        job_text = soup.find('div', class_="text").text
    
        dicts = {
                '职位名':job_title,
                '薪资':job_salary,
                '职位标签':job_tag1,
                '公司1':job_company1,
                '公司2':job_company2,
                '职位描述':job_text,
                }
        print(job_title)
        print(job_salary)
        print(job_tag1)
        print(job_company1)
        print(job_company2)
        print(job_text)

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
    fnames = ['职位名','薪资','职位标签','公司1','公司2','职位描述']
    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
    try:
        writer.writerow(dicts)
        print('成功存入一条数据!')
    except Exception as e:
        print(str(e))
    finally:
        f.close()
        return
    







url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=python&city=101040100&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page=1&pageSize=30'
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
    
    

    
