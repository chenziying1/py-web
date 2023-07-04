import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
          try:
                    r = requests.get(url)
                    r.raise_for_status()
                    r.encoding = r.apparent_encoding
                    return r.text
          except:
                    return ""

def fillUnivList(ulist,html):
          soup = BeautifulSoup(html,"html.parser")
          for tr in soup.find('tbody').children:
                    if isinstance(tr,bs4.element.Tag):
                              tds = tr.find_all("td")
                              tda = tr.find_all("a")
                              ulist.append([tds[0].string,tda[0].string,tds[4].string])

def printunivlist(ulist,num):
    tplt = "{0:^10}\t{1:{3}^}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)),end = "")
                    


def main():
          uinfo = []
          url = "https://www.shanghairanking.cn/rankings/bcur/2021"
          html = getHTMLText(url)
          fillUnivList(uinfo,html)
          printunivlist(uinfo,20)
main()
