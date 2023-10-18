import unittest
import calculator

class TestCalc(unittest,TestCase):
    # All Calculator tests go here 

    def test_subtraction(self):
        result = calculator.subtraction(23,10)
        self.assertEqual(result,13)
