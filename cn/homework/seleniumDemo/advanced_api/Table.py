#encoding=utf-8

class Table(object):
    # 定义一个私有属性__table，用于存放table对象
    __table = ''

    def __init__(self, table):
        # Table类的构造方法
        self.setTable(table)

    def setTable(self, table):
        # 对私有属性__table进行赋值操作
        self.__table = table

    def getTable(self):
        # 获取私有属性__table的值
        return self.__table

    def getRowCount(self):
        # 返回table对象中所有的行tr标签元素对象
        return len(self.__table.find_elements_by_tag_name("tr"))

    def getColumnCount(self):
        # 获取表格对象中的列数
        return len(self.__table.find_elements_by_tag_name("tr")[0].\
                   find_elements_by_tag_name("td"))

    def getCell(self, rowNo, colNo):
        # 获取表格中某行某列的单元格对象
        try:
            # 找到表格中的某一行，因为行号从 0 开始，
            # 例如要找第三行，则需要进行 3 - 1 = 2来获取第三行tr元素对象
            currentRow = self.__table.find_elements_by_tag_name("tr")[rowNo - 1]
            # 在找到的某行基础上，再找这行中的某一列，列号也从 0 开始
            currentCol = currentRow.find_elements_by_tag_name("td")[colNo - 1]
            # 返回找到的单元格对象
            return currentCol
        except Exception, e:
            raise e

    def getWebElementInCell(self, rowNo, colNo, by, value):
        # 获取表格中某行某列的单元格中某个页面元素对象，
        # by表示定位页面元素的方法，比如id，
        # value表定位表达式，比如query
        try:
            currentRow = self.__table.find_elements_by_tag_name("tr")[rowNo - 1]
            currentCol = currentRow.find_elements_by_tag_name("td")[colNo - 1]
            # 获取具体某个单元格中的某个页面元素
            element = currentCol.find_element(by = by, value = value)
            # 返回找到的页面元素对象
            return element
        except Exception, e:
            raise e
