# -*- coding: utf-8 -*-
# time:2023/7/17 17:13
# file urls.py
# outhor:czy
# email:1060324818@qq.com
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views
from videowebsite import settings

urlpatterns = [
    path('',views.upload_video,name = "upload_video"),
    path('upload_video',views.upload_video,name = "upload_video"),
    path('video_list',views.video_list,name = "video_list"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

