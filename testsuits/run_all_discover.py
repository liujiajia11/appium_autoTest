import unittest
import os
import HTMLTestRunner

#设置报告的保存路径
current_path=os.path.dirname(os.path.abspath("."))
report_path=os.path.join(current_path,"report")
if not os.path.exists(report_path) : os.mkdir(report_path)

test_dir="./"
suite=unittest.TestLoader().discover(test_dir,pattern="test*.py")

if __name__=="__main__":
    html_report = report_path + r"\result.html"
    fp = open(html_report, "wb")
    # 初始化一个 HTMLTestRunner 实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="论坛测试报告", description="用例执行情况")
    runner.run(suite)
