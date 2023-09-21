# -*- coding: utf-8 -*-
# time:2023/9/3 20:42
# file demo.py
# outhor:czy
# email:1060324818@qq.com
import json

import requests

AK = "W16W0C5FSsLloaq8Z6HjHphu48GMvKu5"

def getPosition(address):
    url = r"http://api.map.baidu.com/place/v2/search?query={}&region=全国&output=json&ak={}".format(
        address,
        AK  # 自动调用，不用修改
    )
    res = requests.get(url)
    json_data = json.loads(res.text)

    if json_data["status"] == 0:
        lat = json_data["results"][0]["location"]["lat"]  # 纬度
        lng = json_data["results"][0]["location"]["lng"]  # 经度
    else:
        print(json_data["message"])
        return "0,0", json_data["status"]
    return str(lat) + "," + str(lng), json_data["status"]


def getDistance(start, end):
    url = "https://api.map.baidu.com/directionlite/v1/driving?origin={}&destination={}&ak={}".format(
        start,
        end,
        AK  # 自动调用，不用修改
    )
    res = requests.get(url)
    json_data = json.loads(res.text)

    if json_data["status"] == 0:
        return json_data["result"]["routes"][0]["distance"]
    else:
        print(json_data["message"])
        return -1

def calcDistance(startName, endName):
    start, status1 = getPosition(startName)
    end, status2 = getPosition(endName)
    if status1 == 0 and status2 == 0:
        return getDistance(start, end)
    else:
        return -1

if __name__ == "__main__":
    print("预计有"+str(int(calcDistance("北京","上海"))/1000)+"公里")