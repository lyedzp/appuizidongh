import sys,os
# sys.path.extend(['D:\\appuizidongh\\kuaikuaiapp'])#加入这2行是因为在命令行运行直接运行test_01时会找不到zhixingapp这个模块，把路径加上，命令行运行时就可以了
sys.path.extend(['D:\\appuizidongh'])
from kuaikuaiapp.common.start import start_app
from kuaikuaiapp.common.fengzhuangdingwei import BaseApp
import unittest
import warnings
from selenium import webdriver
from kuaikuaiapp.common.base import Base

class Login(unittest.TestCase):
    # 'resourceId("com.taobao.taobao:id/iv_image").className("android.widget.ImageView")'
    # my='text("我的")'
    my = {'by': 'text', 'value': '我的'}
    pwdlogin = {'by': 'text', 'value': '密码登录'}
    phone = {'by': 'text', 'value': '请输入11位手机号'}
    pwd = {"by":"text","value":"请输入密码"}
    login = {"by": "text", "value": "登录"}
    set = {"by" :"com.tckk.kk:id/setting","value":"com.tckk.kk:id/setting"}
    loginOut = {"by": "text", "value": "退出登录"}
    loginOut2 = {"by": "text", "value": "退出登录"}
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.driver,cls.devicename = start_app()
        print(cls.devicename)
        cls.driver.wait_activity("com.tckk.kk/com.tckk.kk.ui.home.HomeActivity", 10)
        cls.base = BaseApp(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def test_one(self):
        # xiaomi9pro  [941,2286][1001,2327]  xiaomi9 	[938,2156][1004,2199]   vivo[934,2081][1009,2141]
        # self.driver.find_element_by_xpath('//*[@text = "我的"]').click()
        account = [{'phone':"17380578335",'pwd':'lye1222085',"width":1080,"height":2141},
                   {'phone':"18084822054",'pwd':'lye1222085',"width":1080,"height":2135}]

        if self.devicename  == "vivo":
            t = Base(self.driver)
            x, y = t.getX_Y(account[0]["width"], account[0]["height"])
            t.tab_new(x=x, y=y)
            self.base.click(self.pwdlogin)
            self.base.clear(self.phone)
            self.base.send(self.phone, account[0]['phone'])
            self.base.send(self.pwd, account[0]['pwd'])
            self.base.click(self.login)
        elif self.devicename == "xiaomi9":
            t = Base(self.driver)
            x, y = t.getX_Y(account[1]["width"], account[1]["height"])
            t.tab_new(x=x, y=y)
            self.base.click(self.pwdlogin)
            self.base.send(self.phone, account[1]['phone'])
            self.base.send(self.pwd, account[1]['pwd'])
            self.base.click(self.login)
        #
        # t = Base(self.driver)
        # x, y = t.getX_Y(account[0]["width"], account[0]["height"])
        # print(x,y)
        # t.tab_new(x=x, y=y)
        # self.base.click(self.pwdlogin)
        # self.base.send(self.phone, account[0]['phone'])
        # self.base.send(self.pwd, account[0]['pwd'])
        # self.base.click(self.login)

        # t = Base(self.driver)
        # x, y = t.getX_Y(account[1]["width"], account[1]["height"])
        # print(x,y)
        # t.tab_new(x=x, y=y)
        # self.base.click(self.pwdlogin)
        # self.base.send(self.phone, account[1]['phone'])
        # self.base.send(self.pwd, account[1]['pwd'])
        # self.base.click(self.login)

        # elif self.devicename == "xiaomi9":
        #         x, y = t.getX_Y(item["width"], item["height"])
        #             t.tab_new(x=x, y=y)
        #             self.base.click(self.pwdlogin)
        #             self.base.send(self.phone, item['phone'])
        #             self.base.send(self.pwd, item['pwd'])
        #             self.base.click(self.login)
        #             return True
        #     print(account[0])
        # for item in account:
        #     if self.devicename == "vivo":
        #         print(item[0])
        #     if self.devicename == "vivo":
        #         print(self.devicename)
        #         x, y = t.getX_Y(item["width"], item["height"])
        #         t.tab_new(x=x, y=y)
        #         self.base.click(self.pwdlogin)
        #         self.base.send(self.phone, item['phone'])
        #         self.base.send(self.pwd, item['pwd'])
        #         self.base.click(self.login)
        #         yield 1
        #
        #
        #     elif self.devicename == "xiaomi9":
        #         x, y = t.getX_Y(item["width"], item["height"])
        #         t.tab_new(x=x, y=y)
        #         self.base.click(self.pwdlogin)
        #         self.base.send(self.phone, item['phone'])
        #         self.base.send(self.pwd, item['pwd'])
        #         self.base.click(self.login)
        #         return True




        # t.tab_new(x=x,y=y)
        #
        # self.base.click(self.set)
        # self.base.click(self.loginOut)
        # self.base.click(self.loginOut2)

if __name__=="__main__":
    unittest.main()
