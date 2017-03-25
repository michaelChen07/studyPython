#encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains


class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        #self.driver = webdriver.Firefox(executable_path="d:\\geckodriver")
         self.driver = webdriver.Ie(executable_path = "c:\\IEDriverServer")

    def test_HandleFrame(self):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.common.exceptions import TimeoutException
        url = "http://www.126.com/"
        # 访问自动以测试网页
        self.driver.get(url)
        # 使用索引方式进入指定的frame页面，索引号从0开始。
        # 所以想进入中间的frame，需要使用索引号1
        # 如果没有使用此行代码，则无法找到页面中左侧frame中的任何页面元素
        self.driver.switch_to.frame(self.driver.find_element_by_id("x-URS-iframe"))
        #self.driver.switch_to.frame("x-URS-iframe")

        #输入账号
        input = self.driver.find_element_by_xpath("//input[@name='email']")
        input.clear()#清空账号输入框的内容
        input.send_keys('wqcz2508')

        #输入密码
        pwd = self.driver.find_element_by_xpath("//input[@name='password']")
        pwd.send_keys('880403cz')

        #点击登录按钮
        button = self.driver.find_element_by_id('dologin')
        button.click()

        time.sleep(10)
        assert u'网易' in self.driver.title
        print self.driver.title
        print self.driver.current_url,
        self.driver.switch_to.default_content()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
