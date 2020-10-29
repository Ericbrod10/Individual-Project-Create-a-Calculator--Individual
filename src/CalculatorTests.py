import unittest
from Calculator import Calculator
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 6), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_multiplication_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 6), 12)
        self.assertEqual(self.calculator.result, 12)

    def test_division_calculator(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_square_calculator(self):
        self.assertEqual(self.calculator.square(10), 100)
        self.assertEqual(self.calculator.result, 100)

    def test_squareRoot_calculator(self):
        self.assertEqual(self.calculator.squared_root(16), 4)
        self.assertEqual(self.calculator.result, 4)


if __name__ == '__main__':
    unittest.main()
