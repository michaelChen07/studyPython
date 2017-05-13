#encoding=utf-8
import unittest
import random

# 被测试类
class MyClass(object):
    @classmethod
    def sum(self, a, b):
        return a + b

    @classmethod
    def div(self, a, b):
        return a / b

    @classmethod
    def retrun_None(self):
        return None

# 单元测试类
class MyTest(unittest.TestCase):

    # assertEqual()方法实例
    def test_assertEqual(self):
        # 断言两数之和的结果
        try:
            a, b = 1, 2
            sum = 13
            self.assertEqual(a + b, sum, '断言失败，%s + %s != %s'.decode("utf-8").encode("gbk") %(a, b, sum))
        except AssertionError, e:
            print e

    # assertNotEqual()方法实例
    def test_assertNotEqual(self):
        # 断言两数之差的结果
        try:
            a, b = 5, 2
            res = 3
            self.assertNotEqual(a - b, res, '断言失败，%s - %s != %s'.decode("utf-8").encode("gbk") %(a, b, res))
        except AssertionError, e:
            print e

    # assertTrue()方法实例
    def test_assertTrue(self):
        # 断言表达式的为真
        try:
            self.assertTrue(1 == 1, "表达式为假")
        except AssertionError, e:
            print e

    # assertFalse()方法实例
    def test_assertFalse(self):
        # 断言表达式为假
        try:
            self.assertFalse(3 == 2, "表达式为真")
        except AssertionError, e:
            print e

    # assertIs()方法实例
    def test_assertIs(self):
        # 断言两变量类型属于同一对象
        try:
            a = 12
            b = a
            self.assertIs(a, b, "%s与%s不属于同一对象" %(a, b))
        except AssertionError, e:
            print e

    # test_assertIsNot()方法实例
    def test_assertIsNot(self):
        # 断言两变量类型不属于同一对象
        try:
            a = 12
            b = "test"
            self.assertIsNot(a, b, "%s与%s属于同一对象" %(a, b))
        except AssertionError, e:
            print e

    # assertIsNone()方法实例
    def test_assertIsNone(self):
        # 断言表达式结果为None
        try:
            result = MyClass.retrun_None()
            self.assertIsNone(result, "not is None")
        except AssertionError, e:
            print e

    # assertIsNotNone()方法实例
    def test_assertIsNotNone(self):
        # 断言表达式结果不为None
        try:
            result = MyClass.sum(2, 5)
            self.assertIsNotNone(result, "is None")
        except AssertionError, e:
            print e

    # assertIn()方法实例
    def test_assertIn(self):
        # 断言对象A是否包含在对象B中
        try:
            strA = "this is a test"
            strB = "is"
            self.assertIn(strB, strA, "%s不包含在%s中" %(strB, strA))
        except AssertionError, e:
            print e

    # assertNotIn()方法实例
    def test_assertNotIn(self):
        # 断言对象A不包含在对象B中
        try:
            strA = "this is a test"
            strB = "Selenium"
            self.assertNotIn(strB, strA, "%s包含在%s中" %(strB, strA))
        except AssertionError, e:
            print e

    # assertIsInstance()方法实例
    def test_assertIsInstance(self):
        # 测试对象A的类型是否值指定的类型
        try:
            x = MyClass
            y = object
            self.assertIsInstance(x, y, "%s的类型不是%s" %(x, y))
        except AssertionError, e:
            print e

    # assertNotIsInstance()方法实例
    def test_assertNotIsInstance(self):
        # 测试对象A的类型不是指定的类型
        try:
            a = 123
            b = str
            self.assertNotIsInstance(a, b, "%s的类型是%s" %(a, b))
        except AssertionError, e:
            print e

    # assertRaises()方法实例
    def test_assertRaises(self):
        # 测试抛出的指定的异常类型
        # assertRaises(exception)
        with self.assertRaises(ValueError) as cm:
            random.sample([1,2,3,4,5], "j")
        # 打印详细的异常信息
        print "===", cm.exception

        # assertRaises(exception, callable, *args, **kwds)
        try:
            self.assertRaises(ZeroDivisionError, MyClass.div, 3, 0)
        except ZeroDivisionError, e:
            print e

    # assertRaisesRegexp()方法实例
    def test_assertRaisesRegexp(self):
        # 测试抛出的指定异常类型，并用正则表达式具体验证
        # assertRaisesRegexp(exception, regexp)
        with self.assertRaisesRegexp(ValueError, 'literal') as ar:
            int("xyz")
        # 打印详细的异常信息
        print ar.exception
        # 打印正则表达式
        print "re:",ar.expected_regexp.pattern

        # assertRaisesRegexp(exception, regexp, callable, *args, **kwds)
        try:
            self.assertRaisesRegexp(ValueError, "invalid literal for.*XYZ'$", int, 'XYZ')
        except AssertionError, e:
            print e


if __name__ == '__main__':
    # 执行单元测试
    unittest.main()
