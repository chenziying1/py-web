# -*- coding: utf-8 -*-
# time:2023/7/20 23:26
# file index.py
# outhor:czy
# email:1060324818@qq.com
import random

import requests
from bs4 import BeautifulSoup
import json

url = 'http://www.weather.com.cn/weather/101010100.shtml'   # 北京市天气预报网址
response = requests.get(url)
response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, 'html.parser')
weather_div = soup.find('div', {'id': '7d'})
weather_ul = weather_div.find('ul')
weather_li = weather_ul.find_all('li')

weather_data = []

for day_weather in weather_li:
    date = day_weather.find('h1').string
    weather = day_weather.find_all('p')


    temperature = weather[0].string
    weather_type = weather[1].string
    wind = weather[2].find('span')['title']
    humidity = random.randint(0,100)


    weather_dict = {
        'date': date,
        'temperature': temperature,
        'weather_type': weather_type,
        'wind': wind,
        'humidity': humidity
    }
    weather_data.append(weather_dict)

json_data = json.dumps(weather_data, indent=4, ensure_ascii=False)
print(json_data)


