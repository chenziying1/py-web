import random
import re
import requests
from bs4 import BeautifulSoup
import json
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



        
def get_content(url):
          browser = webdriver.Edge("C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python39\\msedgedriver.exe")
          browser.get(url)
          time.sleep(10)
          pageSource = browser.text
          return pageSource

url = 'https://vo1.123188kk.com/20211013/LeynXYXG/hls/xP1LmZq3.ts'
contents = get_content(url)
f = open('python链接mysqldemo.ts','w+')
f.write(contents)
f.close()
    
    

    
