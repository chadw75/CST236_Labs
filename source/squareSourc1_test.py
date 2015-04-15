"""
Test for source.squareSource1
"""
from source.squareSource1 import get_square_type
from unittest import TestCase

class TestGetSquareType(TestCase):

    def test_get_square_square_all_int(self):
        result = get_triangle_type(1, 1, 1, 1, 90, 90, 90, 90)
        self.assertEqual(result, 'square')

    def test_get_square_rectangle_all_int(self):
        result = get_square_type(1, 2, 1, 2, 90, 90, 90, 90)
        self.assertEqual(result, 'rectangle')

    def test_get_square_rhombus_all_int(self):
        result = get_square_type(1, 2, 1, 2, 87, 93, 87, 93)
        self.assertEqual(result, 'rectangle')

    def test_get_square_rectangle_all_int(self):
        result = get_square_type(1, 1, 1, 1, 87, 93, 87, 93)
        self.assertEqual(result, 'rhombus')

    def test_get_square_rectangle_all_int(self):
        result = get_square_type(0, 2, 3, 4, 87, 93, 87, 93)
        self.assertEqual(result, 'invalid')

    def test_get_square_rectangle_all_int(self):
        result = get_square_type(1, 2, 3, 4, 0, 93, 87, 93)
        self.assertEqual(result, 'invalid')

    def test_get_square_rectangle_all_int(self):
        result = get_square_type(1, 2, 3, 4, 180, 93, 87, 93)
        self.assertEqual(result, 'invalid')

    def test_get_square_rectangle_all_int(self):
        result = get_square_type(1, 0, 3, 4, 87, 180, 87, 93)
        self.assertEqual(result, 'invalid')

