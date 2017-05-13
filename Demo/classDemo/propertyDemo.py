#encoding=utf-8
import os
"""class Person(object):
    def __init__(self,name):
        self.Name = name
    def getName(self):
        print 'fetch...'
        return self.Name
    def setName(self, name):
        print 'change...'
        self.Name = name
    def delName(self):
        print 'remove...'
        del self.Name

    #通过property方法可以把类对象变量（self.Name）的获取、修改和删除方法 自动影射到类变量(bob.name)的三种行为
    name = property(getName,setName,delName,'name property docs')
    # name=property(getName,setName)

bob = Person('Bob Smith')
print bob.name
bob.name = 'Robert Smith'
print bob.name
del bob.name"""

print "*"*40


class Score(object) :
    def __init__(self, score) :
        self.Score = score
    def getscore(self):
        print "got score"
        return self.Score
    def changescore(self,score):
        print "change"
        self.Score=score
    def delscore(self):
        print "delete"
        del self.Score

    score = property(getscore,changescore,delscore,"score property docs")

student1 = Score("90")
print student1.score

student1.score = "80"
print student1.score

del student1.score


