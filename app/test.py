import unittest

from calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(calculate("Addition", 2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(calculate("Addition", -2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(calculate("Addition", 2, -3), -1)
    
    def test_subtract_positive_numbers(self):
        self.assertEqual(calculate("Subtraction", 3, 2), 1)

    def test_subtract_negative_numbers(self):
        # can't do this one
        self.assertEqual(calculate("Subtraction", -3, -2), -5)

if __name__ == "__main__":
    unittest.main()