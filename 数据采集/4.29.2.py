# -*- coding: utf-8 -*-
# time:2023/4/29 17:58
# file 4.29.2.py
# outhor:czy
# email:1060324818@qq.com
import unittest
from urllib.request import urlopen
from bs4 import BeautifulSoup


class TestWikipedia(unittest.TestCase):
    bsObj = None

    def setUpClass():
        global bsObj
        url = "http://en.wikipedia.org/wiki/Monty_Python"
        bsObj = BeautifulSoup(urlopen(url),"lxml")

    def test_titleText(self):
        global bsObj
        pageTitle = bsObj.find("h1").get_text()
        self.assertEqual("Monty Python", pageTitle)

    def test_contentExists(self):
        global bsObj
        content = bsObj.find("div", {"id": "mw-content-text"})
        self.assertIsNotNone(content)



if __name__ == '__main__':
    unittest.main()
