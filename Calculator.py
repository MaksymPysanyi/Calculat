import unittest
class Calculator:
    def power (self, a, b):
        return a ** b
    
    def gsd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_power(self):
        calculator = Calculator()
        self.assertEqual(calculator.power(5, 3), 125)

    def test_gsd(self):
        calculator = Calculator()
        self.assertEqual(calculator.gsd(12, 18), 6)

if __name__ == "__main__":
    unittest.main()

calculator = Calculator()
result = calculator.power(5, 3)
print("Результат", result)