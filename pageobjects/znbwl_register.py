from framework.base import BasePage
from appium.webdriver.common.mobileby import By
import time
import unittest
class ZnbwlRegister(BasePage):
    start_search_loc=(By.ID,'com.pdswp.su.smartcalendar:id/ab_icon')
    register_search_loc=(By.ID,'com.pdswp.su.smartcalendar:id/email')
    logout_search_loc=(By.NAME,"退出当前账号")
    register_one_search_loc =(By.ID,'com.pdswp.su.smartcalendar:id/register') #点击注册一个吧
    name_test_search_loc=(By.NAME,"昵称")
    email_test_search_loc=(By.NAME,'注册邮箱(这将是您的账号)')                  #邮箱
    password_test_search_loc=(By.ID, 'com.pdswp.su.smartcalendar:id/password')  #密码
    register_button_search_loc=(By.ID,'com.pdswp.su.smartcalendar:id/reguser')    #注册按钮
    register_fail_message_search_loc=(By.ID,"android:id/message")
    def register_success(self,name,email,pwd):
         time.sleep(8)
         self.click(*self.start_search_loc)
         self.click(*self.register_search_loc)
         self.click(*self.register_one_search_loc)
         self.sendkeys(name,*self.name_test_search_loc)
         self.sendkeys(email,*self.email_test_search_loc)
         self.sendkeys(pwd,*self.password_test_search_loc)
         self.click(*self.register_button_search_loc)
         time.sleep(3)
         self.click(*self.start_search_loc)
         container=self.get_text(self.find_element(*self.register_search_loc))
         unittest.TestCase().assertIn(email,container,msg="%s在%s中,注册成功"%(email,container))
         # assert email in container
         # print("注册成功")
    def logout(self):
        time.sleep(3)
        self.click(*self.start_search_loc)
        # self.click(*self.login_search_loc)
        self.click(*self.logout_search_loc)
    def register_fail(self,name,email,pwd):
        self.click(*self.start_search_loc)
        self.click(*self.register_search_loc)
        self.click(*self.register_one_search_loc)
        self.sendkeys(name, *self.name_test_search_loc)
        self.sendkeys(email, *self.email_test_search_loc)
        self.sendkeys(pwd, *self.password_test_search_loc)
        self.click(*self.register_button_search_loc)
        # self.click(*self.start_search_loc)
        # content="注册中"
        # container = self.get_text(self.find_element(*self.register_fail_message_search_loc))
        # unittest.TestCase().assertIn(content, container, msg="注册失败")
