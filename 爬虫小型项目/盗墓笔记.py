import json
import requests
from bs4 import BeautifulSoup


kv = {'User-Agent': 'Mozilla/5.0'}
url = "http://seputu.com/"
r = requests.get(url,headers = kv)
r.raise_for_status()
#r.encoding = r.apparant_encoding
soup = BeautifulSoup(r.text,'html.parser',from_encoding = 'utf-8')
content=[]
for muln in soup.find_all(class_= "mulu"):
          h2 = muln.find('h2')
          print(h2)
          if h2 != None:
                    h2_title = h2.string
                    print(h2.string)
                    list_=[]
                    for a in muln.find(class_='box').find_all('a'):
                              #print(a)
                              href = a.get('href')
                              box_title = a.get('title')
                              list_.append({'href':href,'box_title':box_title})
                    content.append({'title':h2_title,'content':list_})
with open('qiye.json','w+') as fp:
          print('1')
          json.dump(content,fp=fp,indent=4)
          print('1')

