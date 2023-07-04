import requests
url = "https://www.ip138.com/iplookup.asp?ip="
kv = {'User-Agent': 'Mozilla/5.0'}
try:
          r = requests.get(url + '202.204.80.112',headers = kv)
          r.raise_for_status()
          r.encoding = r.apparent_encoding
          print(r.text[:1000])
except:
          print("爬取失败")
