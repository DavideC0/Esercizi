import unittest
from calc import Calculations

class TestCalc(unittest.TestCase):
    
    def test_sum(self):
        calc_1:Calculations = Calculations(2,3)
        result = calc_1.get_sum()
        self.assertEqual(result, 5, f"Error Test failed the goal was 5 the function return {result}")
        
if __name__ == '__main__':
    unittest.main()