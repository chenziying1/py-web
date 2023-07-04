import os
import requests
import time

def m3u8(filename):
          a = 0
          f = open(filename,'r+')
          while True:
                    url = f.readline()
                    url = url.rstrip()
                    if url == "":
                              break
                    elif 'https:' in url and '.key' not in url:
                              a += 1
          print(a)

m3u8('index.txt')
