from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe')
browser.get('https://www.jd.com/')
actions = ActionChains(browser)
li_list = browser.find_elements(By.CSS_SELECTOR,".cate_menu_item")
for li in li_list:
          actions.move_to_element(li).perform()
          time.sleep(1)
