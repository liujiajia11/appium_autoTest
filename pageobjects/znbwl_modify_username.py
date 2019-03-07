import time
import unittest
from framework.base import BasePage
from pageobjects.znbwl_login import ZnbwlLogin
from pageobjects.znbwl_register import ZnbwlRegister
from appium.webdriver.common.mobileby import By
class ZnbwlModifyUser(BasePage):
    start_search_loc = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon')
    register_search_loc = (By.ID, 'com.pdswp.su.smartcalendar:id/email')
    login_search_loc = (By.ID, "com.pdswp.su.smartcalendar:id/login")
    logout_search_loc = (By.ID, "com.pdswp.su.smartcalendar:id/exit")
    user_info_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/title")
    email_text_search_loc = (By.ID, "com.pdswp.su.smartcalendar:id/email")
    password_text_search_loc = (By.ID, "com.pdswp.su.smartcalendar:id/password")
    login_button_search_loc = (By.ID, "com.pdswp.su.smartcalendar:id/login")
    username_text_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    duigou_button_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")
    def login(self,username,pwd):
        time.sleep(8)
        self.click(*self.start_search_loc)
        self.click(*self.register_search_loc)
        self.sendkeys(username, *self.email_text_search_loc)
        self.sendkeys(pwd, *self.password_text_search_loc)
        self.click(*self.login_button_search_loc)
    def modify_username(self,username):
        self.click(*self.start_search_loc)
        self.click(*self.login_search_loc)
        self.click(*self.user_info_search_loc)
        self.sendkeys(username,*self.username_text_search_loc)
        except_value=self.get_text(self.find_element(*self.username_text_search_loc))
        unittest.TestCase().assertEqual(username,except_value,except_value)
        # except_value = self.get_text(self.find_element(*self.username_text_search_loc))
        # unittest.TestCase().assertEqual(username,except_value,except_value)
        self.click(*self.duigou_button_search_loc)
    def logout(self):
        time.sleep(3)
        self.click(*self.logout_search_loc)