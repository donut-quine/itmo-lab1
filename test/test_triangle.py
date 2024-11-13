import unittest

from geometric_lib.triangle import area, perimeter
from geometric_lib.exceptions import NotPositiveLengthException


class TriangleTestCase(unittest.TestCase):
    def test_negative_area(self):
        self.assertRaises(NotPositiveLengthException, lambda: area(-1, 123))

    def test_negative_perimeter(self):
        self.assertRaises(NotPositiveLengthException, lambda: perimeter(123, -1, 1))

    def test_zero_area(self):
        self.assertRaises(NotPositiveLengthException, lambda: area(0, 0))

    def test_zero_perimeter(self):
        self.assertRaises(NotPositiveLengthException, lambda: perimeter(0, 1, 2))
    
    def test_area(self):
        self.assertEqual(6, area(3, 4))
    
    def test_perimeter(self):
        self.assertEqual(12, perimeter(3, 4, 5))
