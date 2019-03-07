from pageobjects.znbwl_menu import ZnbwlMenu
from testsuits.base_testcase import BaseTestCase
import unittest
class Znbwlmenu(BaseTestCase):
    def test_znbwl_memo(self):
        zdf=ZnbwlMenu(self.driver)
        zdf.sort()
        zdf.do_filing()
        zdf.look_do_filing_menu()
        zdf.resume_archving()
        zdf.delete_menu()
        zdf.look_delete_menu()
        zdf.empty_recycle_bin()

if __name__=="__mian__":
    unittest.main()