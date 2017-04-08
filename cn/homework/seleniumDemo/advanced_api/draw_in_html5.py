#encoding=utf-8
import unittest
from selenium import webdriver
import time

class TestDemo(unittest.TestCase):
    def setUp(self):
        # 获取浏览器驱动实例
        self.driver = webdriver.Ie(executable_path = "c:\\IEDriverServer")

    def test_HTML5Canvas(self):
        url = "http://www.w3school.com.cn/tiy/loadtext.asp?f=html5_canvas_line"
        # 访问指定的网址
        self.driver.get(url)
        # 调用JavaScript语句，在页面画布上画一个红色的图案
        # getElementById('myCanvas'); 语句获取页面上的画布元素
        # var cxt = c.getContext('2d'); 设定画布为2d
        # cxt.fillStyle = '#FF0000'; 设定填充色为  # FF0000 红色
        # cxt.fillRect(0, 0, 150, 150); 在画布上绘制矩形
        self.driver.execute_script("var c = document.getElementById('myCanvas');"
               + "var cxt=c.getContext('2d');"
               + "cxt.fillStyle='#FF0000';"
               +"cxt.fillRect(0,0,150,150);")
        time.sleep(3)
        # 将绘制的红色矩形页面，进行截屏，并保存为E盘的HTML5Canvas.jpg
        self.driver.save_screenshot("E:\\HTML5Canvas.jpg")

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
