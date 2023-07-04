# -*- coding: utf-8 -*-
# time:2023/5/16 15:07
# file 爬取并判断链接是否可用.py
# outhor:czy
# email:1060324818@qq.com

"""
需求：根据xlsx文件进行判断，看看有哪些链接还是可以使用的，将名字和解压密码一块打印出来

功能：
    1.获取xlsx文件中字，解压密码，链接信息
    2.进行判断，还可以使用的链接打印，
"""

import requests

headers = {
    "accept":"application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
}
not_exists = 0

def like_is(url,name,password):
    global not_exists
    r = requests.get(url, headers=headers)
    if "<title>百度网盘-链接不存在</title>" in r.text:
        not_exists += 1
    else:
        print(name,url,password)


#分析xlsx文件
def duqu():
    import openpyxl

    # Load the workbook
    workbook = openpyxl.load_workbook('电脑游戏备用链接.xlsx')

    # Select the worksheet
    worksheet = workbook['Sheet1']

    # Get the values in column B
    column_b = [cell.value for cell in worksheet['B']]
    # Get the values in column C
    column_C = [cell.value for cell in worksheet['C']]
    # Get the values in column D
    column_D = [cell.value for cell in worksheet['D']]

    # Print the values in column B
    for i in range(len(column_b)):
        #去除空连接以及不规范链接
        if column_b[i] is None or column_b[i] == 24 :
            continue
        if "http" not in column_b[i]:
            column_b[i] = "https://" + column_b[i]

        like_is(url=column_b[i],name=column_C[i],password=column_D[i])

#分析xlsx文件2
def duqu2():
    import openpyxl

    # Load the workbook
    workbook = openpyxl.load_workbook('电脑游戏备用链接.xlsx')

    # Select the worksheet
    worksheet = workbook['Sheet1 (3)']

    # Get the values in column B
    column_b = [cell.value for cell in worksheet['B']]
    # Get the values in column C
    column_C = [cell.value for cell in worksheet['A']]
    # Get the values in column D
    column_D = [cell.value for cell in worksheet['C']]

    # Print the values in column B
    for i in range(len(column_b)):
        #去除空连接以及不规范链接
        if column_b[i] is None or column_b[i] == 24 :
            continue
        if "http" not in column_b[i]:
            column_b[i] = "https://" + column_b[i]

        like_is(url=column_b[i],name=column_C[i],password=column_D[i])


if __name__ == "__main__":
    duqu2()
    print("一共有",not_exists,"个失效链接")
