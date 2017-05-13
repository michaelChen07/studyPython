# encoding=utf-8
import unittest
from Calc import Calc

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.num = 5

    def test_Factorial(self):
        # 生成一个递增序列
        seq = range(1, self.num + 1)
        # 求阶乘
        res = reduce(lambda x, y: x * y, seq)
        # 断言阶乘结果
        self.assertEqual(res, 120, "断言阶乘结果错误！")
