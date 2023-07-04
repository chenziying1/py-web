# -*- coding: utf-8 -*-
# time:2023/4/27 14:34
# file five.py
# outhor:czy
# email:1060324818@qq.com
import operator
import re
import string
from collections import OrderedDict
from urllib.request import urlopen
from bs4 import BeautifulSoup

def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it","i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
     "they", "is", "an", "at", "but","we", "his", "from", "that", "not",
     "by", "she", "or", "as", "what", "go", "their","can", "who", "get",
     "if", "would", "her", "all", "my", "make", "about", "know", "will",
     "as", "up", "one", "time", "has", "been", "there", "year", "so",
     "think", "when", "which", "them", "some", "me", "people", "take",
     "out", "into", "just", "see", "him", "your", "come", "could", "now",
     "than", "like", "other", "how", "then", "its", "our", "two", "more",
     "these", "want", "way", "look", "first", "also", "new", "because",
     "day", "more", "use", "no", "man", "find", "here", "thing", "give",
     "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False


def cleanInput(data):
    data = re.sub('\n+'," ",data)
    data = re.sub('\[[0-9]*\]',"",data)
    data = re.sub(' +'," ",data)
    data = bytes(data,"UTF-8")
    data = data.decode("ascii", "ignore")
    cleanInputs = []
    data = data.split(" ")
    for item in data:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInputs.append(item)
    return cleanInputs


def ngrams(data,n):
    inputs = cleanInput(data)
    output = {}
    for i in range(len(inputs) - n + 1):
        ngramsTemp = " ".join(inputs[i:i+n])
        if isCommon(ngramsTemp):
            if ngramsTemp not in output:
                output[ngramsTemp] = 1
            output[ngramsTemp] += 1
    return output




"""
data = data.upper()
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsobj = BeautifulSoup(html,"lxml")
content = bsobj.find("div", {"id":"mw-content-text"}).get_text()
ngram = sorted(ngram, key = operator.itemgetter(1), reverse=True)
"""
content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')
ngram = ngrams(content, 2)
ngram = sorted(ngram.items(), key=lambda d: d[1], reverse=True)
print(ngram)
print("2-grams count is: "+str(len(ngram)))
