from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import os
import time
from framework.logger import Logger

logger=Logger(logger="BasePage").getlog()   #logger实例化对象
class BasePage():
    def __init__(self,driver):
        self.driver=driver
    def click(self, *loc):
        """点击"""
        el = self.driver.find_element(*loc)
        try:
            el.click()
            logger.info("The element was click ")
        except Exception as e:
            logger.error("Failed to clickelement with %s" % e)
    def clear(self,*loc):
        """清除"""
        el=self.driver.find_element(*loc)
        try:
            el.clear()
            # logger.info("Clear text in input box before typing")
            logger.info("清除文本框里的默认内容")
        except Exception as e:
            logger.error("Failed to clear text in input box with %s" %e)
            self.get_windows_img()
    def find_element(self,*loc):
        """查找元素"""
        try:
           self.driver.find_element(*loc)
           # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
           logger.info("找到页面元素%s", loc)
           return self.driver.find_element(*loc)        #当页面在加载的时候定位元素
           # return ljj
        except:
            logger.error("%s 页面中找不到 %s元素" %(self,loc))
    def get_text(self,content):
        """得到该元素的文本内容"""
        try:
            con = content.text
            logger.info("取得的内容:%s",content)
            return con
        except Exception as e:
            logger.error("Failed to get element with %s" % e)
            self.get_windows_img()
    def get_windows_img(self):
        """屏幕截图"""
        file_path=os.path.dirname(os.path.abspath('.'))+"/screenshots/"
        nq=time.strftime("%y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+nq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("take screenshot and save to floder")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshot! %s"% e)
    def long_press(self,*loc):
        """长按"""
        el = self.driver.find_element(*loc)
        try:
            TouchAction(self.driver).long_press(el).wait(2000).perform()  # 长按
            logger.info("长按成功")
        except Exception as e:
            logger.error("长按失败")
            self.get_windows_img()
    def huiche(self):
        """按回车键"""
        try:
            self.driver.keyevent(66)
            logger.info("按回车键成功")
        except Exception as e:
            logger.error("按回车键失败")
            self.get_windows_img()
    def resetApp(self):
        """重启app"""
        try:
            self.driver.resetApp()
            logger.info("重启APP成功")
        except Exception as e:
            logger.error("重启APP失败")
            self.get_windows_img()
    def slide(self,x1,y1,x2,y2,t):
        """滑动"""
        try:
            TouchAction(self.driver).press(x1, y1).move_to(x2, y2).wait(t).release().perform()
            logger.info("滑动成功")
        except Exception as e:
            logger.error("滑动失败")
            self.get_windows_img()

        # x = self.driver.get_window_size()['width']
        # y = self.driver.get_window_size()['height']
        # self.driver.swipe(0.5 * x, 0.8 * y, 0.5 * x, 0.3 * y, 1000)
    def sendkeys(self,text,*loc):
        el=self.driver.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容:%s",text)
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    def swipLeft(self,x1,y1,x2,y2,t):
        """向左滑动"""
        try:
            self.driver.swipe(x1, y1, x2, y2, t)
            logger.info("向左滑动成功")
        except Exception as e:
            logger.error("向左滑动失败")
            self.get_windows_img()



