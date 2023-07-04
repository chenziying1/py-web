from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
options = webdriver.EdgeOptions()
options.add_argument('headless')
browser = webdriver.Edge('C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe',options=options)
browser.get('https://www.jd.com')
ul = browser.find_element(By.ID,'navitems-group1')
print(ul.text)
print(ul.id)
print(ul.location)
print(ul.tag_name)
print(ul.size)

