#coding=utf-8
class Parent(object): # define parent class
  parentAttr = 100
  def __init__(self):
    "父类构造方法，用于初始化工作"
    print "Calling parent constructor"

  def parentMethod(self):
    print 'Calling parent method'

  def setAttr(self, attr):
    Parent.parentAttr = attr

  def getAttr(self):
    print "Parent attribute :", Parent.parentAttr

class Child1(Parent): # define child1 class
  def __init__(self):
    "子类构造方法，用于初始化子类本身数据的工作"
    print "Calling child1 constructor"

  def childMethod(self):
    print 'Calling child1 method'
    Parent.parentMethod(self) #调用基类的方法，所以要加上参数self
class Child2(Parent): # define child2 class
  #没有实现__init__方法，则会调用基类的__init__方法
  def childMethod(self):
    print 'Calling child2 method'
    self.parentMethod()  #子类调用自己从父类那继承过来的父类的方法

c1 = Child1() # 实例化子类 1
c2 = Child2() # 实例化子类 2，没有写子类构造函数，直接调用父类
c1.childMethod() # 调用子类1的方法
c2.childMethod() # 调用子类2的方法
c1.parentMethod() # 子类实例对象调用父类方法
c1.setAttr(200) # 再次调用父类的方法
c1.getAttr() # 再次调用父类的方法
