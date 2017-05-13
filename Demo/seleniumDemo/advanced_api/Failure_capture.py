#encoding=utf-8
from selenium import webdriver
import unittest, time, os
from FileUtil import createDir
import traceback

# 创建存放异常截图的目录，并得到本次实例中存放图片目录的绝对路径，
# 并且作为全局变量，以供本次所有测试用例调用
picDir = createDir()

def takeScreenshot(driver, savePath, picName):
    # 封装截屏方法
    # 构造屏幕截图路径及图片名
    # 因为Windows默认编码是GBK，而传入的图片名为utf8编码，
    # 所以这里需要进行转码，以便让图片名中的中文字符能正常显示
    picPath = os.path.join(savePath, str(picName).decode("utf-8").encode("gbk")\
                           + ".png")
    try:
        # 调用WebDriver提供的get_screenshot_as_file()方法，
        # 将截取的屏幕图片保存为本地文件
        driver.get_screenshot_as_file(picPath)
    except Exception, e:
        # 打印异常堆栈信息
        print traceback.print_exc()

class TestFailCaptureScreen(unittest.TestCase):

    def setUp(self):
        # 启动Firefox浏览器
        self.driver = webdriver.Ie(executable_path = "c:\\IEDriverServer")

    def testSoGouSearch(self):
        url = "http://www.sogou.com"
        # 访问搜狗首页
        self.driver.get(url)
        try:
            self.driver.find_element_by_id("query").\
                send_keys(u"光荣之路自动化测试")
            self.driver.find_element_by_id("stb").click()
            time.sleep(3)
            # 断言页面的代码中是否存在“事在人为”这4个关键字，
            # 因为页面中没有这4个字，所以会触发except语句的执行，并触发截图操作
            self.assertTrue(u"事在人为" in self.driver.page_source, \
                            "“事在人为”关键字串在页面源代码中未找到")
        except AssertionError, e:
            # 调用封装好的截图方法，进行截图并保存在本地磁盘
            takeScreenshot(self.driver, picDir, e)
        except Exception, e:
            print traceback.print_exc()
            takeScreenshot(self.driver, picDir, e)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
