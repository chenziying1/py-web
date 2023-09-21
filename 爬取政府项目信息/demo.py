# -*- coding: utf-8 -*-
# time:2023/7/25 12:37
# file index.py
# outhor:czy
# email:1060324818@qq.com
import requests
from bs4 import BeautifulSoup

#1.获取页面信息，如果获取不了，就会返回一个404信息页面，所以是一定有消息的
def get_response(url):
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'Cookie': 'SECKEY_ABVK=CGJYfCNp2JCxsUNXhLdDwBk1b9QsT4T+VamozGRDOp4%3D; BMAP_SECKEY=TK0AcdnQzR-QK1wnoLmy5wSSlNqazRB0glQxsihJsU3zM1IFkLyUeMubVoNRtfkjj5fa0tWDfXp60H1weBrixEkBSsnQQDy6KkhIcOxEtjcGazXmKquUFPhS74ojqbu7EWHwbuoXaW11ruIvoteHxS9p0Kk2cQf9Qc7vx4tn8pJYHri-AUrfrtNL4Qib-oNE; Hm_lvt_fe91a642e7a8fdc9b5e05008f38c505b=1690258243; JSESSIONID=1009b92f-7b82-4cb8-847d-1615aac6c9e4; SECKEY_ABVK=CGJYfCNp2JCxsUNXhLdDwD2PJtYHZTHuzB3kkOOLHS8%3D; BMAP_SECKEY=TK0AcdnQzR-QK1wnoLmy55f2-Yeo8SEKgdGWpV1NTHswuOMzduNBTeLMCkp2LdRhf2FwuruKsVV8WALdkGz2vrB5bKMp1jDVRpqjRTM7zWZr-4-yMBqaIFO6SCZeVMfmO59Yfsd_mA2DchAwYrXcAMgxfCcxeCULVl4ZFcEhRJIAdB_ITEbUaj05RNEs2-84; Hm_lpvt_fe91a642e7a8fdc9b5e05008f38c505b=1690284157',
                'Host': 'cqchengshigengxin.com',
                'Referer': 'http://cqchengshigengxin.com/csgx/xmxx/zf',
        }

        response = requests.get(url, headers=headers)
        return response.text

def  get_data(response):
        soup = BeautifulSoup(response, 'html.parser')
        text = soup.get_text()
        text_list = [t.strip() for t in text.split('\n') if t.strip()]
        return text_list

def save_data(text_list):
        with open("data.txt","a+",encoding="utf-8") as f:
                f.write(str(text_list))
        f.close()


def main():
        with open("url.txt","r",encoding="utf-8") as f:
                lines = f.readlines()
                lines = [line.strip() for line in lines]
                for url in lines:
                        response = get_response(url)
                        text_list = get_data(response)
                        if len(text_list) <= 1 or "403" in text_list or "您没有访问权限" in text_list:
                                print("页面403 "+url)
                        else:
                                save_data(text_list)
                        print(text_list)
        f.close()

if __name__ == "__main__":
        main()
