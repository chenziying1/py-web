# -*- coding: utf-8 -*-
# time:2023/6/10 7:39
# file urls.py
# outhor:czy
# email:1060324818@qq.com


from django.contrib import admin
from django.urls import path, include
from .views import index, jiami, jiemi

urlpatterns = [
    path('',index),
    path('show_message',jiami),
    path('show_message2',jiemi)
]

