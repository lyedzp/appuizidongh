#coding=utf-8
import time
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
# 指定测试用例为当前文件夹下的interface目录
test_dir = './case'
testsuit = defaultTestLoader.discover(test_dir,pattern='test*')
if __name__=='__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name='./report/'+now+'result.html'
    fp = open(report_name,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='appui自动化测试',
                            description='运行环境')
    runner.run(testsuit)
    fp.close()