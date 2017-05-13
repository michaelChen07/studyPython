#encoding=utf-8
from selenium import webdriver
import unittest, time
from selenium.webdriver.common.keys import Keys

class TestDemo(unittest.TestCase):

    def test_openFireBug(self):
        # 找到自定义配置文件路径
        profilePath = "C:\\Users\\Administrator\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\sbzden4j.default"
        # 将自定义配置文件加载到FirefoxProfile实例中
        profile = webdriver.firefox.firefox_profile.FirefoxProfile(profilePath)
        # 将添加了新配置文件的Firefox浏览器首页设为百度主页，
        # 以便启动浏览器后将直接跳转到百度首页
        profile.set_preference("browser.startup.homepage", "http://www.baidu.com")
        # 设置启动浏览器的同时主页不为空白页
        profile.set_preference("browser.startup.page", 1)
        # 自动打开firebug
        profile.set_preference("extensions.firebug.allPagesActivation", "on")
        # 启用firebug网络面板功能
        profile.set_preference("extensions.firebug.net.enableSites", True)
        # 启用firebug Cookies面板功能
        profile.set_preference("extensions.firebug.cookies.enableSites", True)
        # 启动自定义配置信息的Firefox浏览器
        driver = webdriver.Firefox(executable_path="c:\\geckodriver", firefox_profile = profile)
        # 等待浏览器启动完成
        time.sleep(3)
        # 找到百度主页中的搜索输入框页面元素
        input = driver.find_element_by_id("kw")
        # 在搜索输入框中输入“selenium”
        input.send_keys("selenium")
        # input.send_keys(Keys.F12)
        # 等待30秒，人工确认上面一系列设置是否生效
        time.sleep(30)
        driver.quit()

if __name__ == '__main__':
    unittest.main()
