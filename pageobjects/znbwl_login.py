from appium.webdriver.common.mobileby import By
import time
import unittest
from framework.base import BasePage
class ZnbwlLogin(BasePage):
    start_search_loc = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon')
    register_search_loc = (By.ID, 'com.pdswp.su.smartcalendar:id/email')
    # login_search_loc = (By.ID, "com.pdswp.su.smartcalendar:id/login")
    logout_search_loc = (By.ID, "com.pdswp.su.smartcalendar:id/exit")
    znbwl_text_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")
    email_text_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/email")
    password_text_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/password")
    login_button_search_loc=(By.NAME,"登录")
    def login_success(self,email,pwd):
        time.sleep(8)
        self.click(*self.start_search_loc)
        self.click(*self.register_search_loc)
        self.sendkeys(email,*self.email_text_search_loc)
        self.sendkeys(pwd,*self.password_text_search_loc)
        self.click(*self.login_button_search_loc)
        time.sleep(3)
        self.click(*self.start_search_loc)
        container = self.get_text(self.find_element(*self.register_search_loc))
        unittest.TestCase().assertIn(email, container, msg="%s在%s中,登录成功" % (email, container))
        print("登录成功")
    def logout(self):
        time.sleep(3)
        self.click(*self.start_search_loc)
        # self.click(*self.register_search_loc)
        self.click(*self.logout_search_loc)
    def login_fail(self,email,pwd):
        time.sleep(2)
        self.click(*self.start_search_loc)
        self.click(*self.register_search_loc)
        self.sendkeys(email,*self.email_text_search_loc)
        self.sendkeys(pwd,*self.password_text_search_loc)
        self.click(*self.login_button_search_loc)
        print("登录失败")
        # content="智能备忘录"
        # container = self.get_text(self.find_element(*self.znbwl_text_search_loc))
        # unittest.TestCase().assertNotIn(content, container, msg="登录失败")
