import requests
url = "https://www.amazon.cn/"
try:
          kv = {'User-Agent': 'Mozilla/5.0'}
          url = "https://www.amazon.cn/"
          r = requests.get(url,headers = kv)
          r.raise_for_status()
          r.encoding = r.apparent_encoding
          print(r.text[:1000])
except:
          print("爬取失败")
