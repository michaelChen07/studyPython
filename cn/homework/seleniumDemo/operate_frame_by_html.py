# encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

#多个frame

class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="e:\\IEDriverServer")

    def test_HandleFrameByPageSource(self):
        url = "http://127.0.0.1/frameset.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 找到页面上所有的frame页面对象，并存储到名为framesList列表中
        framesList = self.driver.find_elements_by_tag_name("frame")
        # 通过for循环遍历framesList中所有的frame页面，查找页面源码中含有
        # “中间 frame”的frame页面
        for frame in framesList:
            # 进入与frame页面
            self.driver.switch_to.frame(frame)
            # 判断每个frame的HTML源码中是否包含“中间 frame”几个关键词
            if u"中间 frame" in self.driver.page_source:
                # 如果包含需要查找的关键字，则查找到页面上的p标签元素
                p = self.driver.find_element_by_xpath("//p")
                # 断言页面上p元素文本内容是否是“这是中间 frame 页面上的文字”
                self.assertAlmostEqual(u"这是中间 frame 页面上的文字", p.text)
                # 退出frame
                self.driver.switch_to.default_content()
                # 找到指定的frame页面，并作相应的操作后退出循环
                break
            else:
                # 若果没找到指定的frame，则调用此行代码，返回到frameset页面中
                # 以便下次for循环中能继续调用driver.switch_to.frame方法,否则会报错
                self.driver.switch_to.default_content()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
