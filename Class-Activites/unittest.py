import unittest

class TestTipCalculator(unittest.TestCase):
    def test_tip_calculator(self):
        # Test case 1: Bill amount is $30 (Tip rate should be 10%)
        tc1 = TipCalculator(30)
        self.assertEqual(tc1.get_tip_rate(), 0.10)
        self.assertEqual(tc1.calculate_tip(), 3.00)
        self.assertEqual(tc1.total_amount(), 33.00)
        
        # Test case 2: Bill amount is $50 (Tip rate should be 10%)
        tc2 = TipCalculator(50)
        self.assertEqual(tc2.get_tip_rate(), 0.10)
        self.assertEqual(tc2.calculate_tip(), 5.00)
        self.assertEqual(tc2.total_amount(), 55.00)

        # Test case 3: Bill amount is $100 (Tip rate should be 15%)
        tc3 = TipCalculator(100)
        self.assertEqual(tc3.get_tip_rate(), 0.15)
        self.assertEqual(tc3.calculate_tip(), 15.00)
        self.assertEqual(tc3.total_amount(), 115.00)

        # Test case 4: Bill amount is $150 (Tip rate should be 15%)
        tc4 = TipCalculator(150)
        self.assertEqual(tc4.get_tip_rate(), 0.15)
        self.assertEqual(tc4.calculate_tip(), 22.50)
        self.assertEqual(tc4.total_amount(), 172.50)

        # Test case 5: Bill amount is $200 (Tip rate should be 20%)
        tc5 = TipCalculator(200)
        self.assertEqual(tc5.get_tip_rate(), 0.20)
        self.assertEqual(tc5.calculate_tip(), 40.00)
        self.assertEqual(tc5.total_amount(), 240.00)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)