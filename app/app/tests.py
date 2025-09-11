"""
Tests the functions
"""

from django.test import SimpleTestCase

from app import calc


class TestCalcFunc(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 7)

        self.assertEqual(res, 12)

    def test_substract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10, 18)

        self.assertEqual(res, 8)
