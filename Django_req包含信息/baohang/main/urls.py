# -*- coding: utf-8 -*-
# time:2023/6/12 17:11
# file urls.py
# outhor:czy
# email:1060324818@qq.com
from django.urls import path
from .views import index

urlpatterns = [
    path('',index),
]
