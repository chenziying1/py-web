# -*- coding: utf-8 -*-
# time:2023/7/25 16:20
# file get_id.py
# outhor:czy
# email:1060324818@qq.com
import json

import requests
urls2 = []
for i in range(1,6):
    url = "https://cqchengshigengxin.com/csgx/xmxx/searchZf?pageNum={0}&jzqk=00".format(i)
    urls2.append(url)
for i in range(1,8):
    url = "https://cqchengshigengxin.com/csgx/xmxx/searchZf?pageNum={0}&jzqk=01".format(i)
    urls2.append(url)
for i in range(1,15):
    url = "https://cqchengshigengxin.com/csgx/xmxx/searchZf?pageNum={0}&jzqk=02".format(i)
    urls2.append(url)
for i in range(1,8):
    url = "https://cqchengshigengxin.com/csgx/xmxx/searchZf?pageNum={0}&jzqk=03".format(i)
    urls2.append(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Cookie': 'SECKEY_ABVK=CGJYfCNp2JCxsUNXhLdDwEzcSlTNkmrWpt5hvK8geqc%3D; BMAP_SECKEY=TK0AcdnQzR-QK1wnoLmy55If0G0BbB6-YDqNviSMkvUekKCTUN4_bzGXhg-ogpmyugWAtpSUAsSGkMy-rPpxtXG343m672Hu49bqvf6rb9oIs7aVpuF-u9MmM00-SL8bBCxOUb3tc282z7TZbVSzwptIGaTIe2xWt4LCA8JKHTXlbE7GgcP2vOOQn-IGLwiw; Hm_lvt_fe91a642e7a8fdc9b5e05008f38c505b=1690258243; JSESSIONID=1009b92f-7b82-4cb8-847d-1615aac6c9e4; SECKEY_ABVK=CGJYfCNp2JCxsUNXhLdDwD2PJtYHZTHuzB3kkOOLHS8%3D; BMAP_SECKEY=TK0AcdnQzR-QK1wnoLmy55f2-Yeo8SEKgdGWpV1NTHswuOMzduNBTeLMCkp2LdRhf2FwuruKsVV8WALdkGz2vrB5bKMp1jDVRpqjRTM7zWZr-4-yMBqaIFO6SCZeVMfmO59Yfsd_mA2DchAwYrXcAMgxfCcxeCULVl4ZFcEhRJIAdB_ITEbUaj05RNEs2-84; Hm_lpvt_fe91a642e7a8fdc9b5e05008f38c505b=1690282239',
    'Host': 'cqchengshigengxin.com',
    'Referer': 'http://cqchengshigengxin.com/csgx/xmxx/zf',
}

for url in urls2:
    response = requests.get(url, headers=headers)
    # Convert the string to JSON
    data = json.loads(response.text)
    print(response.text)
    # Read the 'id' field values
    id_values = [item['id'] for item in data['data']['xmxxList']]
    print(id_values)

    for i in id_values:
        urls="http://cqchengshigengxin.com/csgx/xmxx/details/"+str(i)+"\n"
        with open("url.txt","a+",encoding = "utf-8") as f:
            f.write(urls)
        f.close()
