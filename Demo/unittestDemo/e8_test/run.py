#coding=utf-8
import unittest

if __name__ == '__main__' :
    # ���ص�ǰĿ¼��������Ч�Ĳ���ģ�飨��test��ͷ���ļ�������.����ʾ��ǰĿ¼
    testSuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity = 2).run(testSuite)