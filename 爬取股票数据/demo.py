import datetime

import requests
import openpyxl
import time

# 网站URL
url = 'https://data.cfi.cn/data_ndkA0A1934A1935A36.html#A0A1934A1935'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
# Excel文件路径
excel_file = 'data.xlsx'
# 指定行数
row_num = 2

while True:
    try:
        # 发送请求，获取网页内容
        response = requests.get(url,headers=headers)

        html = response.text
        # 提取涨幅中位数
        index_start = html.find('涨幅中位数')
        index_end = html.find('</font>', index_start)
        content = html[index_start:index_end]

        value = content.split('>')[1]
        now = datetime.datetime.now()
        print(str(now) + " 现在的中位价涨幅为:" + content.split('>')[1])
        # 打开Excel文件，获取工作簿和工作表
        wb = openpyxl.load_workbook(excel_file)
        ws = wb.active
        # 将数据写入指定单元格
        cell = ws.cell(row_num, 1)
        cell.value = value
        row_num += 1
        # 保存Excel文件
        wb.save(excel_file)

        with open("log.txt","a+",encoding="utf-8" ) as f:
            f.write(str(now) + " 现在的中位价涨幅为:" + content.split('>')[1] + "\n")
        f.close()

        # 休眠5分钟
        time.sleep(300)

    except :
        now = datetime.datetime.now()
        print("运行出现错误 可能是data.xlsx重复导致，请将data.xlsx保存到别处，再在这里新建一个data.xlsx\n")
        with open("log.txt","a+",encoding="utf-8" ) as f:
            f.write(str(now) + " 运行出现错误\n")
        f.close()
