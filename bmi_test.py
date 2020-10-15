import unittest
from bmi import BmiCalculator
class TestBmi(unittest.TestCase):

    def setUp(self):
        self.bmi_calci = BmiCalculator()

    
    def test_bmi(self):

        self.assertEqual(self.bmi_calci.bmi(height = 165,weight=60)[0] ,22.04)
        self.assertEqual(self.bmi_calci.bmi(height = 165,weight=55)[0] ,20.2)

if __name__ == "__main__":
    unittest.main()