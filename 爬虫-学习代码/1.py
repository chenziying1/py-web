from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re
url = 'https://en.wikipedia.ahau.cf/wiki/Kevin_Bacon'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1"
}
request = Request(url, headers = headers)
resp = urlopen(request)

bs = BeautifulSoup(resp,'html.parser')
for link in bs.find_all('a',href = re.compile('^(/wiki/)((?!:).)*$')):
          if 'href' in link.attrs:
                    print(link.attrs['href'])
          #if 'href' in link.attrs:
                    #print(link.attrs['href'])


                    
