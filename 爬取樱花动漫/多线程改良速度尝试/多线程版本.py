#IO密集型程序应该用多线程，所以此时我们使用线程池
import requests
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

def parse_page(res):
    res=res.result()
    print('%s 解析 %s \n' %(current_thread().getName(),len(res)))

def get_page(url):
    print('%s 下载 %s \n' %(current_thread().getName(),url))
    response=requests.get(url)
    if response.status_code == 200:
        return response.text

if __name__ == '__main__':
    urls=['https://www.baidu.com/','http://www.sina.com.cn/','https://www.python.org']

    pool=ThreadPoolExecutor(50)
    # pool=ProcessPoolExecutor(50)
    for url in urls:
        pool.submit(get_page,url).add_done_callback(parse_page)

    pool.shutdown(wait=True)
