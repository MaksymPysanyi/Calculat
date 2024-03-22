import unittest
class Calculator:
    def power (self, a, b):
        return a ** b
    
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator()

    def test_power(self):
        calculator = Calculator()
        self.assertEqual(calculator.power(5, 3), 125)

if __name__ == "__main__":
    unittest.main()

calculator = Calculator()
result = calculator.power(5, 3)
print("Результат", result)