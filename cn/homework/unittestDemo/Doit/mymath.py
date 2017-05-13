#encoding=utf-8

class Person(object):
    "created by gloryroad teacher wu"
    person_count=0
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        Person.person_count+=1
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    def get_person_count(self):
        return Person.person_count

p=Person("fosterwu","50","male")

print p.__dict__
print Person.__dict__
print "-"*50
print Person.__doc__
print "-"*50
print Person.__name__
print "-"*50
print Person.__module__
print "-"*50
print Person.__bases__

