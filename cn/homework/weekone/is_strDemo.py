#encoding=utf-8
#判断一个对象是不是字符串类型
def is_str(s):
    if isinstance(s,(str,unicode)):#basestring相当于str\unicode的集合体
        return True
    try:
        s+"a"   #判断类是否有拼接字符串的功能，上方的if判断可不要
        return True
    except Exception,e:
        return False

print is_str("abd")
print is_str(21)

#assert断言，不能加print，当与预期结果不一致时会抛出异常AssertionError
assert is_str("abc")
assert is_str(21)==False
#assert is_str(21)==True #与预期结果不一致时会抛出异常AssertionError

#定义了一个类，type是instance
class newstring():
    def __init__(self, value):
        self.value=value
    def __str__(self):
        return self.value
    def __add__(self, other):
        return str(self.value)+str(other)

print is_str(newstring("abc"))
print is_str(newstring(0))

#查看类的type
print type(newstring("abc"))

#查看类的功能
print newstring("abd")+"a"
print newstring("abd").value