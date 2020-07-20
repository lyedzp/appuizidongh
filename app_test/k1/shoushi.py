from appium import webdriver
from time import sleep
from k1 import base
des = {
        "platformName":"Android",#手机是android还是ios
        "deviceName":"emulator-5554",#手机名称，通过adb devices获得
        "platformVersion":"7.1.2",#android版本号
        "appPackage":"com.taobao.taobao",#app包名
        "appActivity":"com.taobao.tao.welcome.Welcome",#apk第一个启动页
        "noReset":True#不重置手机app
    }
# appnium服务搭建的地址，这里是在本机上，所以是127.0.0.1
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
sleep(5)



#封装向上滑动方法
# def swipeUp(driver):
#     # 滑动
#     a = driver.get_window_size()  # 获取屏幕分辨率
#     print(a)  # {'width': 1080, 'height': 1920}
#     width = a['width']
#     height = a['height']
#     start_x = width / 2
#     start_y = height / 5 * 4
#
#     end_x = width / 2
#     end_y = height / 5 * 1
#     # 往上滑动
#     driver.swipe(start_x, start_y, end_x, end_y)
#
# #封装向下滑动方法
# def swipeDown(driver):
#     # 滑动
#     a = driver.get_window_size()  # 获取屏幕分辨率
#     print(a)  # {'width': 1080, 'height': 1920}
#     width = a['width']
#     height = a['height']
#     start_x = width / 2
#     start_y = height / 5 * 1
#
#     end_x = width / 2
#     end_y = height / 5 * 4
#     # 往下滑动
#     driver.swipe(start_x, start_y, end_x, end_y)
# swipeUp(driver)
# swipeDown(driver)

#将上面两个方法封装到公共类Base中
# c = base.Base(driver)
# c.swipeUp()
# c.swipeDown()


#tap,触摸
#有时候定位元素的时候，你使出了十八班武艺还是定位不到，怎么办呢？（面试经常会问）那就拿出绝招：点元素所在位置的坐标
t = base.Base(driver)
t.tab_new(x=819,y=1204)
