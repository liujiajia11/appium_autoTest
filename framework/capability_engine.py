from appium import webdriver
import yaml
import os
class CapablitityEngine():
    def appium_desired(self):
        apk_path = os.path.dirname(os.path.abspath("."))
        with open(apk_path+"/config/config.yaml",'r',encoding='utf-8') as file:
            data = yaml.load(file)
        desired_caps={}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['sessionOverride'] = True
        desired_caps['app'] = apk_path+"/app/znbwl.apk"
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote('http://'+ str(data['ip']) +':'+ str(data['port']) + 	'/wd/hub', desired_caps)
        return self.driver

if __name__ == '__main__':
    CapablitityEngine().appium_desired()

