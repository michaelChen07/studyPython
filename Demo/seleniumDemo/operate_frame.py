# encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

#切换frame

class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="c:\\IEDriverServer")

    def test_HandleFrame(self):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.common.exceptions import TimeoutException
        url = "http://127.0.0.1:8080/web/frameset.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 使用索引方式进入指定的frame页面，索引号从0开始。
        # 所以想进入中间的frame，需要使用索引号1
        # 如果没有使用此行代码，则无法找到页面中左侧frame中的任何页面元素
        self.driver.switch_to.frame(0)
        # 找到左侧frame中的p标签元素
        leftFrameText = self.driver.find_element_by_xpath("//p")
        # 断言左侧frame中的文字是否和“这是左侧 frame 页面上的文字”几个关键字相一致
        self.assertAlmostEqual(leftFrameText.text, u"这是左侧 frame 页面上的文字")
        # 找到左侧frame中的按钮元素，并点击该元素
        self.driver.find_element_by_tag_name("input").click()
        try:
            # 动态等待alert窗体出现
            alertWindow = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            # 打印alert消息
            print alertWindow.text
            alertWindow.accept()
        except TimeoutException, e:
            print e

        # 使用driver.switchTo.default_content方法，从左侧frame中返回到frameset页面
        # 如果不调用此行代码，则无法从左侧frame页面中直接进入其他frame页面
        self.driver.switch_to.default_content()

        # 通过标签名找到页面中所有的frame元素，然后通过索引进入该frame
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name("frame")[1])

        # 断言页面源码中是否存在“这是中间 frame 页面上的文字”关键子串
        assert u"这是中间 frame 页面上的文字" in self.driver.page_source

        # 再输入框中输入“我在中间frame”
        self.driver.find_element_by_tag_name("input").send_keys(u"我在中间frame")
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.driver.find_element_by_id("rightframe"))
        assert u"这是右侧 frame 页面上的文字" in self.driver.page_source
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame("rightframe")
        assert u"这是右侧 frame 页面上的文字" in self.driver.page_source
        self.driver.switch_to.default_content()


    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
