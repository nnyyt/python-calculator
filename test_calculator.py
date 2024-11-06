import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(1,4),5)

    def test_sub(self):
        self.assertEqual(self.calc.subtract(2,4), -2)
        self.assertEqual(self.calc.subtract(4,2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(4,2), 8)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4,2), 2)
        self.assertEqual(self.calc.divide(24,8), 3)

    def test_mol(self):
        self.assertEqual(self.calc.modulo(4,2), 0)
        self.assertEqual(self.calc.modulo(52,7), 3)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()