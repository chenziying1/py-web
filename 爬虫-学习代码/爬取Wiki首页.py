from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def geturl(url):
          global pages
          html = urlopen('https://zh.wikipedia.ahau.cf/wiki/{}'.format(url))
          bs = Bea
