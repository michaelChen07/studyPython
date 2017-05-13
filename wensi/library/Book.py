# encoding=utf-8

# 书籍
# 类： 属性, 方法
# 数据类
class Book:
    name = "" # 书名（属性）
    author = "" # 作家（属性）

    def __init__(self, name, author): # 构造函数（方法）： 创建一个对象（实例）
        self.name = name
        self.author = author