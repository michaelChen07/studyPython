# encoding=utf-8
import unittest
from Calc import Calc

class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print u"单元测试前，创建Calc类的实例"
        self.c = Calc()

    # 具体的测试用例，一定要以test开头
    def test_add(self):

        self.assertEqual(self.c.add(1, 2, 12), 15, 'test add fail')
