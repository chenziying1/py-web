# -*- coding: utf-8 -*-
# time:2023/7/22 23:23
# file demo2.py
# outhor:czy
# email:1060324818@qq.com

"""
1.爬取百度地图昆明城市道路的实时拥堵数据，大约二十条道路
2.可以设置时间，(应该是指设置一个时间段，获取现在到这个时间段里面的数据)
3.数据保存到excel表格中
"""

import datetime
import random
import time
import requests
import json
import openpyxl

def get_congestion_data(urls):

    congestion_data = []

    for url in urls:
        #获取当前时间
        now = datetime.datetime.now()
        # 发送请求，获取数据
        response = requests.get(url)
        json_data = json.loads(response.text)
        print(json_data)
        if json_data['message'] == "road_name错误":
            continue
        try:
            # 解析数据，并保存到一个数组中
            if "畅通" in json_data['evaluation']['status_desc']:
                congestion_data.append({
                    '名称': json_data['road_traffic'][0]['road_name'],
                    '速度': "0",
                    '级别': "0",
                    '拥堵': json_data['evaluation']['status_desc'],
                    '时间': now.strftime("%Y-%m-%d %H:%M:%S")
                })
            else:
                congestion_data.append({
                    '名称': json_data['road_traffic'][0]['road_name'],
                    '速度': json_data['road_traffic'][0]['congestion_sections'][0]['speed'],
                    '级别': json_data['road_traffic'][0]['congestion_sections'][0]['status'],
                    '拥堵': json_data['road_traffic'][0]['congestion_sections'][0]['section_desc'],
                    '时间': now.strftime("%Y-%m-%d %H:%M:%S")
                })
        except ValueError as e:
            print(e)

    return congestion_data

def save_to_excel(data):
    # 创建Excel工作簿
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # 向工作表中添加表头
    sheet.append(['名称', '速度', '级别', '拥堵', '时间'])

    # 向工作表中添加数据
    for item in data:
        sheet.append([
            item['名称'],
            item['速度'],
            item['级别'],
            item['拥堵'],
            item['时间']
        ])

    # 保存Excel文件
    workbook.save('昆明市道路实时拥堵数据.xlsx')

if __name__ == '__main__':

    road_name = ['北京路','东风西路','环城西路','环城南路','二环东路','二环北路','二环西路','滇池路','二环南路','彩云北路','彩云中路',
                      '彩云南路','金色大道','白塔路','北辰大道','昌宏路','西三环','人民路','北三环','广福路']
    urls = []
    for road in road_name:
        url = 'http://api.map.baidu.com/traffic/v1/road?road_name={0}&city=%E6%98%86%E6%98%8E%E5%B8%82' \
              '&ak=W16W0C5FSsLloaq8Z6HjHphu48GMvKu5'.format(road)
        urls.append(url)
    #print(urls)

    #读取配置文件
    with open("setting.txt", "r",encoding="utf-8") as f:
        first_line = f.readline()
        end_time_str, duration = first_line.split("，")
    f.close()

    if end_time_str == "":
        end_time_str = datetime.datetime.now()  # 结束时间
    if duration == None:
        duration = 60  # 持续时间

    end_time = time.mktime(datetime.datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S').timetuple())  # 转换为时间戳
    now_time = int(datetime.datetime.now().timestamp())
    #print(end_time,now_time)

    congestion_data = []
    while True:
        now_time = int(datetime.datetime.now().timestamp())
        if end_time >= now_time :
            congestion_data+=get_congestion_data(urls)
            time.sleep(int(duration)-15)
        else:
            break

    save_to_excel(congestion_data)

    #生成日志文件
    content = str(datetime.datetime.now()) + " 获取交通信息"
    with open('log.txt', 'a+') as f:
        # 将文本内容写入文件中
        f.write(content)
    f.close()


