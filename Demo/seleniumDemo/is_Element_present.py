# encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

#判断页面某个元素在不在

class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="c:\\IEDriverServer")

    def isElementPresent(self, by, value):
        # 从selenium.common.exceptions模块导入NoSuchElementException异常类
        from selenium.common.exceptions import NoSuchElementException
        try:
            element = self.driver.find_element(by=by, value=value)
        except NoSuchElementException, e:
            # 打印异常信息
            print e
            # 发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
            return False
        else:
            # 没有发生异常，表示在页面中找到了该元素，返回True
            return True

    def test_isElementPresent(self):
        url = "http://www.sogou.com"
        # 访问sogou首页
        self.driver.get(url)
        # 判断页面元素id属性值为“query”的页面元素是否存在
        res = self.isElementPresent("id", "query")
        if res is True:
            print u"所查找的元素存在于页面上！"
        else:
            print u"页面中未找到所需要的页面元素！"


def tearDown(self):
    # 退出IE浏览器
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()
