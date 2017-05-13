#encoding=utf-8
class Animal(object):#新式类
    """creat animal,also can count them"""
    animal_count = 0#类变量
    def __init__(self,name,sex,length):
        self.name = name
        self.sex = sex
        self.length = length#加self表示该变量只在该实例本身有效
        Animal.animal_count += 1

    def get_Animal_name(self):#方法
        return self.name
    def get_Animal_count(self):
        return self.animal_count
    def get_a(self,a):
        return a

    @classmethod#类方法
    def class_animal(cls,a):
        print Animal.animal_count + a

    @staticmethod#静态方法
    def static_animal(b):
        print Animal.animal_count*b

    @property#属性
    def prop(self):
        return "tt"

tiger = Animal("tiger","f","50")#实例化
tiger.sex = "F"#增加实例属性
print tiger.sex

print Animal.__doc__#类的文档字符串
print tiger.__dict__#实例变量的属性
print Animal.__dict__#类的属性
print Animal.__name__#类名
print Animal.__module__#所在模块
print Animal.__base__#查看父类

#修改
a=Animal("cat")
Animal.count=10
print Animal.count
Animal.class1="kind"
print Animal.class1
Animal.class1="new kind"
print Animal.class1
del Animal.class1


