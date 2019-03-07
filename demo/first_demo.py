import os
from appium import webdriver

apk_path=os.path.dirname(os.path.abspath('.'))
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.2.7.0'
desired_caps['deviceName']='127.0.0.1:62001'
desired_caps['sessionOverride']=True

desired_caps['app']=apk_path+"/app/todolist.apk"
#如果存在不在重新安装
desired_caps['noReset']=True

desired_caps['appPackage']="com.example.todolist"
desired_caps['appActivity']="com.example.todolist.LoginActivity"

driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)       #启动app

driver.find_element_by_id("com.example.todolist:id/nameET").send_keys("1")
driver.find_element_by_id("com.example.todolist:id/passwordET").send_keys("1")
driver.find_element_by_id("com.example.todolist:id/loginBtn").click()   #登录
driver.find_element_by_id("com.example.todolist:id/action_new").click()    #添加待办事物
driver.find_element_by_id("com.example.todolist:id/toDoItemDetailET").send_keys("happy")
driver.find_element_by_id("com.example.todolist:id/saveBtn").click()      #点击保存按钮
driver.quit()