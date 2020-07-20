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
def is_toast_exist(driver,_text):
        locator = ('xpath','.//*[contains(@text,"%s")]'%_text)
        #加try except主要是为了防止点返回有时失效或没点到产生的异常
        try:
            # 超时时间30S,每0.3秒查找一次
            ele = WebDriverWait(driver, 20, 0.3).until(EC.presence_of_element_located(locator))
            t = ele.text
            print(t)
            if _text in t:
                return True
            else:
                return False
        except:
            return False
driver.back()  # 返回键
text = "再按一次"
r = is_toast_exist(driver,text)
print(r)