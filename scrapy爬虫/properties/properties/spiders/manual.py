# -*- coding: utf-8 -*-
# time:2023/5/7 9:37
# file manual.py
# outhor:czy
# email:1060324818@qq.com

from urllib.parse import urljoin
import scrapy
from properties.items import PropertiesItem
from scrapy.http import Request

class BasicSpider(scrapy.Spider):
    name = "manual"
    allowed_domains = ["web"]
    start_urls = ["https://geek-docs.com/scrapy/scrapy-tutorials/scrapy-create-project.html"]

    def parse(self, response):
        next_selector = response.xpath('//*[@class="relates"]/li/a//@href')
        for url in next_selector.extract():
            self.log(url)
