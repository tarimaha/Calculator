import unittest
import calculator

class TestCalc(unittest.TestCase):
    # All Calculator tests go here 

    def test_subtraction(self):
        self.assertEqual( calculator.subtract(23,10), 13)
        self.assertEqual( calculator.subtract(-1,1), -2)
        self.assertEqual( calculator.subtract(1,-1), 2)
        self.assertEqual( calculator.subtract(-10,-10), 0)
        
        
        



if __name__ == "__main__":
    unittest.main()