#encoding=utf-8
from selenium import webdriver
import time

#常见操作

#打开一个IE窗口
driver = webdriver.Ie(executable_path="C:\\IEDriverServer")
driver.get("http://www.baidu.com")
#driver.get("http://www.sogou.com")#访问搜狗

time.sleep(5)

search_input_box = driver.find_element_by_id("kw")#定位百度的输入框，通过id定位
#search_input_box = driver.find_element_by_id("query")#定位搜狗的输入框
print type(search_input_box)

driver.maximize_window()#全屏，最大化
driver.get_window_size()#获取窗体的大小
driver.get_window_size()["width"]#获取窗体的宽度
driver.set_window_size(900,800)#设置窗体大小

driver.get_window_position()#获取窗体当前位置
driver.get_window_position(302,3224)#设置窗体位置

search_input_box.send_keys(u"光荣之路")#在搜索框输入光荣之路
submit_button = driver.find_element_by_id("stb")#定位搜索按钮
submit_button.click()#点击搜索按钮

first_link = driver.find_element_by_xpath("//a")#通过firepath定位
len(driver.find_elements_by_xpath("//a"))

driver.find_element_by_tag_name("a")#根据标签名定位，找第一个
driver.find_elements_by_tag_name("a")#根据标签名定位，找全部

driver.get("http://www.sogou.com")#访问搜狗
driver.find_element_by_name("q")#通过属性定位
driver.find_element_by_link_text(u"图片")#通过链接文本定位
driver.find_element_by_link_text(u"图片").click()#点击

driver.find_element_by_partial_link_text(u"图片").click()#可进行模糊匹配
len(driver.find_elements_by_partial_link_text())#匹配到的对象放入列表，列表的长度，可统计匹配到的对象个数

driver.set_page_load_timeout(5)#可设定页面加载等待时间，如果没有加载完毕，可能会抛出异常

#捕获异常
from selenium.common.exceptions import TimeoutException
try:
    driver.get("http://sports.sohu.com/nba.shtml")
except TimeoutException,e:
    print u"页面没有完全加载完"

#获取页面的源码
print driver.page_source.unicod.encode("gbk","ignore")
print driver.page_source[:10000].unicod.encode("gbk","ignore")#可用切片获取前10000行

#判断某个字段是否在页面
assert u"消息" in driver.page_source


#根据条件，查找页面元素
driver.find_element("id","kw")
driver.find_element("xpath","//input[@id='kw']")
driver.find_elements("xpath","//a")

driver.get("http://www.sogou.com")
class Object_map(object):
    def __init__(self,config_file):
        self.config_file = config_file
    def find_object(self,element_name):
        with open(self.config_file) as fp:
            content = fp.readlines()
        for i in content:
            if element_name in i:
                element = driver.find_element(i.split(":")[1].split(",")[0].strip().str(i.split(":")[1].split(",")[1]).strip())
                return element
om = Object_map("e:\\config.txt")
om.find_object("searchbox").send_keys(u"光荣之路自动化测试")
om.find_object("submitbutton").click()
time.sleep(5)
assert u"吴老" in driver.page_source

driver.quit()

driver.find_element_by_css_selector("#query")#用css方式定位元素，不推荐


driver.back()#返回
driver.forward()#返回上一页面

print driver.title#获取浏览器的title
driver.desired_capabilities#获取浏览器的默认设置
driver.window_handles#当前窗口对应的值，切换窗口时可能会用到
driver.name#获取当前浏览器的名字
driver.port#获取当前浏览器的端口
driver.current_url#获取当前访问的网址
driver.get_screenshot_as_file("e:\\1.png")#截图

driver.execute_script("alert('hello');")#在窗口弹alert，内容是hello，JS方法
driver.execute_script("document.write('<h1>hello<h1>');")#将窗口内容改写成hello

driver.get("http://www.sogou.com")
driver.execute_script("document.getElementById('query').value='hello';")
driver.execute_script("document.getElementById('stb').click();")
print driver.execute_script("return document.getElementById('query').value;")#可以获取页面输入值

#driver.close()#关闭当前网页
driver.quit()#退出当前浏览器进程，可关闭多个网页，退的比较干净