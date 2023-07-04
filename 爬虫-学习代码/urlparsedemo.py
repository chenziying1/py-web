from urllib.parse import urlparse,urlunparse

result = urlparse('https://baike.baidu.com/item/%E4%B8%96%E7%95%8C%E6%97%85%E6%B8%B8%E7%BB%84%E7%BB%87/470768?fromtitle=%E8%81%94%E5%90%88%E5%9B%BD%E4%B8%96%E7%95%8C%E6%97%85%E6%B8%B8%E7%BB%84%E7%BB%87&fromid=15775365&fr=aladdin')

print(result.scheme)
print(result.netloc)
print(result.path)
print(result.params)
print(result.query)
print(result.fragment)

data = ['https','baike.baidu.com','/item/%E4%B8%96%E7%95%8C%E6%97%85%E6%B8%B8%E7%BB%84%E7%BB%87/470768','',
        'fromtitle=%E8%81%94%E5%90%88%E5%9B%BD%E4%B8%96%E7%95%8C%E6%97%85%E6%B8%B8%E7%BB%84%E7%BB%87&fromid=15775365&fr=aladdin','']
print(urlunparse(data))
