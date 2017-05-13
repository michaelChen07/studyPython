#encoding=utf-8
import unittest

# 被测试类
class myclass(object):
    #加@classmethod：一个类只会执行一次
    @classmethod
    def sum(self, a, b):
        return a + b #将两个传入参数进行相加操作

    @classmethod
    def sub(self, a, b):
        return a - b #将两个传入参数进行相减操作


class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        "初始化类固件"
        print "----setUpClass"

    @classmethod
    def tearDownClass(cls):
        "重构类固件"
        print "----tearDownClass"

    # 初始化工作
    # 未加@classmethod：每个test case都会执行一次
    def setUp(self):
        self.a = 3
        self.b = 1
        print "--setUp"

    # 退出清理工作
    def tearDown(self):
        print "--tearDown"

    # 具体的测试用例，一定要以test开头
    def testsum(self):
        # 断言两数之和的结果是否是4
        self.assertEqual(myclass.sum(self.a, self.b), 4, 'test sum fail')

    def testsub(self):
        # 断言两数之差的结果是否是2
        self.assertEqual(myclass.sub(self.a, self.b), 2, 'test sub fail')


if __name__ == '__main__':
    unittest.main() # 启动单元测试
