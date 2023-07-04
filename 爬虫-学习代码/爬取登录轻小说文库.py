from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
options = webdriver.EdgeOptions()
options.add_argument('headless')
browser = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe',options=options)

def get_info():
          browser.get('https://www.wenku8.net/login.php?jumpurl=http%3A%2F%2Fwww.wenku8.net%2Findex.php')
          name = browser.find_elements(By.CLASS_NAME,'text')[0].send_keys(3337026057)
          password = browser.find_elements(By.CLASS_NAME,'text')[1].send_keys('czy123456')
          login = browser.find_elements(By.CLASS_NAME,'button')[0].click()
          time.sleep(5)
          print('登录成功')
          ul = browser.find_elements(By.CLASS_NAME,'navlist')[0]
          li_list = ul.find_elements(By.TAG_NAME,'li')
          for li in li_list:
                    print(li.text)
                    a = li.find_element(By.TAG_NAME,'a')
                    print(a.text)


get_info()          


