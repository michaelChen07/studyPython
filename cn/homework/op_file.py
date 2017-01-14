#encoding=utf-8
class Person:
    """操作文件"""
    def __init__(self, path,line):
        self.path = path
        self.line = line

    def readfile(self):
        try:
            with open(self.path,"r") as fp:
                content = fp.readlines()
                return content[self.line-1]
        except Exception,e:
            return e

file1 = Person(r"d:/test/fp1.txt",2)
print file1.readfile()


# 操作文件的类
class op_file(object):
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            self.fp = open(self.file_path, "r")
        except Exception, e:
            print e

    def get_file_line_content(self, line_number):#获取指定行
        number = 1
        for line in self.fp:
            if line_number == number:
                # print line
                return line
            number += 1

    def get_cursor_position(self):#获取游标位置
        return self.fp.tell()

    def close_file(self):#关闭文件
        self.fp.close()

f = op_file(r"d:/test/fp1.txt")
print f.get_file_line_content(2)
print f.get_cursor_position()


