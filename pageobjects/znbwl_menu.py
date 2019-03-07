from framework.base import BasePage
from appium.webdriver.common.mobileby import By
import time
import unittest
class ZnbwlMenu(BasePage):
    start_search_loc = (By.ID, 'com.pdswp.su.smartcalendar:id/ab_icon')
    page_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/notelistview")
    menu_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/note_title")            #找备忘录
    sort_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu_sort")              #排序
    duigou_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_ok")
    do_filing_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu_archive")     #归档备忘录
    # do_filing_search_loc=(By.CLASS_NAME,"android.widget.LinearLayout")
    look_do_filinf_menu_search_loc = (By.NAME, "归档")          # 归档
    resume_archiving_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu")     #恢复归档
    delete_menu_button_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/menu_delete")  #删除备忘录
    recycle_bin_search_loc=(By.NAME,"回收站")                                        #回收站
    look_delete_menu_search_loc=(By.CLASS_NAME,"android.widget.LinearLayout")     #查看删除的备忘录
    empty_recycle_bin_search_loc=(By.ID,"com.pdswp.su.smartcalendar:id/button")  #清空回收站
    sure_button_serch_loc=(By.NAME,"确定")
    def sort(self):
        """排序"""
        # self.resetApp()
        time.sleep(3)
        self.long_press(*self.menu_search_loc)
        self.click(*self.sort_search_loc)
        self.click(*self.duigou_search_loc)
        print("排序成功")
    def do_filing(self):
        """归档备忘录"""
        time.sleep(3)
        self.long_press(*self.menu_search_loc)
        self.click(*self.do_filing_search_loc)
        ele = self.get_text(self.find_element(*self.menu_search_loc))
        container=self.get_text(self.find_element(*self.page_search_loc))
        unittest.TestCase().assertNotIn(ele, container, msg="归档成功")
        print("归档成功")
    def look_do_filing_menu(self):
        """查看归档备忘录"""
        self.click(*self.start_search_loc)
        self.click(*self.look_do_filinf_menu_search_loc)
        time.sleep(3)
        print("查看归档")
    def resume_archving(self):
        """恢复归档"""
        self.click(*self.start_search_loc)
        time.sleep(3)
        self.click(*self.start_search_loc)
        time.sleep(3)
        self.click(*self.look_do_filinf_menu_search_loc)
        time.sleep(2)
        self.swipLeft(700,200,350,200,1000)
        time.sleep(3)
        self.click(*self.resume_archiving_search_loc)
        # self.slide()
        # ele = self.get_text(self.find_element(*self.menu_search_loc))
        # container = self.get_text(self.find_element(*self.page_search_loc))
        # unittest.TestCase().assertIn(ele, container, msg="恢复归档成功")
        print("恢复归档")
    def delete_menu(self):
        """删除备忘录"""
        self.click(*self.start_search_loc)
        self.long_press(*self.menu_search_loc)
        # TouchAction(self.driver).long_press(*self.menu_search_loc).wait(2000).perform()  # 长按
        self.click(*self.delete_menu_button_search_loc)
        ele = self.get_text(self.find_element(*self.menu_search_loc))
        container = self.get_text(self.find_element(*self.page_search_loc))
        unittest.TestCase().assertNotIn(ele, container, msg="删除成功")
        print("删除成功")
    def look_delete_menu(self):
        """查看删除的备忘录"""
        self.click(*self.start_search_loc)
        time.sleep(3)
        self.click(*self.recycle_bin_search_loc)
        time.sleep(3)
        print("点击回收站")
        # self.click(*self.look_delete_menu_search_loc)
        # print("查看删除备忘录")
    def empty_recycle_bin(self):
        """清空回收站"""
        self.click(*self.empty_recycle_bin_search_loc)
        time.sleep(3)
        self.click(*self.sure_button_serch_loc)
        print("清空回收站成功")
