from testsuits.base_testcase import BaseTestCase
from pageobjects.znbwl_register import ZnbwlRegister
import unittest
class ZnbwlRegis(BaseTestCase):
    def test_znbwl(self):
        zr=ZnbwlRegister(self.driver)
        zr.register_success("you and me","57464369@qq.com","1111111")
        zr.logout()
        zr.register_fail("you and me","1912198737@qq.com","1111111")

if __name__=="__main__":
    unittest.main()