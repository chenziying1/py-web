import requests

class HtmlDownloader(object):
    def downloader(self,url):
        if url is None:
            return None
        kv = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None