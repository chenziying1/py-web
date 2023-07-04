import requests
keyword = "Python"
url = "http://www.baidu.com/"
try:
          kv = {'wd': keyword}
          r = requests.get(url,params = kv)
          r.raise_for_status()
          r.encoding = r.apparent_encoding
          print(len(r.text))
          print(r.text[:1000])
except:
          print("爬取失败")
