#encoding=utf-8
from selenium import webdriver
import unittest, time, traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import win32clipboard as w
import win32api, win32con

# 用于设置剪切板内容
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

# 键盘按键映射字典
VK_CODE = {'ctrl':0x11, 'v':0x56}

# 键盘键按下
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)
# 键盘键抬起
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)

class TestDemo(unittest.TestCase):

    def setUp(self):
        # 启动Firefox浏览器
        self.driver = webdriver.Firefox(executable_path="c:\\geckodriver")

    def test_SohuMailSendEMail(self):
        url = "http://mail.sohu.com"
        # 访问搜狐邮箱登录页
        self.driver.get(url)
        try:
            userName = self.driver.find_element_by_xpath\
                ('//input[@placeholder="请输入您的邮箱"]')
            userName.clear()
            userName.send_keys("17710497931")
            passWord = self.driver.find_element_by_xpath\
                ('//input[@placeholder="请输入您的密码"]')
            passWord.clear()
            passWord.send_keys("880403souhu")
            login = self.driver.find_element_by_xpath('//input[@value="登 录"]')
            login.click()
            wait = WebDriverWait(self.driver, 10)
            # 显示等待，确定页面是否成功登录并跳转到登录成功后的首页
            wait.until(EC.element_to_be_clickable\
                           ((By.XPATH, '//li[text()="写邮件"]')))
            self.driver.find_element_by_xpath('//li[text()="写邮件"]').click()
            time.sleep(2)
            receiver = self.driver.find_element_by_xpath\
                ('//div[@arr="mail.to_render"]//input')
            # 输入收件人
            receiver.send_keys("xxxx")
            subject = self.driver.find_element_by_xpath\
                ('//input[@ng-model="mail.subject"]')
            # 输入邮件标题
            subject.send_keys(u"一封测试邮件！")
            # 输入完邮件标题后，按下Tab键可以将页面焦点切换到富文本框编辑区域
            subject.send_keys(Keys.TAB)
            # 设置剪切板内容，也就是将要输入的正文内容
            setText(u"邮件正文内容")
            # 模拟键盘的Ctrl + v组合键，将剪切板内容粘贴到富文本编辑区中
            keyDown("ctrl")
            keyDown("v")
            keyUp("v")
            keyUp("ctrl")
            # 找到页面上的“发送”按钮，并单击它
            self.driver.find_element_by_xpath('//span[.="发送"]').click()
            # 显示都等待含有关键字串“发送成功”的页面元素出现在页面中
            wait.until(EC.visibility_of_element_located\
                           ((By.XPATH, '//span[.="发送成功"]')))
            print u"邮件发送成功"
        except TimeoutException:
            print u"显示等待页面元素超时"
        except NoSuchElementException:
            print u"寻找的页面元素不存在", traceback.print_exc()
        except Exception:
            # 打印其他异常堆栈信息
            print traceback.print_exc()

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
