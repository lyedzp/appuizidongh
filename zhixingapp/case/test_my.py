import sys
sys.path.extend(['D:\\appuizidongh\\zhixingapp'])#加入这2行是因为在命令行运行直接运行test_01时会找不到zhixingapp这个模块，把路径加上，命令行运行时就可以了
from zhixingapp.common.start import start_app
from zhixingapp.common.fengzhuangdingwei import Base
import unittest
import warnings
from zhixingapp.pages.mypage import MyPage
from zhixingapp.pages.fenxiangpage import FenXiang
from selenium import webdriver

class TestYaoQing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.driver = start_app()
        cls.driver.wait_activity("com.yipiao/com.zt.main.entrance.MainActivity", 20)
        cls.base = Base(cls.driver)
        # 判断更新弹框中“下次再说”是否存在,如果弹框存在，先点下次再说，如果不存在，直接点我的
        tan_loc = {"by": "text", "value": "下次再说", "timeout": "5"}
        if cls.base.is_element_exist(tan_loc):
            cls.base.click({"by": "text", "value": "下次再说"})
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def get_Result(self):
        result = []
        # 分享页面有微信好友，朋友圈等选项，所以用class可以获取这一组元素
        els = self.base.click(FenXiang.tanchu)
        # 循环去元组里面取每个元素的text
        for i in els:
            r = i.text
            result.append(r)
        return result

    def test_01(self):
        """我的足迹页面-分享"""
        self.base.click(MyPage.loc1)
        self.base.click(MyPage.loc11)
        self.base.click(FenXiang.loc1)
        resultR = self.get_Result()

        #期望值
        exceptresult = ["微信好友","朋友圈"]
        self.assertTrue(resultR==exceptresult)
if __name__=="__main__":
    unittest.main()
