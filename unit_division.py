from calculator import divide
import unittest


class TestDivision(unittest.TestCase):
    def test_divide_positive_numbers(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_negative_numbers(self):
        result = divide(-10, -2)
        self.assertEqual(result, 5)

    def test_divide_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()