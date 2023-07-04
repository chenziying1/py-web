# -*- coding: utf-8 -*-
# time:2023/7/1 20:44
# file urls.py
# outhor:czy
# email:1060324818@qq.com
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import fristcontact,secondcontact,threecontact,save_page,view_page,change_view
import sys
import os

# 将parent_path替换成你的项目所在的绝对路径
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(parent_path)
from JL import settings # 从项目根目录开始

urlpatterns = [
    path('',views.show_category, name='show_category'),
    path('frist/',views.frist,name='frist'),
    path('frist/contact/',fristcontact, name='fristcontact'),
    path('second/contact/',secondcontact, name='secondcontact'),
    path('three/contact/',threecontact, name='threecontact'),
    path('save_page/', save_page, name='save_page'),
    path('view_page/<str:file_name>/', view_page, name='view_page'),
    path('change_pdf', change_view, name='change_view'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


