#encoding=utf-8
from selenium import webdriver
# 导入Options类
from selenium.webdriver.chrome.options import Options
import unittest, time

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 创建Chrome浏览器的一个Options实例对象
        chrome_options = Options()
        # 向Options实例中添加禁用扩展插件的设置参数项
        chrome_options.add_argument("--disable-extensions")
        # 添加屏蔽--ignore-certificate-errors提示信息的设置参数项
        chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        # 添加浏览器最大化的设置参数项，已启动就最大化
        chrome_options.add_argument('--start-maximized')
        # 启动带有自定义设置的Chrome浏览器
        self.driver = webdriver.Chrome(executable_path="c:\\chromedriver", chrome_options=chrome_options)

    def test_extendedAttributesChrome(self):
        # 访问百度首页
        self.driver.get("http://www.baidu.com")
        # 暂停3秒，人工查看上面设置是否已生效
        time.sleep(3)
        # 找到页面的搜索输入框，输入“光荣之路自动化测试”
        self.driver.find_element_by_id("kw").send_keys(u"光荣之路自动化测试")
        time.sleep(2)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
