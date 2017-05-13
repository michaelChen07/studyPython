from unittest import TestCase
from Solver import Calculate


class TestCalculate(TestCase):
    def test_add(self):
        cal = Calculate()
        real = cal.add(4, 5)
        expect = 9
        self.assertEqual(real, expect)
5
    def test_mul(self):
        cal = Calculate()
        real = cal.mul(4, 5)
        expect = 20
        self.assertEqual(real, expect)
