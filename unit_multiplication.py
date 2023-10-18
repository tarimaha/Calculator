from calculator import multiply_numbers
import unittest

class TestMultiplication(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        result = multiply(3, 4)
        self.assertEqual(result, 12)

    def test_multiply_negative_numbers(self):
        result = multiply(-5, -2)
        self.assertEqual(result, 10)

    def test_multiply_zero(self):
        result = multiply(7, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()