import requests
url = "https://mall.jd.com/index-1000073023.html"
try:
          r = requests.get(url)
          r.raise_for_status()
          r.encoding = r.apparent_encoding
          print(r.text[:1000])
except:
          print("爬取失败")
