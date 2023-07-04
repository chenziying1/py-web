import scrapy
from news.items import NewsItem
from scrapy.loader import ItemLoader


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['https://news.baidu.com/']

    def parse(self, response):
        #item = NewsItem()
        #item['title'] = response.xpath('').extract() + response.xpath('').extract()
        #item['url'] = response.xpath('').extract() + response.xpath('').extract()
        #用这种方式才能获取到全部的内容，loader不用这么麻烦

        """ This function parses a property page.

        @url https://news.baidu.com/
        @returns items 1
        @scrapes title url
        """

        I = ItemLoader(item=NewsItem(),response=response)

        I.add_xpath('title','//*[@id="pane-news"]/ul/li/a/text()')
        I.add_xpath('url','//*[@id="pane-news"]/ul/li/a/@href')

        I.add_xpath('title', '//*[@id="pane-news"]/div/ul/li/strong/a/text()')
        I.add_xpath('url', '//*[@id="pane-news"]/div/ul/li/strong/a/@href')


        return I.load_item()


