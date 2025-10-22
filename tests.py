import unittest
from decimal import Decimal
from main import isPassed

class TestIsPassedValid(unittest.TestCase):
    def test_failed_grades(self):
        self.assertEqual(isPassed(Decimal("2")), False)

    def test_passed_grades(self):
        self.assertEqual(isPassed(Decimal("7.3")), True)

class TestIsPassedInvalid(unittest.TestCase):
    def test_below_range(self):
        with self.assertRaises(ValueError):
            isPassed(Decimal("-5"))

    def test_above_range(self):
        with self.assertRaises(ValueError):
            isPassed(Decimal("15"))

    def test_non_numeric_value(self):
        with self.assertRaises(ValueError):
            isPassed(None)
        with self.assertRaises(ValueError):
            isPassed("seven")

class TestIsPassedBoundary(unittest.TestCase):
    def test_minimum_valid(self):
        self.assertEqual(isPassed(Decimal("0")), False)

    def test_maximum_valid(self):
        self.assertEqual(isPassed(Decimal("10")), True)

    def test_passing_valid(self):
        self.assertEqual(isPassed(Decimal("5")), True)

    def test_below_minimum_invalid(self):
        with self.assertRaises(ValueError):
            isPassed(Decimal("-1"))

    def test_above_maximum_invalid(self):
        with self.assertRaises(ValueError):
            isPassed(Decimal("11"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
