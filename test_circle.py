import unittest
from circle import area
from circle import perimeter
import math

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_pi_area(self):
        res = area(math.pi)
        self.assertEqual(res, 31.006276680299816)
    def test_float_area(self):
        res = area(4.5)
        self.assertEqual(res, 63.61725123519331)
    def test_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_pi_perimeter(self):
        res = perimeter(math.pi)
        self.assertEqual(res, 19.739208802178716)
    def test_float_perimeter(self):
        res = perimeter(2.27)
        self.assertEqual(res, 14.26283064729766)
