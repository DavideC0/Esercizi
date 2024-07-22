import unittest
from calc import Calculations

class TestCalc(unittest.TestCase):
    
    def test_sum(self):
        calc_1:Calculations = Calculations(2,3)
        result = calc_1.get_sum()
        self.assertEqual(result, 5, f"Error Test failed the goal was 5 the function return {result}")
    
    def test_diff(self):
        calc_2:Calculations = Calculations(3,2)
        result = calc_2.get_difference()
        self.assertEqual(result, 1, f"Error Test failed the goal was 1 the function return {result}")

    def test_product(self):
        calc_3:Calculations = Calculations(3,2)
        result = calc_3.get_product()
        self.assertEqual(result, 6, f"Error Test failed the goal was 6 the function return {result}")

    def test_quotient(self):
        calc_4:Calculations = Calculations(10,2)
        result = calc_4.get_quotient()
        self.assertEqual(result, 5.0 , f"Error Test failed the goal was 5.0 the function return {result}")
        
if __name__ == '__main__':
    unittest.main()