# encoding=utf-8
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

#多窗口，通过title找到想要的网页

class VisitSogouByIE(unittest.TestCase):
    def setUp(self):
        # 启动IE浏览器
        # self.driver = webdriver.Firefox(executable_path = "e:\\geckodriver")
        self.driver = webdriver.Ie(executable_path="c:\\IEDriverServer")

    def test_identifyPopUpWindowByTitle(self):
        # 导入多个异常类型
        from selenium.common.exceptions import NoSuchWindowException, \
            TimeoutException
        # 导入期望场景类
        from selenium.webdriver.support import expected_conditions as EC
        # 导入By类
        from selenium.webdriver.common.by import By
        # 导入WebDriverWait类
        from selenium.webdriver.support.ui import WebDriverWait
        # 导入堆栈类
        import traceback
        # 导入时间模块
        import time
        url = "http://127.0.0.1:8080/web/test_popup_window.html"
        # 访问自动以测试网页
        self.driver.get(url)
        # 显示等待找到页面上链接文字为“sogou 搜索”的链接元素，找到后点击它
        WebDriverWait(self.driver, 10, 0.2).until(EC.element_to_be_clickable \
                                                      ((By.LINK_TEXT, 'sogou 搜索'))).click()
        # 获取当前所有打开的浏览器窗口句柄
        all_handles = self.driver.window_handles
        # 打印当前浏览器窗口句柄
        print self.driver.current_window_handle
        # 打印打开的浏览器窗口的个数
        print len(all_handles)
        # 等待2秒，以便更好查看效果
        time.sleep(2)
        # 如果存储浏览器窗口句柄的容器不对空，再遍历all_handles中所有的浏览器句柄
        if len(all_handles) > 0:
            try:
                for windowHandle in all_handles:
                    # 切换窗口
                    self.driver.switch_to.window(windowHandle)
                    print self.driver.title
                    # 判断当前浏览器窗口的title属性是否等于
                    # “搜狗搜索引擎 - 上网从搜狗开始”
                    if self.driver.title == u"搜狗搜索引擎 - 上网从搜狗开始":
                    #if u"搜狗" in self.driver.page_source:
                        # 显示等待页面搜索输入框加载完成，
                        # 然后输入“sogou 首页的浏览器窗口被找到”
                        WebDriverWait(self.driver, 10, 0.2).until \
                            (lambda x: x.find_element_by_id("query")). \
                            send_keys(u"sogou 首页的浏览器窗口被找到")
                        time.sleep(2)
            except NoSuchWindowException, e:
                # 捕获NoSuchWindowException异常
                print traceback.print_exc()
            except TimeoutException, e:
                # 捕获TimeoutException异常
                print traceback.print_exc()
        # 将浏览器窗口切换回默认窗口
        self.driver.switch_to.window(all_handles[0])
        print self.driver.title
        # 断言当前浏览器窗口的title属性是“你喜欢的水果”
        self.assertEqual(self.driver.title, u"你喜欢的水果")

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
