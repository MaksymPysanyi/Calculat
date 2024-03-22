import unittest
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by 0 is not possible")
        return a / b 
    
    def power (self, a, b):
        return a ** b
    
    def gsd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(self, a, b):
        return a * b // self.gsd(a, b)

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

    def test_multiply(self):
        a, b = 5, 3
        result = self.calculator.multiply(a,b)
        self.assertEqual(result, 15, "Multiply of 5 and 3 sholud be 15")

    def test_divide(self):
        a, b = 5, 3
        result = self.calculator.divide(a, b)
        self.assertEqual(result, 1.666666667, "Divide of 5 and 2 should be 1.666666667")

    def test_power(self):
        calculator = Calculator()
        self.assertEqual(calculator.power(5, 3), 125)

    def test_gsd(self):
        calculator = Calculator()
        self.assertEqual(calculator.gsd(12, 18), 6)

    def test_lcm(self):
        calculator = Calculator()
        self.assertEqual(calculator.lcm(12, 18), 36)

if __name__ == "__main__":
    unittest.main()

calculator = Calculator()
result = calculator.add(5, 3)
print("Результат", result)