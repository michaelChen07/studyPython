#encoding=utf-8
class Person(object):
    def __init__(self, height, name):
        self.height = height
        self.name = name

    def get_height(self):
        return self.height

class Student(Person):
    def __init__(self, study_no, school):
        Person.__init__(self, 180, "lily")#子类要先初始化父类的构造函数
        self.study_no = study_no
        self.school = school

    def get_study_no(self):
        return self.study_no

    def get_school(self):
        return self.school

person1 = Person("180","xiao")
student1 = Student(001, "wuhanu")#如果是“001”，则会显示001
print student1.get_height()  # 调用父类方法
print student1.get_study_no()
print student1.get_school()  # 调用子类方法

print "*"*40




