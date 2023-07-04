# -*- coding: utf-8 -*-
# time:2023/7/1 20:44
# file urls.py
# outhor:czy
# email:1060324818@qq.com
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import contact
import sys
import os

# 将parent_path替换成你的项目所在的绝对路径
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parent_path)
from demo import settings # 从项目根目录开始

urlpatterns = [
    path('',views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('frist/',views.frist,name='frist'),
    path('contact/', contact, name='contact'),
    path('upload/', views.upload, name='upload'),
    path('media/', views.image_list, name='image_list'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


