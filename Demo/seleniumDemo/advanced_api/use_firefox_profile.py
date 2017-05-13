#encoding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest, time

#设置浏览器配置文件

class TestFailCaptureScreen(unittest.TestCase):

    def setUp(self):
        # 创建存储自定义配置文件的路径变量
        #proPath = "C:\\Users\\wuxiaohua\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\tbbmxtkv.webdriver"
        proPath = "C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\sbzden4j.default"
        # 加载自定义配置文件到FirefoxProfile实例中，
        # 等价profile = webdriver.FirefoxProfile(proPath)
        profile = webdriver.firefox.firefox_profile.FirefoxProfile(proPath)
        # 将添加了新配置文件的Firefox浏览器首页设为搜狗主页
        profile.set_preference("browser.startup.homepage", "http://www.sogou.com")
        # 设置开始页面不是空白页，0表示空白页，
        # 这一步必须做，否则设置的主页不会生效
        profile.set_preference("browser.startup.page", 1)
        # 启动带自定义配置文件的Firefox浏览器
        self.driver = webdriver.Firefox(executable_path="c:\\geckodriver", firefox_profile=profile)

    def testSoGouSearch(self):
        # 等待5秒，以便浏览器启动完成
        time.sleep(5)
        try:
            # 找到搜狗主页搜索输入框页面元素
            searchBox = self.driver.find_element_by_id("query")
            # 在找到的搜索输入框中输入“光荣之路自动化测试”
            searchBox.send_keys(u"光荣之路自动化测试")
            # 找到搜索按钮，并点击
            self.driver.find_element_by_id("stb").click()
            time.sleep(10)
        except NoSuchElementException, e:
            print "修改带自定义配置文件的浏览器主页不成功！"

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
