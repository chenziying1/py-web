# -*- coding: utf-8 -*-
# time:2023/6/7 23:00
# file urls.py
# outhor:czy
# email:1060324818@qq.com
from django.urls import path
from .views import index, change

urlpatterns = [
    path('',index),
    path('about/',change),
]

