import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.jd.com/")
html.encoding = "utf-8"
soup = BeautifulSoup(html.text,'lxml')

atag = soup.select('#navitems-group1 > li:nth-child(1) > a:nth-child(1)')
print(atag[0].string)
