#encoding=utf-8
from selenium import webdriver
import unittest
import time, traceback
from ObjectMap import ObjectMap

class TestSoGouByObjectMap(unittest.TestCase):

    def setUp(self):
        self.obj = ObjectMap()
        # 启动Firefox浏览器
        self.driver = webdriver.Ie(executable_path = "c:\\IEDriverServer")

    def testSoGouSearch(self):
        url = "http://www.sogou.com"
        # 访问搜狗首页
        self.driver.get(url)
        try:
            # 查找页面搜索输入框
            searchBox = self.obj.getElementObject\
                (self.driver, "sogou", "searchBox")
            # 在找到的搜索输入框中输入“WebDriver实战宝典”
            searchBox.send_keys(u"WebDriver实战宝典")
            # 查找搜索按钮
            searchButton = self.obj.getElementObject\
                (self.driver, "sogou", "searchButton")
            # 点击找到的搜索按钮
            searchButton.click()
            # 等待2秒，以便页面加载完成
            time.sleep(2)
            # 断言关键字“吴晓华”是否按预期出现在页面源代码中
            self.assertTrue(u"吴晓华" in self.driver.page_source, "assert error!")
        except Exception, e:
            # 打印异常堆栈信息
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
