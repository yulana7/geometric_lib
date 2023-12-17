import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(7, 8)
        self.assertEqual(res, 56)
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_float_area(self):
        res = area(7.7, 10.2)
        self.assertEqual(res, 78.53999999999999)
    def test_perimeter(self):
        res = perimeter(5, 3)
        self.assertEqual(res, 16)
    def test_zero_perimeter(self):
        res = perimeter(0, 10)
        self.assertRaises(Exception, res, 'incorrect input')
    def test_float_perimeter(self):
        res = perimeter(7.7, 10.2)
        self.assertEqual(res, 35.8)

