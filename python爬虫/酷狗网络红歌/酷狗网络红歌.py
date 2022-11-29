import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}


def find_info(url):
          html = requests.get(url,headers=headers)
          html.encoding = "utf-8"
          soup = BeautifulSoup(html.text,'lxml')
          ranks = soup.select("#rankWrap > div.pc_temp_songlist > ul > li> span.pc_temp_num")
          titles = soup.select("#rankWrap > div.pc_temp_songlist > ul > li > a")
          times = soup.select("#rankWrap > div.pc_temp_songlist > ul > li> span.pc_temp_tips_r > span")
          for rank,title,time in zip(ranks,titles,times):
                    data = {'rank':rank.get_text().strip(),'signer':title.get_text().split('-')[0].strip(),'song':title.get_text().split('-')[1].strip(),'time':time.get_text().strip()}
                    print(data)
                    
          


urls = ['https://www.kugou.com/yy/rank/home/{}-23784.html'.format(i) for i in range(1,11)]
for url in urls:
          find_info(url)
