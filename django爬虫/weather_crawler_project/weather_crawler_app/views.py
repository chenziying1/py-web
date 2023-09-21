# weather_crawler_app/views.py

from django.shortcuts import render
from django.utils import timezone
import random
import requests
from bs4 import BeautifulSoup
import json
from .models import CrawlerTask


# Mock function to simulate fetching weather data
def fetch_weather_data():


    url = 'http://www.weather.com.cn/weather/101010100.shtml'  # 北京市天气预报网址
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
        humidity = random.randint(0, 100)

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

    return json_data[0]

def task_list(request):
    tasks = CrawlerTask.objects.all()

    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = CrawlerTask.objects.get(pk=task_id)

        if 'enable' in request.POST:
            task.enabled = True
        elif 'disable' in request.POST:
            task.enabled = False
        elif 'run-now' in request.POST:
            data = fetch_weather_data()

            if data is not None:
                # Your code to process the fetched data and update the task status goes here
                task.status = 'Data fetched and processed'
                task.last_run = timezone.now()
            else:
                task.status = 'Error fetching weather data'

        task.save()

    return render(request, 'weather_crawler_app/task_list.html', {'tasks': tasks})
