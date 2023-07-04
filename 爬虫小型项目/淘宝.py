#CrowTaobaoPrice.py
import requests
import re

def getHTMLText(url):
    try:
          kv = {'User-Agent': 'Mozilla/5.0'}
          r = requests.get(url,headers = kv)
          r.raise_for_status()
          r.encoding = r.apparent_encoding
          return r.text
    except:
        return ""
    
def parsePage(ilt, html):
    try:
        print("1")
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        print(plt)
        tlt = re.findall(r'\"title\"\:\".*?\\u',html)
        print("3")
        for i in range(len(plt)):
            print("4")
            price = eval(plt[i].split(':')[1])
            print(price)
            title = eval(tlt[i].split(':')[1])
            print(tirle)
            ilt.append([price , title])
    except:
        print("")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
        
def main():
    goods = '书包'
    depth = 2
    start_url = ['https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.21814703.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E4%B9%A6%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest','https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.21814703.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E4%B9%A6%E5%8C%85&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&bcoffset=4&p4ppushleft=2%2C48&s=44&ntoffset=4']
    infoList = []
    for i in range(depth):
        try:
            url = start_url[i]
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
    
main()
