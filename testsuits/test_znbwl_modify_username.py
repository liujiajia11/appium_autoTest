from testsuits.base_testcase import BaseTestCase
from framework.base import BasePage
from pageobjects.znbwl_login import ZnbwlLogin
from pageobjects.znbwl_modify_username import ZnbwlModifyUser
import unittest
class ZnbwlModifyUsername(BaseTestCase):
    def test_znbwl_modify_username(self):
        zmu=ZnbwlModifyUser(self.driver)
        zmu.login("57464369@qq.com","1111111")
        zmu.modify_username("happy")
if __name__=="__main__":
    unittest.main()
