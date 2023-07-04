# -*- coding: utf-8 -*-
# time:2023/6/9 9:42
# file urls.py
# outhor:czy
# email:1060324818@qq.com
from django.urls import path
from .views import index,add_message
urlpatterns = [
    path('',index),
    path('add_message',add_message),
]
