import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# 设置headers以模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Cookie':'session-id=137-2110609-6269505; session-id-time=2082787201l; i18n-prefs=USD; lc-main=zh_CN; sp-cdn="L5Z9:HK"; ubid-main=131-5040387-8498704; session-token="Ewq21RF6/1aYfUYyL+JOMlB5fDHdiV5j0HGRxgm2WxTdAjqUuMiPZQuO9wj7qN4fBPHNzRYeDUYYPpmzmmXKgRV4SOuTC2ivgXIWopdjeiFNNr0gD3jh7HgZqEpki6btCzlY+fI6/dZDO1sEdmKr1Hx1N+N5aPSvW7DlRbASwbDHYmDxViUebrNOe3qOlkuxiV0nV8RCJObccOQZo933SUxn96gsAK4/i8Jq1u5mm7c="; csm-hit=tb:DNGNFXR56JD6H4WFGWND+b-WXPFJYZVS6VKCMZRGZT7|1690435056902&t:1690435056902&adb:adblk_yes',
}

target_list = ["DeerValley", "TOTO", 'Swiss Madison', 'American Standard', 'Kohler','HOROW','MOHOME',"Fine Fixtures",'Woodbrige']

for i in target_list:
    url = f'https://www.amazon.com/s?k={i}'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    spans = soup.find_all('span', {'class': "s-pagination-item s-pagination-disabled"})

    if spans:
        for j in range(1,spans+1):
            url2 = f"https://www.amazon.com/s?k={i}&page={j}"
            with open("urls.txt","a+",encoding = "utf-8" ) as f:
                f.write(url2+"\n")
            f.close()
            print(url2)
    else:
        with open("urls.txt", "a+", encoding="utf-8") as f:
            f.write(url+"\n")
        f.close()
        print(url)


