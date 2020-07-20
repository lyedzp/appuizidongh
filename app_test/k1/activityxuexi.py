from appium import webdriver
from time import sleep
from k1.fengzhuangdingwei import Base
des = {
        "platformName":"Android",#手机是android还是ios
        "deviceName":"emulator-5554",#手机名称，通过adb devices获得
        "platformVersion":"7.1.2",#android版本号
        "appPackage":"com.taobao.taobao",#app包名
        "appActivity":"com.taobao.tao.welcome.Welcome",#apk第一个启动页
        # Uiautomator2支持toast
        # "automationName":"Uiautomator2",
        "noReset":True#不重置手机app
    }
# appnium服务搭建的地址，这里是在本机上，所以是127.0.0.1
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
sleep(10)

#获取当前页面activity
# curr = driver.current_activity
# print(curr)

#等待activity启动完成,在20s内完成就行
# driver.wait_activity("com.taobao.tao.TBMainActivity",20)
# base = Base(driver)
# base.find({"by":"text","value":"注册/登录"}).click()

#不点按钮，直接切换到某个activity,第一个传包名，第二个传需要跳转到的activity
#start_activity的好处：可以写在setup方法里面，让每条用例都从某个activity开始执行
driver.start_activity("com.taobao.taobao","com.ali.user.mobile.login.ui.UserLoginActivity")
sleep(10)