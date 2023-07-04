import requests
url = "https://s.taobao.com/search?q=%E4%B9%A6%E5%8C%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.21814703.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=6&ntoffset=6&p4ppushleft=2%2C48&s=0"
try:
          kv = {'User-Agent': 'Mozilla/5.0'}
          r = requests.get(url,headers = kv)
          r.raise_for_status()
          r.encoding = r.apparent_encoding
          print(r.text[:1000])
except:
          print("爬取失败")
