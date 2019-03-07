from testsuits.base_testcase import BaseTestCase
from pageobjects.znbwl_login import ZnbwlLogin
from framework.unit import Unit
import os
import unittest
dir_path=os.path.dirname(os.path.abspath("."))
data_path=dir_path+"/data/info.xlsx"
sheetName="Sheet1"
class ZnbwlLog(BaseTestCase):
    def test_znbwl_login(self):
        u=Unit()
        info=u.readdata(data_path,sheetName)
        data=info[0]
        email1=data['email']
        pwd1=data['pwd']
        data = info[1]
        email = data['email']
        pwd = data['pwd']
        zl=ZnbwlLogin(self.driver)
        zl.login_success(email,pwd)
        zl.logout()
        zl.login_fail(email1,pwd1)

if __name__=="__main__":
    unittest.main()
