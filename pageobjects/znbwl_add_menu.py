import time
import unittest
from appium.webdriver.common.mobileby import By
from framework.base import BasePage
class ZnbwlAddMenu(BasePage):
    start_search_loc = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon')
    # page_search_loc = (By.ID, "com.pdswp.su.smartcalendar:id/notelistview")
    page_search_loc=(By.CLASS_NAME,"android.widget.LinearLayout")
    add_button_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menuAdd")    #1.页面中的+
    add_input_content_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/add_input_content")  #添加备忘录的文本框
    duigou_button_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")      #对勾按钮
    add_menu_button_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text")   #2.添加备忘按钮
    search_button_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_search")      #搜索按钮
    search_text_search_oc=(By.ID,"android:id/search_src_text")        #搜索文本框
    def first_add_menu(self,content):
        time.sleep(8)
        self.click(*self.add_button_search_loc)
        self.sendkeys(content,*self.add_input_content_search_loc)
        self.click(*self.duigou_button_search_loc)
        # page=self.get_text(self.find_element(*self.page_search_loc))
        # unittest.TestCase().assertIn(content, page, msg="%s在%s中,添加成功" % (content, page))
    def second_add_menu(self,content):
        self.click(*self.start_search_loc)
        self.click(*self.add_menu_button_search_loc)
        self.sendkeys(content,*self.add_input_content_search_loc)
        self.click(*self.duigou_button_search_loc)
        time.sleep(5)
        # page = self.get_text(self.find_element(*self.page_search_loc))
        # unittest.TestCase().assertIn(content, page, msg="%s在%s中,添加成功" % (content, page))
    def search(self,content):
        self.click(*self.search_button_search_loc)
        self.sendkeys(content,*self.search_text_search_oc)
        self.huiche()
        time.sleep(3)
