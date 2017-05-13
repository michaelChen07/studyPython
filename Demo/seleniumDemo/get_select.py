#encoding=utf-8
# encoding=utf-8
import unittest
import time
import chardet
from selenium import webdriver

#下拉菜单中选中一个选项

class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="C:\\IEDriverServer")

    def test_printSelectText(self):
        url = "http://127.0.0.1:8080/web/test_select.html"
        # 访问自定义的html网页
        self.driver.get(url)
        # 使用name属性找到页面上name属性为“fruit”的下拉列表元素
        select = self.driver.find_element_by_name("fruit")
        all_options = select.find_elements_by_tag_name("option")
        for option in all_options:
            print u"选项显示的文本：", option.text
            print u"选项值为：", option.get_attribute("value")
            if option.text == u"橘子":
                option.click()
                break
            time.sleep(1)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

