# coding=utf-8
class Calc(object):

    #实例方法
    def add(self, x, y, *d):
        # 加法计算
        result = x + y
        for i in d:
            result += i
        return result

    def sub(self, x, y, *d):
        # 减法计算
        result = x - y
        for i in d:
            result -= i
        return result

    #类方法
    @classmethod
    def mul(cls, x, y, *d):
        # 乘法计算
        result = x * y
        for i in d:
            result *= i
        return result

    #静态方法，不能使用实例变量
    @staticmethod
    def div(x, y, *d):
        # 除法计算
        if y != 0:
            result = x / y
        else:
            return -1
        for i in d:
            if i != 0:
                result /= i
            else:
                return -1
        return result


if __name__ == "__main__":
    c = Calc()
    print c.add(1, 2, 3, 4)
    print c.mul(2, 3, 4)
    print c.div(10, 5)
    print Calc.mul(1, 2, 3, 4)
    print Calc.div(100, 10, 5, 1)


def sum(a,b,*args,**kw):
    print a,b
    for i in args:
        print i
    for i in kw.values():
        print i
sum(1,2,3)
sum(1,2,3,4,5)
sum(1,2,3,4,5,[6,7,8])


