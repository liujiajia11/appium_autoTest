import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

apk_path=os.path.dirname(os.path.abspath("."))
desired_caps={}
desired_caps['platformName']="Android"       #运行的系统
desired_caps['platformVersion']="6.2.7.0"
desired_caps['deviceName']="127.0.0.1:62001"
desired_caps['sessionOverride']=True       #每次运行新建session

desired_caps['app']=apk_path+"/app/todolist.apk"
desired_caps['noreSet']=True
desired_caps['appPackage']="com.example.todolist"
desired_caps['appActivity']="com.example.todolist.LoginActivity"

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.find_element_by_id("com.example.todolist:id/nameET").send_keys("1")
driver.find_element_by_id("com.example.todolist:id/passwordET").send_keys("1")
driver.find_element_by_id("com.example.todolist:id/loginBtn").click()  #登录
driver.find_element_by_id("com.example.todolist:id/action_new").click()
driver.find_element_by_id("com.example.todolist:id/toDoItemDetailET").send_keys("happy")
driver.find_element_by_id("com.example.todolist:id/saveBtn").click()    #保存

element=driver.find_element_by_id("com.example.todolist:id/toDoItemDetailTv")     #找到要删除的元素
TouchAction(driver).long_press(element).wait(2000).perform()      #长按
driver.find_element_by_name("删除").click()      # 删除按钮
driver.find_element_by_id("android:id/button1").click()      #确认删除

driver.quit()


