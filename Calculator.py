import unittest
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    
    def test_add(self):
        a, b = 5, 3
        result = self.calculator.add(a, b)
        self.assertEqual(result, 8, "Sum of 5 and 3 should be 8")
    
    def test_subtract(self):
        a, b = 5, 3
        result=self.calculator.subtract(a,b)
        self.assertEqual(result, 2, "Subtract of 5 and 3 sholud be 2")


if __name__ == "__main__":
    unittest.main()

calculator = Calculator()
result = calculator.add(5, 3)
print("Результат", result)