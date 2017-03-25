# encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver

#单键操作：
class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="c:\\IEDriverServer")

    def test_simulateASingleKeys(self):
        url = "http://www.sogou.com"
        # 访问搜狗首页，焦点会自动定位到搜索输入框中
        self.driver.get(url)
        # 导入模拟按键模块Keys
        from selenium.webdriver.common.keys import Keys
        import time
        # 通过id获取搜索输入框的页面元素
        query = self.driver.find_element_by_id("query")
        # 通过WebDriver实例发送一个F12键
        query.send_keys(Keys.F12)
        time.sleep(3)
        # 再次通过WebDriver实例模拟发送一个F12键
        query.send_keys(Keys.F12)
        # 在搜索输入框中输入“selenium”
        query.send_keys("selenium")
        # 通过WebDriver实例模拟发送一个回车键，
        # 或者使用query.send_keys(Keys.RETURN)
        query.send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()