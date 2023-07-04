from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from appium import webdriver
server = "http://localhost:4723/wd/hub"

desired_caps = {
  'platformName': 'Android', # 被测手机是安卓
  'platformVersion': '9', # 手机安卓版本
  'deviceName': '20200606', # 设备名，安卓手机可以随意填写
  'appPackage': 'com.tencent.mm', # 启动APP Package名称
  'appActivity': 'com.tencent.mm.ui.LauncherUI' # 启动Activity名称
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

wait = WebDriverWait(driver,20)

login = wait.until(ec.presence_of_element_located((By.ID,'com.tencent.mm:id/e80')))

print(login)

login.click()

phone = wait.until(ec.presence_of_element_located((By.ID,'com.tencent.mm:id/13')))

phone.set_text('88888888')
