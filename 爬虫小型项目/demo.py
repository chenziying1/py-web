# -*- coding: utf-8 -*-
# time:2023/7/5 16:29
# file index.py
# outhor:czy
# email:1060324818@qq.com

# 导入相关库
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 定义爬虫函数
def spider_zhilian(keyword, page):
    # 构造请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    # 构造请求参数
    params = {
        "kw": keyword, # 搜索关键词
        "p": page # 页码
    }
    # 发送请求，获取响应
    response = requests.get("https://sou.zhaopin.com/", headers=headers, params=params)
    # 判断响应状态码
    if response.status_code == 200:
        # 解析响应内容，获取网页源码
        html = response.text
        # 创建BeautifulSoup对象，指定解析器为lxml
        soup = BeautifulSoup(html, "lxml")
        # 获取招聘信息列表
        job_list = soup.find_all("div", class_="contentpile__content__wrapper")
        # 定义空列表，用于存储数据
        data_list = []
        # 遍历招聘信息列表，提取数据
        for job in job_list:
            # 获取职位名称
            title = job.find("a", class_="contentpile__content__wrapper__item__info__box__jobname").text.strip()
            # 获取公司名称
            company = job.find("a", class_="contentpile__content__wrapper__item__info__box__cname").text.strip()
            # 获取工作地点和薪资范围
            location, salary = job.find("p", class_="contentpile__content__wrapper__item__info__box__job").text.split("_")
            # 获取发布时间和工作经验要求
            time, experience = job.find("p", class_="contentpile__content__wrapper__item__info__box__jobupdate").text.split("_")
            # 获取招聘信息链接
            link = job.find("a", class_="contentpile__content__wrapper__item__info")["href"]
            # 将数据存入字典中
            data = {
                "title": title,
                "company": company,
                "location": location,
                "salary": salary,
                "time": time,
                "experience": experience,
                "link": link
            }
            # 将字典追加到列表中
            data_list.append(data)
        # 返回数据列表
        return data_list
    else:
        # 返回空列表
        return []

# 定义主函数
def main():
    # 定义搜索关键词和页码范围
    keyword = "机器学习工程师"
    pages = range(1, 11) # 前10页
    # 定义空列表，用于存储所有数据
    all_data = []
    # 遍历页码，调用爬虫函数，获取数据
    for page in pages:
        print(f"正在爬取第{page}页的数据...")
        data = spider_zhilian(keyword, page)
        # 将数据追加到总列表中
        all_data.extend(data)
    print(f"爬取完成，共获取{len(all_data)}条数据。")
    # 将总列表转换为DataFrame对象，并保存为csv文件
    df = pd.DataFrame(all_data)
    df.to_csv(f"{keyword}.csv", index=False, encoding="utf-8-sig")
    print(f"数据已保存为{keyword}.csv文件。")

# 调用主函数，执行程序
if __name__ == "__main__":
    main()

