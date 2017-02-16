#coding=utf-8
class UniversityMember(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Student(UniversityMember):
    def __init__(self, name, age, sno, Department):
        #注意要显示调用父类构造方法，并传递参数self
        UniversityMember.__init__(self, name, age)
        self.sno = sno
        self.Department = Department

    def getSno(self):
        return self.sno

    def getDepartment(self):
        return self.Department

s = Student("fosterwu", "18", "CS", 18)
print s.name, s.age
s.name = 'superman'
print s.name
print s.getName()
print s.getAge()


