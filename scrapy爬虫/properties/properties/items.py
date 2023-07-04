# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class PropertiesItem(Item):
    # Primary fields
    title = Field()
    price = Field()
    description = Field()
    address = Field()
    image_urls = Field()

    # Calculated fields
    images = Field()
    location = Field()

    # Housekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()

class WeiboreshouItem(scrapy.Item):
    order = scrapy.Field() #热搜排名
    news = scrapy.Field() #热搜新闻
    number = scrapy.Field() #热搜量

class DoubanItem(scrapy.Item):
    ranking = scrapy.Field()    # 排名
    name = scrapy.Field()   # 电影名
    introduce = scrapy.Field()  # 简介
    star = scrapy.Field()   # 星级
    comments = scrapy.Field()   # 评论数
    describe = scrapy.Field()   # 描述
