import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 设置headers以模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Cookie':'session-id=137-2110609-6269505; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=131-5040387-8498704; lc-main=en_US; sp-cdn="L5Z9:CN"; session-token=RmYRbhFuJEYp3uoCglQ7L1dcLic5RUdEKOfgZiZstDgassCoMbQMmoVsHt+hdR85xvdXlyNkbYGdIGHi68DeICmHwS7CKWjUquK+fZy2czEoWYy3fE/it+q1wm+MKgIb77U7NVm9brwD5eIfsRQnx1+aOC7kEfBZpV+1tSClxFkq79gWE5iBQ8jpOdeKOMaMPSq/vVhR27166ushaR/ljg6wmG0CIZTrKdfa6s933SW410SoGzJgrxGV8BXB5EF7HJLmMfDQsWaTIc0ublTb1xC2wKblGQHqt2+xkXhKzBehSn6ffiBmzJSdTNwonYtIOoasCi6Mzadlxc98yTJld71+3yZKlcZi; csm-hit=tb:10F53XEGR29Q7WRESJA7+s-10F53XEGR29Q7WRESJA7|1694766701671&t:1694766701671&adb:adblk_no',
}

def get_amazon_url(url):
    target2_list = set()
    if url:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            spans = soup.find_all('a', class_="Overlay__overlay__LloCU ProductGridItem__overlay__IQ3Kw")
        except:
            spans = ""

        if spans:
            for i in spans:
                target2 = i['href']
                target2_list.add("https://www.amazon.com/"+target2)
            ans = list(target2_list)
            with open("amazon_url.txt", "a+", encoding="utf-8") as f:
                for i in ans:
                    f.write(i+"\n")
            f.close()
    else:
        print("发生错误")



target_list = []

with open("amzon_url.txt","r",encoding = "utf-8") as f:
    target = f.readlines()
    for i in target:
        target_list.append(i.replace("\n",""))
f.close()


for url in target_list:
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        spans = soup.find_all('li', class_="Navigation__navItem__bakjf")
    except:
        spans = ""

    if spans:
        for i in spans:
            try:
                target2 = i.find("a")['href']
                target2 = "https://www.amazon.com"+target2
                get_amazon_url(target2)
            except:
                print("i是空值")
    else:
        print("未获取到信息，也许是cookie失效？")

