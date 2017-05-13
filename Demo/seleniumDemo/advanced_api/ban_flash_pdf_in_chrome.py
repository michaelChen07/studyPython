#encoding=utf-8
from selenium import webdriver
# 导入Options类
from selenium.webdriver.chrome.options import Options
import unittest, time

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 创建Chrome浏览器的一个Options实例对象
        chrome_options = Options()
        # 设置Chrome浏览器禁用PDF和Flash插件,把图片也关掉了。
        profile = {"plugins.plugins_disabled": ['Chrome PDF Viewer'],
                   "plugins.plugins_disabled": ['Adobe Flash Player'],
				   "profile.managed_default_content_settings.images":2}


        chrome_options.add_experimental_option("prefs", profile)
        prefs = {"profile.managed_default_content_settings.images":2}
        chrome_options.add_experimental_option("prefs", profile)
        # 向Options实例中添加禁用扩展插件的设置参数项
        chrome_options.add_argument("--disable-extensions")
        # 添加屏蔽--ignore-certificate-errors提示信息的设置参数项
        chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        # 添加浏览器最大化的设置参数项，启动同时最大化窗口
        chrome_options.add_argument('--start-maximized')
        # 启动带有自定义设置的Chrome浏览器
        self.driver = webdriver.Chrome(executable_path="c:\\chromedriver", chrome_options=chrome_options)

    def test_forbidPdfFlashChrome(self):
        # 访问爱奇艺首页
        self.driver.get("http://www.iqiyi.com")
        # 等待50秒，期间可以看到页面由于禁用了Flash插件，
        # 导致需要Flash支持的内容无法正常展示
        time.sleep(10)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
