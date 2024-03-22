import unittest
class calculator:
    def add(self, a, b):
        return a + b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.cal = calculator()
    
    def test_add(self):
        a, b = 5, 3
        result = self.cal.add(a, b)
        self.assertEqual(result, 8, "Sum of 5 and 3 should be 8")

if __name__ == "__main__":
    unittest.main()

cal = calculator()
result = cal.add(5, 3)
print("Результат", result)