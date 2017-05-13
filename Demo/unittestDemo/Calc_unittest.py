# encoding=utf-8
import unittest
from Calc import Calc

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        self.c = Calc()
        print "setup completed!"

    def test_add(self):
        self.assertTrue(self.c.add(1,2,3,4)==10)

    def test_sub(self):
        self.assertTrue(self.c.sub(10,2,3,4)==0)

    def test_mul(self):
        self.assertTrue(self.c.mul(1,2,3,4)==24)

    def test_div(self):
        self.assertTrue(self.c.div(100,10,2)==5)

    def tearDown(self):
        print "tearDown completed"

if __name__ == '__main__':
    unittest.main()
