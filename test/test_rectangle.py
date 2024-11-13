import unittest

from geometric_lib.rectangle import area, perimeter
from geometric_lib.exceptions import NotPositiveLengthException

class RectangleTestCase(unittest.TestCase):    
    def test_negative_area(self):
        self.assertRaises(NotPositiveLengthException, lambda: area(10, -10))

    def test_negative_perimeter(self):
        self.assertRaises(NotPositiveLengthException, lambda: perimeter(10, -20))

    def test_zero_area(self):
        self.assertRaises(NotPositiveLengthException, lambda: area(10, 0))

    def test_zero_perimeter(self):
        self.assertRaises(NotPositiveLengthException, lambda: perimeter(10, 0))
    
    def test_area(self):
        self.assertEqual(200, area(10, 20))
    
    def test_square_area(self):
        self.assertEqual(100, area(10, 10))
    
    def test_rect_perimeter(self):
        self.assertEqual(60, perimeter(10, 20))
    
    def test_square_perimeter(self):
        self.assertEqual(40, perimeter(10, 10))
