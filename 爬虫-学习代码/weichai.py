from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from weichai_config import *
from selenium.common.exceptions import NoSuchElementException


class frindsprider():

          def __init__(self):
                    self.desired_caps = {
                      'platformName': 'Android', # 被测手机是安卓
                      'platformVersion': '9', # 手机安卓版本
                      'deviceName': '20200606', # 设备名，安卓手机可以随意填写
                      'appPackage': 'com.tencent.mm', # 启动APP Package名称
                      'appActivity': 'com.tencent.mm.ui.LauncherUI' # 启动Activity名称
                    }
                    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
                    self.wait = WebDriverWait(driver,20)

          def login_weixin(self):
                    el1 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/j_9")
                    el1.click()
                    el2 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/g5x")
                    el2.click()
                    el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText")
                    el3.send_keys("13229539388")
                    el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.EditText")
                    el4.send_keys("czy10603248181")
                    el5 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/g5o")
                    el5.click()
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(587, 635)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.move_to_location(493, 643)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(117, 587)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(152, 603)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.move_to_location(544, 589)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(245, 1195)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(365, 1285)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(368, 1173)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(309, 552)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(341, 603)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(93, 851)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(264, 741)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(349, 739)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(163, 765)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
                        
                    actions = ActionChains(driver)
                    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
                    actions.w3c_actions.pointer_action.move_to_location(219, 979)
                    actions.w3c_actions.pointer_action.pointer_down()
                    actions.w3c_actions.pointer_action.pause(0.1)
                    actions.w3c_actions.pointer_action.release()
                    actions.perform()
    

                    
          

sprider = frindsprider()
sprider.start()

'''

el1 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/j_9")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/cd7")
el2.send_keys("13229539388")
el3 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/hfe")
el3.click()
el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.EditText")
el4.send_keys("czy10603248181")
el5 = driver.find_element(by=AppiumBy.ID, value="com.tencent.mm:id/hfe")
el5.click()
driver.switch_to.context('NATIVE_APP')

'''

