# -*- coding: utf-8 -*-
# time:2023/6/10 20:51
# file urls.py
# outhor:czy
# email:1060324818@qq.com
from django.urls import path
from .views import index,genxing

urlpatterns = [
    path('',index),
    path('python链接mysqldemo',genxing)
]