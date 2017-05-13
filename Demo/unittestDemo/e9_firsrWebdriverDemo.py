#encoding=utf-8
import unittest
from selenium import webdriver
import time

class GloryRoad(unittest.TestCase):
    def setUp(self):
        # 启动Firefox浏览器
        #self.driver = webdriver.Firefox(executable_path = "c:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="c:\\IEDriverServer")

    def testSoGou(self):
        # 访问搜狗首页
        self.driver.get("http://sogou.com")
        # 清空搜索输入框默认内容
        self.driver.find_element_by_id("query").clear()
        # 在搜索输入框中输入“光荣之路自动化测试”
        self.driver.find_element_by_id("query").send_keys(u"WebDriver实战宝典")
        # 单击“搜索”按钮
        self.driver.find_element_by_id("stb").click()
        # 等待3秒
        time.sleep(3)
        assert u"吴晓华" in self.driver.page_source, u"页面中不存在要寻找的关键字！".encode("gbk")

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
