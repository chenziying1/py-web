# -*- coding: utf-8 -*-
# time:2022/12/25 14:05
# file demo.py
# outhor:czy
# email:1060324818@qq.com

import requests
import re
import os
import parsel
import openpyxl

#1.1获取页面源代码
def get_html(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'}
    req = requests.get(url,headers=headers)
    if req.status_code == 200:
        data_html = req.text
    else:
        data_html = "页面获取失败！"
    return data_html


#1.2 获取一整个单本小说
def get_onebook(book_url):

    data_html = get_html(book_url)
    if data_html == "页面获取失败！":
        print("此条跳过，执行下一条！")
        return

    selectors = parsel.Selector(data_html)
    selector_list = selectors.css('.listmain dd a::attr(href)').getall()
    book_title = selectors.css('.title::text').get()

    print(f"{book_title} 开始爬取")
    for page in selector_list:

        if page == "javascript:dd_show()":
            continue

        url = f"https://www.quge7.cc{page}"
        data_html = get_html(url)

        if data_html != "页面获取失败！":
            title = re.findall('<span class="title">(.*?)</span>', data_html)[0]
            text = re.findall('<div id="chaptercontent" class="Readarea ReadAjax_content">(.*?)请收藏本站：https://www.quge7.cc。笔趣阁手机版：https://m.quge7.cc <br /><br />',data_html)[0]

            if text != "":
                text = text.replace("<br />", "\n")
                with open("./books/" + book_title + ".txt",mode = "a+" ,encoding="utf-8") as f:
                    f.write(text)
                f.close()
                print(title+"     爬取成功！")
            else:
                print("页面内容为空！")




#1.3获取整个网站地图
def book_map():
    all_books_url = {}
    temp_url,temp_author,temp_name = [],[],[]

    for page in range(1,272):
        map_url = f"https://www.quge7.cc/map/{page}.html"

        data_html = get_html(map_url)
        if data_html == "页面获取失败！":
            print("此条跳过，执行下一条！")
            continue

        selectors = parsel.Selector(data_html)
        url_list_url = selectors.css('.blocks li a::attr(href)').getall()
        url_list_name = selectors.css('.blocks li a::text').getall()
        url_list_author = selectors.css('.blocks li::text').getall()

        temp_url += url_list_url
        temp_name += url_list_name
        temp_author += url_list_author

    #将网站地图数据保存到xlsx文件中
    workbook = openpyxl.load_workbook('./笔趣阁小说数据.xlsx')
    for i in range(len(temp_url)):

        all_books_url[temp_name[i]] = temp_url[i]

        sheet = workbook.active
        frist = 'A' + str(i+1)
        second = 'B' + str(i+1)
        third = 'C' + str(i+1)
        sheet[frist].value = temp_name[i]
        sheet[second].value = temp_author[i]
        sheet[third].value = temp_url[i]

    workbook.save("./笔趣阁小说数据.xlsx")

    return all_books_url

#1.4 将数据保存到excel中
def xlsx_crate():
    if os.path.exists('./笔趣阁小说数据.xlsx'):
        return
    else:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = '笔趣阁小说数据'
        workbook.save('./笔趣阁小说数据.xlsx')




if __name__ == "__main__":
    limits_num = eval(input("请输入最大要获取多少本小说："))
    xlsx_crate()
    all_books_url = book_map()
    a = 0
    for book_url in all_books_url:
        a += 1

        url = all_books_url[book_url]
        get_onebook(f"https://www.quge7.cc{url}")

        if a == limits_num:
            break



