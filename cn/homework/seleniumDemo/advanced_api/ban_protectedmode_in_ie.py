#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest, time

class TestDemo(unittest.TestCase):

    def setUp(self):
        caps = DesiredCapabilities.INTERNETEXPLORER
        # 将忽略IE保护模式的参数设置为True
        caps['ignoreProtectedModeSettings'] = True
        # 启动带有自定义设置的IE浏览器
        self.driver = webdriver.Ie(executable_path="c:\\IEDriverServer", capabilities=caps)

    def test_forbidPdfFlashChrome(self):
        # 访问百度首页
        self.driver.get("http://www.baidu.com")
        time.sleep(2)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
