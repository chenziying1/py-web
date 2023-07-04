import random
import re
import requests
from bs4 import BeautifulSoup
import json
import csv
import time






def get_page(url):
    cookie = ""
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
    html = get_page(i)
    #print(html)
    dicts = get_job(html)
    save(dicts)
    
    

    
