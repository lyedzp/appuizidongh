from appium import webdriver
from time import sleep
des = {
        "platformName":"Android",#手机是android还是ios
        "deviceName":"emulator-5554",#手机名称，通过adb devices获得
        "platformVersion":"7.1.2",#android版本号
        "appPackage":"com.yipiao",#app包名
        "appActivity":"com.zt.main.entrance.ZTLaunchActivity",#apk第一个启动页
        "noReset":True#不重置手机app
    }
# appnium服务搭建的地址，这里是在本机上，所以是127.0.0.1
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
sleep(10)
driver.find_element_by_xpath("//*[@text='我的']").click()
sleep(3)
driver.find_element_by_xpath("//*[@text='产品意见']").click()
sleep(3)

#获取当前上下文
# cur = driver.current_context
# print(cur)   NATIVE_APP
# #获取所有上下文context
# all=driver.contexts  ['NATIVE_APP', 'WEBVIEW_com.yipiao']
# print(all)
# sleep(4)
# driver.quit()

#从原生切换到webview(h5)
driver.switch_to.context("WEBVIEW_com.yipiao")
sleep(2)
#查看是否切换
cur = driver.current_context
print(cur)
sleep(3)
#定位webview的元素
driver.find_element_by_id("feedback-content").send_keys('测试')



#切回NATIVE_APP
# driver.switch_to.context("NATIVE_APP")
# print(driver.current_context)