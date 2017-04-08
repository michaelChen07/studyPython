#encoding=utf-8
import unittest
from selenium import webdriver
import time

class TestDemo(unittest.TestCase):
    def setUp(self):
        # 获取浏览器驱动实例
        #self.driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
        self.driver = webdriver.Firefox(executable_path = "c:\\geckodriver")
    def test_HTML5VideoPlayer(self):
        url = "http://www.w3school.com.cn/tiy/loadtext.asp?f=html5_video_simple"
        # 访问HTML5语言实现的播放器网页
        self.driver.get(url)
        # 打印访问网页的页面源代码，供读者学习
        #print self.driver.page_source
        # 获取页面中的video标签元素对象
        videoPlayer = self.driver.find_element_by_tag_name("video")
        # 使用JavaScript语句，通过播放器内部的
        # currentSrc 属性获取视频文件的网络存储地址
        videoSrc = self.driver.execute_script\
            ("return arguments[0].currentSrc;", videoPlayer)
        # 打印网页中视频存放地址
        print videoSrc
        # 断言视频存放地址是否符合预期
        self.assertEqual(videoSrc, "http://www.w3school.com.cn/i/movie.ogg")
        # 使用JavaScript语句，通过播放器内部的
        # duration属性获取视频文件的播放时长
        videoDuration = self.driver.execute_script\
            ("return arguments[0].duration;", videoPlayer)
        # 打印视频时长
        print videoDuration
        # 对获取到的视频时长取整，然后断言是否等于3秒
        #self.assertEqual(int(videoDuration), 3)
        # 使用JavaScript语句，通过调用播放器内部的
        # play()方法来播放影片
        self.driver.execute_script("return arguments[0].play();", videoPlayer)
        time.sleep(2)
        # 播放2秒后，使用JavaScript语句，通过调用播放器
        # 内部的pause函数来暂停播放影片
        self.driver.execute_script("return arguments[0].pause();", videoPlayer)
        # 暂停3秒，以便人工确认视频是否已被暂停
        time.sleep(3)
        # 将暂停视频播放页面进行截屏，并保存为D盘的videoPlay_pause.jpg文件
        self.driver.save_screenshot("e:\\videoPlay_pause.jpg")
        self.driver.execute_script("return arguments[0].play();", videoPlayer)
        time.sleep(3)
    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
