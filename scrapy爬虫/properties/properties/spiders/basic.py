import scrapy
from properties.items import PropertiesItem

class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["web"]
    start_urls = ["https://geek-docs.com/scrapy/scrapy-tutorials/scrapy-create-project.html"]

    def parse(self, response):
        item = PropertiesItem()
        item['title'] = response.xpath("//h1/a/text()").extract()
        item['text'] = response.xpath("//p/text()").extract()
        item['img'] = response.xpath("//img/@src").extract()
        return item
