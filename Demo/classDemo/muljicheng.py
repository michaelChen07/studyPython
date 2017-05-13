#coding=utf-8
class Person(object):
    def __init__(self, name):
        print "Person name is:"
        self.name=name

    def get_name(self):
        return self.name


class University(object):
    def __init__(self, name):
        print "University name is:"
        self.name=name

    def get_name(self):
        return self.name


class Teacher(Person,University):
    def get_teachername(self):
        print "Teacher:"
        return self.get_name()

teacher1=Teacher("lily")
print teacher1.get_teachername()
