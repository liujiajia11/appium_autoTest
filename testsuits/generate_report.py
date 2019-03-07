import unittest
import os
import HTMLTestRunner
from testsuits.test_znbwl_login import ZnbwlLog
from testsuits.test_znbwl_modify_username import ZnbwlModifyUsername
from testsuits.test_znbwl_add_menu import Znbwladdmenu
from testsuits.test_znbwl_menu import Znbwlmenu
from testsuits.test_znbwl_register import ZnbwlRegis

#设置报告的保存路径
current_path=os.path.dirname(os.path.abspath("."))
report_path=os.path.join(current_path,"report")
if not os.path.exists(report_path) : os.mkdir(report_path)
#构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(ZnbwlRegis))
suite.addTest(unittest.makeSuite(ZnbwlLog))
suite.addTest(unittest.makeSuite(Znbwladdmenu))
suite.addTest(unittest.makeSuite(Znbwlmenu))
suite.addTest(unittest.makeSuite(ZnbwlModifyUsername))

if __name__=="__main__":
    # 打开一个文件，将 result 写入此 file 中
    html_report = report_path + r"\result1.html"
    fp = open(html_report, "wb")
    # 初始化一个 HTMLTestRunner 实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2,title="appium测试报告", description="用例执行情况")
    runner.run(suite)
