import unittest
import warnings
from framework.capability_engine import CapablitityEngine
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        cap=CapablitityEngine()
        self.driver=cap.appium_desired()
        # apk_path=os.path.dirname(os.path.abspath("."))
        # config_path=os.path.dirname(os.path.abspath("."))
        # with open(config_path, 'r', encoding='utf-8') as file:
        #     data = yaml.load(file)
        # desired_caps={}
        # desired_caps['platformName']=data['platformName']
        # desired_caps['platformVersion']=data['platformVersion']
        # desired_caps['deviceName']=data['deviceName']
        # desired_caps['sessionOverride']=data['sessionOverride']
        # desired_caps['app']=apk_path+"/app/znbwl.apk"
        # desired_caps['noReset']=data['noReset']
        # # desired_caps['appPackage']=data['appPackage']     #app包名
        # # desired_caps['appActivity']=data['appActivity']
        # self.deiver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
    def tearDown(self):
        self.driver.quit()