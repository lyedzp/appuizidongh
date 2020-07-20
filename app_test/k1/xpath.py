from appium import webdriver
from time import sleep
#显式等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
des = {
        "platformName":"Android",#手机是android还是ios
        "deviceName":"emulator-5554",#手机名称，通过adb devices获得
        "platformVersion":"7.1.2",#android版本号
        "appPackage":"com.taobao.taobao",#app包名
        "appActivity":"com.taobao.tao.welcome.Welcome",#apk第一个启动页
        # Uiautomator2支持toast
        "automationName":"Uiautomator2",
        "noReset":True#不重置手机app
    }
# appnium服务搭建的地址，这里是在本机上，所以是127.0.0.1
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
sleep(10)

#通过文本定位
# driver.find_element_by_xpath('//*[@text = "注册/登录"]').click()
#通过id定位
# driver.find_element_by_xpath('//*[@resource-id = "com.taobao.taobao:id/iv_image"]').click()
#通过class定位
# driver.find_element_by_xpath('//*[@android.widget.ImageView = "com.taobao.taobao:id/iv_image"]').click()
# #通过content-desc定位
# driver.find_element_by_xpath('//*[@content-desc = "content-desc的文本"]').click()
#contains用法
driver.find_element_by_xpath('//*[contains(@text,"登录")]').click()
