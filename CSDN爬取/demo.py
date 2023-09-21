# -*- coding: utf-8 -*-
# time:2022/12/26 17:19
# file index.py
# outhor:czy
# email:1060324818@qq.com

import requests
import openpyxl
import parsel
import os
import pdfkit


#1.1创建数据表
def create_xlsx():
    if os.path.exists("./数据.xlsx"):
        return
    else:
        wookbook = openpyxl.Workbook()
        sheet = wookbook.active
        sheet.title = "csdn数据"
        wookbook.save("./数据.xlsx")

#1.2访问请求
def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }
    rep = requests.get(url, headers=headers)
    if rep.status_code == 200:
        data_html = rep.text
    else:
        data_html = "页面爬取失败!"
        print("页面爬取失败!")
    return data_html

#1.3保存数据到xlsx
def save_xlsx(data_html):

    selectors = parsel.Selector(data_html)
    all_url = selectors.css(".blog-list-box a::attr(href)").getall()
    all_name = selectors.css(".blog-list-content::text").getall()
    all_yuedu = selectors.css(".view-num::text").getall()
    all_dz = selectors.css(".give-like-num::text").getall()
    all_pl = selectors.css(".comment-num::text").getall()
    all_type = selectors.css(".article-type.article-type-yc::text").getall()

    wookbook = openpyxl.load_workbook("./数据.xlsx")

    for i in range(len(all_pl)):
        frist, second, third, four, five, six = 'A' + str(i + 1), 'B' + str(i + 1), \
                                                'C' + str(i + 1), 'D' + str(i + 1), \
                                                'E' + str(i + 1), 'F' + str(i + 1)
        sheet = wookbook.active
        sheet[frist].value = all_name[i]  # 文章名字
        sheet[second].value = all_type[i]  # 类型
        sheet[third].value = all_dz[i]  # 点赞
        sheet[four].value = all_pl[i]  # 评论
        sheet[five].value = all_yuedu[i]  # 阅读
        sheet[six].value = all_url[i]  # 链接
    wookbook.save("./数据.xlsx")

    return all_name,all_url




if __name__ == '__main__':
    create_xlsx()

    url = "https://blog.csdn.net/m0_56366541?spm=1011.2124.3001.5343"
    data_html = get_html(url)

    if data_html != "页面爬取失败!":
        all_name,all_url = save_xlsx(data_html)
        for i in range(len(all_url)-5):
            rep = get_html(all_url[i])


            with open(all_name[i]+".html","w+",encoding="utf-8") as f:
                f.write(rep)
            f.close()

            path_wkthmltopdf = r'D:\\frist\\second\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
            pdfkit.from_file(all_name[i]+".html",all_name[i]+".pdf",configuration=config)











