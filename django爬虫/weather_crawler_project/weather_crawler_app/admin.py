from django.contrib import admin

# Register your models here.
# weather_crawler_app/admin.py

from django.contrib import admin
from .models import CrawlerTask

admin.site.register(CrawlerTask)

