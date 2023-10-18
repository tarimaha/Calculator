from calculator import calc_log
import unittest

class LogarithmTestCase(unittest.TestCase):

    def test_positive_number(self):
        #Test positive number
        result = calc_log(10)
        self.assertLogs(result,2.302585092994046)

    def test_negative_number(self):
        #Test negative number
        with self.assertRaises(ValueError):
            calc_log(-4)

if __name__ == '__main__':
    unittest.main()