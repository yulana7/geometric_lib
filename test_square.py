import unittest
from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = area(3)
        self.assertEqual(res, 9)
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_float_area(self):
        res = area(2.27)
        self.assertEqual(res, 5.1529)
    def test_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_float_perimeter(self):
        res = perimeter(2.27)
        self.assertEqual(res, 9.08)

