#encoding=utf-8
import unittest
from Calc import Calc

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print u"单元测试前，创建Calc类的实例"
        self.c = Calc()

    # 具体的测试用例，一定要以test开头，执行顺序按照字母顺序开头
    def test_0add(self):
        print "run add()"
        self.assertEqual(self.c.add(1, 2, 12), 15, 'test add fail')

    def test_1sub(self):
        print "run sub()"
        self.assertEqual(self.c.sub(2, 1, 3), -2, 'test sub fail')

    def test_2mul(self):
        print "run mul()"
        self.assertEqual(Calc.mul(2, 3, 5), 30, 'test mul fail')

    def test_3div(self):
        print "run div()"
        self.assertEqual(Calc.div(8, 2, 4), 1, 'test div fail')


if __name__ == '__main__':
    unittest.main()# 启动单元测试
