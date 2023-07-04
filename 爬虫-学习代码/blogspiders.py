import scrapy
from bs4 import *

class blogspiders(scrapy.Spider):
          name = 'blogspiders'
          start_urls = ['https://geekori.com/blogsCenter.php?uid=geekori']

          def parse(self,response):
                    Lists = response.xpath("").extract()
                    for lists in Lists:
                              bs = BeautifulSoup(lists,'lxml')
                              art = {}
                              art['title'] = 

