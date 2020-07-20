from appium import webdriver
from time import sleep
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
#id定位
# driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
# sleep(3)
# driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()

#文本定位
# driver.find_element_by_xpath("//*[@text='医药']").click()
# sleep(10)
# #contains语法
# driver.find_element_by_xpath("//*[contains(@text,'补肾')]").click()
#通过描述定位
# driver.find_element_by_accessibility_id("购物车").click()


# ------------通过Uiautomator高级组合定位-----------------------
#通过id和class定位
# idAndcls = 'resourceId("com.taobao.taobao:id/iv_image").className("android.widget.ImageView")'
# driver.find_element_by_android_uiautomator(idAndcls).click()

#通过父子关系联合定位
f_sun = 'className("android.widget.FrameLayout").childSelector(resourceId("com.taobao.taobao:id/iv_image"))'
driver.find_element_by_android_uiautomator(f_sun).click()

#通过兄弟定位
# f_sun = 'className("android.widget.FrameLayout").fromParent(resourceId("com.taobao.taobao:id/iv_image"))'
# driver.find_element_by_android_uiautomator(f_sun).click()

sleep(3)
driver.quit()









