# -*- coding: utf-8 -*-
# time:2023/4/26 14:31
# file three.py
# outhor:czy
# email:1060324818@qq.com mignon
import json
import re
from datetime import datetime
from random import random, seed
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getLinks(url):
    html = urlopen("http://en.wikipedia.org" + url)
    bsObj = BeautifulSoup(html,"lxml")
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(url):
    pageUrl = url.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("history url is: " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html,"lxml")
    ipAddresses = bsObj.findAll("a", {"class": "mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountry(ipAddress):
    try:
        response = urlopen("https://ip.cn/ip/"+ipAddress+".html")
    except HTTPError:
        return None
    bsObj = BeautifulSoup(response, "lxml")
    CountryAddresses = bsObj.find("div", {"id": "tab0_address"})
    print(response,CountryAddresses)
    return CountryAddresses


links = getLinks("/wiki/Python_(programming_language)")

while len(links) > 0:
    for link in links:
        print("-------------------")
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            print(historyIP)
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP + " is from " + country)
    newLink = links[random.randint(0, len(links) - 1)].attrs["href"]
    links = getLinks(newLink)
