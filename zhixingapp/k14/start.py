from appium import webdriver
des_leidian = {
        "platformName":"Android",#手机是android还是ios
        "deviceName":"emulator-5554",#手机名称，通过adb devices获得
        "platformVersion":"7.1.2",#android版本号
        "appPackage":"com.yipiao",#app包名
        "appActivity":"com.zt.main.entrance.ZTLaunchActivity",#apk第一个启动页
        "udid":"ca548277",
        "noReset":True#不重置手机app
    }

des_xiaomi9 = {
        "platformName":"Android",#手机是android还是ios
        "deviceName":"ca548277",#手机名称，通过adb devices获得
        "platformVersion":"10",#android版本号
        "appPackage":"com.yipiao",#app包名
        "appActivity":"com.zt.main.entrance.ZTLaunchActivity",#apk第一个启动页
        "udid":"ca548277",#识别手机唯一标志
        "noReset":True#不重置手机app
    }
def start_app(device):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", device)