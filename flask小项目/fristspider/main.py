from firstSpider.DataOotput import DataOutput
from firstSpider.HtmlParse import HtmlParser
from firstSpider.HtmlDownloader import HtmlDownloader
from firstSpider.URLManger import UrlManger

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManger()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def craw(self,root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.downloader(new_url)
                new_urls,data = self.parser.parser(new_url,html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print("一抓取%s个链接"%self.manager.old_url_size())
            except Exception:
                print("123")

        self.output.output_html()

if __name__ == '__main__':
    spider = SpiderMan.SpiderMan()
    spider.crawl("http://www.baidu.com/view/284853.htm")
