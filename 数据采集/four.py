# -*- coding: utf-8 -*-
# time:2023/4/26 16:12
# file four.py
# outhor:czy
# email:1060324818@qq.com
import csv
from io import StringIO, BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

from bs4 import BeautifulSoup

"""textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(textPage.read(),'utf-8'))"""

"""data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)

for row in dictReader:
    print(row)"""

data = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(data)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')
wordObj = BeautifulSoup(xml_content.decode('utf-8'),"lxml")
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    print(textElem.text)
