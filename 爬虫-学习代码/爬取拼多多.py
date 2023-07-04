from appium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from config import *



desired_cap = {
          'platformName': 'Android', # 平台

          'deviceName': "20200606", # 手机设备名称

          'platformVersion': "9", # 安卓系统版本号

          'appPackage': 'com.xunmeng.pinduoduo', # apk包名

          'appActivity': 'com.xunmeng.pinduoduo.ui.activity.MainFrameActivity', # apk activity
}

class shoppingspider():
          def __init__(self):
                    self.desired_caps = desired_cap
                    self.driver = webdriver.Remote("20200606",self.desired_caps)
                    self.wait = WebDriverWait(self.driver,500)

          def login():
                    el1 = self.wait.until(driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout"))
                    el1.click()
                    el2 = self.wait.until(driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.ListView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.ImageView"))
                    el2.click()
                    sleep(30)

          def shopping():
                    el4 = self.wait.until(driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="搜索"))
                    el4.click()
                    el5 = self.wait.until(driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="搜索"))
                    el5.send_keys("py爬虫")
                    el6 = self.wait.until(driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView"))
                    el6.click()
                    sleep(5)

          def get_friends_info():
                    while True:
                              items = self.wait.until(ec.presence_of_all_elements_located((By.ID,'com.xunmeng.pinduoduo:id/pdd')))
                              for item in items:
                                        try:
                                                  name = item.find_element_by_id('com.xunmeng.pinduoduo:id/tv_title').get_attribute('text')
                                                  jiage = item.find_element_by_id('com.xunmeng.pinduoduo:id/pdd').get_attribute('text')
                                                  xiaoshouqingkuan = item.find_element_by_id('com.xunmeng.pinduoduo:id/pdd').get_attribute('text')
                                                  sleep(1)
                                                  print(name," ",jiage," ",xiaoshouqingkuan)
                                        except NoSuchElementException:
                                                  pass
                    
          
          def start(self):
                    self.login()
                    self.shopping()
                    self.get_friends_info()

spider = shoppingspider()
spider.start()

