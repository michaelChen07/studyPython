#encoding=utf-8
from selenium import webdriver
import unittest
import time
# 从当前文件呢所在目录下导入Table.py文件中的Table类
from Table import Table

class TestSoGouByObjectMap(unittest.TestCase):

    def setUp(self):
        # 启动IE浏览器
        self.driver = webdriver.Ie(executable_path = "c:\\IEDriverServer")

    def testSoGouSearch(self):
        url = "http://127.0.0.1:8080/web/test_table.html"
        # 访问自定义的网页
        self.driver.get(url)
        # 获取被测试页面中的表格元素，并存储在webTable变量中
        webTable = self.driver.find_element_by_tag_name("table")
        # 使用webTable变量对Table类进行实例化
        table = Table(webTable)
        # 统计表格的行数
        print table.getRowCount()
        # 统计表格的列数
        print table.getColumnCount()
        # 获取表格中第二行第三列单元格对象
        cell = table.getCell(2, 3)
        # 断言获取的单元格文本内容是否是“第二行第三列”
        self.assertAlmostEqual(u"第二行第三列", cell.text)
        # 获取表格中第三行第二列单元格中的输入框对象
        cellInput = table.getWebElementInCell(3, 2, "tag name", "input")
        # 在找到的输入框中输入“第三行的第二列表格被找到”关键字内容
        cellInput.send_keys(u"第三行的第二列表格被找到")
        # 等待3秒，肉眼查看输入效果
        time.sleep(3)

    def tearDown(self):
        # 退出IE浏览器
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
