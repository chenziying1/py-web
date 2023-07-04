import requests

def parse_page(res):
    print('解析 %s' %(len(res)))
def get_page(url):
    print('下载 %s' %url)
    response=requests.get(url)
    if response.status_code == 200:
        return response.text
urls=['https://www.baidu.com/','http://www.sina.com.cn/','https://www.python.org']
for url in urls:
    res=get_page(url) #调用一个任务，就在原地等待任务结束拿到结果后才继续往后执行
    parse_page(res)
