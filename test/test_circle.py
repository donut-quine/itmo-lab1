import unittest

from geometric_lib.circle import area, perimeter
from geometric_lib.exceptions import NotPositiveLengthException

class CircleTestCase(unittest.TestCase):
    def test_negative_area(self):
        self.assertRaises(NotPositiveLengthException, lambda: area(-1))

    def test_negative_perimeter(self):
        self.assertRaises(NotPositiveLengthException, lambda: perimeter(-1))

    def test_zero_area(self):
        self.assertRaises(NotPositiveLengthException, lambda: area(0))

    def test_zero_perimeter(self):
        self.assertRaises(NotPositiveLengthException, lambda: perimeter(0))
    
    def test_area(self):
        self.assertEqual(314.1592653589793, area(10))
    
    def test_perimeter(self):
        self.assertEqual(62.83185307179586, perimeter(10))
