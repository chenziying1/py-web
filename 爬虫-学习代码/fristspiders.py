import scrapy

class Test1Spider(scrapy.Spider):
          name = 'fristspiders'
          start_urls = {
                    'https://www.jd.com'
                    }

          def parse(self,response):
                    self.log('hello,world!')
