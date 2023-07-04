# -*- coding: utf-8 -*-
# time:2023/4/30 10:15
# file 4.30.9.py
# outhor:czy
# email:1060324818@qq.com
import requests

headers = {
    "origin": "https://www.lanqiao.cn",
    "referer": "https://www.lanqiao.cn/questions/6512/",
    "accept":"application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
    "cookie":"_ga=GA1.2.384774285.1672565891; MEIQIA_TRACK_ID=2KtwnKn7qT0xRhE2PSiXvt9IX13; MEIQIA_VISIT_ID=2KtwnN0jq5yVYpNnMjJgzPUZ2Wc; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%224004023%22%2C%22first_id%22%3A%221856cb17c9e470-018d2b3183afef2-26021151-921600-1856cb17c9f7b1%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221856cb17c9e470-018d2b3183afef2-26021151-921600-1856cb17c9f7b1%22%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1NmNiMjFkOTk4ZjctMDVjZjhlODBjZWM0M2I0LTI2MDIxMTUxLTkyMTYwMC0xODU2Y2IyMWQ5YTYxMiIsIiRpZGVudGl0eV9sb2dpbl9pZCI6IjQwMDQwMjMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%224004023%22%7D%7D; lqtoken=a86f66e5cb16a3d1a8a2f71689e62754; _gid=GA1.2.1122178423.1682776686; aliyungf_tc=49999116142fc652b6a218cb40048be98eba8649ac7fae53f9086b96b765773c; Hm_lvt_56f68d0377761a87e16266ec3560ae56=1682154145,1682776683,1682777352,1682813276; platform=LANQIAO-FE; _SESSIONKEY=5d1acdca-0c86-4255-9ca8-59e3bcdb32d4; _LQUSERTYPE=0; Hm_lpvt_56f68d0377761a87e16266ec3560ae56=1682820913"
}

def like(question_id):
    url = "https://www.lanqiao.cn/api/v2/questions/{}/like/".format(question_id)
    r = requests.put(url, headers=headers)
    print(r.ok)

if __name__ == "__main__":
    like(6512)

