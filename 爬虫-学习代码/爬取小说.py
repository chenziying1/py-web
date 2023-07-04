from urllib import request
import re

headers = {
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
          }


def getgale(url):
          req = request.Request(url=url,headers = headers,method = "GET")
          response = request.urlopen(req)
          result = []
          if response.status == 200:
                    html = response.read().decode('gb18030')
                    #print(html)
                    slist = re.findall('<td class="L">.*</td>',html)                    #print(slist)
                    for a in slist:
                              b = {}
                              urls = re.search("([0-9]*\.html)",a)
                              titles = re.search("([\u4e00-\u9fa5])+",a)
                              if urls != None:
                                        url2 = url + urls.group()
                                        b["url"] =  url2 
                              else:
                                        b["url"] = ""
                              if titles != None:
                                        b["titles"] = titles.group()
                              else:
                                        b["titles"] = ""
                              result.append(b)
          return result


def getcontent(goods):
          for good in goods:
                    req = request.Request(url=good["url"],headers = headers,method = "GET")
                    response = request.urlopen(req)
                    if response.status == 200:
                              f = open(good["titles"]+".txt",'a+')
                              contents = re.findall("<dd id=\"contents\".*</dd>",response.read().decode('gb18030'))
                              for i in contents:
                                        f.write(i)
                              f.close()
                              print(good["titles"]+"已完成")

#python链接mysqldemo
goods = getgale(url)
getcontent(goods)
