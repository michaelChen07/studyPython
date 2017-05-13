#coding=utf-8
import unittest

if __name__ == '__main__' :
    # 加载当前目录下所有有效的测试模块（以test开头的文件），“.”表示当前目录
    testSuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity = 2).run(testSuite)