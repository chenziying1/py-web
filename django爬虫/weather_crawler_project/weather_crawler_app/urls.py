# -*- coding: utf-8 -*-
# time:2023/7/20 20:21
# file urls.py
# outhor:czy
# email:1060324818@qq.com

# weather_crawler_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('task-list', views.task_list, name='task_list'),
    # Add more URL patterns for other views if needed
]

