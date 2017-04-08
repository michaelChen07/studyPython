#encoding=utf-8
from selenium import webdriver
import unittest
import logging

# 从当前文件所在目录中导入Log.py文件中所有内容
from Log import *

class TestSoGouByObjectMap(unittest.TestCase):

    def setUp(self):
        # 启动Firefox浏览器
        self.driver = webdriver.Ie(executable_path = "c:\\IEDriverServer")

    def testSoGouSearch(self):
        debug(u"============== 搜索 ==============")
        url = "http://www.sogou.com"
        # 访问搜狗首页
        self.driver.get(url)
        debug(u"访问sogou首页")
        self.driver.find_element_by_id("query").send_keys(u"光荣之路自动化测试")
        warning(u"在输入框中输入搜索关键字串“光荣之路自动化测试”"+self.driver.find_element_by_id("query").get_attribute("value"))
        self.driver.find_element_by_id("stb").click()
        info(u"点击搜索按钮")
        debug(u"========== 测试用例执行结束 ==========")

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
