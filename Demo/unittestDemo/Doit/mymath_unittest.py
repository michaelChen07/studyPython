# encoding=utf-8
import unittest
from mymath import Person

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):

        self.c = Person("lucy","18","female")
        print "setup completed!"

    def test_get_agg(self):
        self.assertTrue(self.c.get_age()=="18")

    def test_get_name(self):
        self.assertTrue(self.c.get_name()=="lily")

    def test_get_sex(self):
        self.assertTrue(self.c.get_sex()=="female")

    def test_get_person_count(self):
        self.assertTrue(self.c.get_person_count()==3)

    def tearDown(self):
        print "tearDown completed"

if __name__ == '__main__':
    unittest.main()