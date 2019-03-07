from testsuits.base_testcase import BaseTestCase
from pageobjects.znbwl_add_menu import ZnbwlAddMenu
import unittest
class Znbwladdmenu(BaseTestCase):
    def test_znbwl_add_menu(self):
        zam=ZnbwlAddMenu(self.driver)
        zam.first_add_menu("today is Thursday")
        zam.second_add_menu("a fine day")
        zam.search("a")
if __name__=="__main__":
    unittest.main()