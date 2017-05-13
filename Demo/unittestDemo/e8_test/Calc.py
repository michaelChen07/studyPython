# coding=utf-8
class Calc(object):

    def add(self, x, y, *d):
        # 加法计算
        result = x + y
        for i in d:
            result += i
        return result

    def mul(self, a, b):
        # 返回两数之积
        return a * b
