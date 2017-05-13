#encoding=utf-8
#coding=utf-8
class Animal(object):

    def __init__(self, name):
#构造方法一个对象创建后会立即调用此方法
        self.Name = name
        print self.Name

    def accessibleMethod(self):
 #绑定方法对外公开
        print "I have a self! current name is:"
        print self.Name
        print "the secret message is:"
        self.__inaccessible()

    def __inaccessible(self):
 #私有方法对外不公开以双下划线开头
        print "U cannot see me..."

    @staticmethod
    def staticMethod():
# self.accessibleMethod() #在静态方法中无法
#直接调用实例方法直接抛出NameError异常
        print "this is a static method"
    def setName(self,name): #访问器函数
        print "setName:"
        self.Name=name

    def getName(self): #访问器函数
        print "getName:"
        return self.Name

a = Animal("learns")
print a.getName()
a.setName("sr")
print "new name:",a.getName()
a.staticMethod()
