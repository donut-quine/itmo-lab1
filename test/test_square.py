import unittest

from geometric_lib.square import area, perimeter
from geometric_lib.exceptions import NotPositiveLengthException

class SquareTestCase(unittest.TestCase):
    def test_negative_area(self):
        self.assertRaises(NotPositiveLengthException, lambda: area(-10))

    def test_negative_perimeter(self):
        self.assertRaises(NotPositiveLengthException, lambda: perimeter(-1))

    def test_zero_area(self):
        self.assertRaises(NotPositiveLengthException, lambda: area(0))

    def test_zero_perimeter(self):
        self.assertRaises(NotPositiveLengthException, lambda: perimeter(0))
    
    def test_area(self):
        self.assertEqual(100, area(10))
    
    def test_perimeter(self):
        self.assertEqual(40, perimeter(10))
