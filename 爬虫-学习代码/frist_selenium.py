from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

browser = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
try:
          browser.get('https://www.jd.com/')
          inputs = browser.find_element(by=By.ID ,value = 'key')
          inputs.send_keys('py爬虫')
          inputs.send_keys(Keys.ENTER)
          wait = WebDriverWait(browser,4)
          wait.until(ec.presence_of_all_elements_located((By.ID,'J_goodsList')))
          print(browser.page_source)
          browser.close()
except Exception as e:
          print(e)
          browser.close()
