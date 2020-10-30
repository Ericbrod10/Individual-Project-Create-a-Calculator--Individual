import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    # Define setUp for Tests
    def setUp(self) -> None:
        self.calculator = Calculator()
        self.data = CsvReader()

    # Instance Test
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_Instance_CsvReader(self):
        self.assertIsInstance(self.data, CsvReader)

    # Addition Test
    def test_add_method_calculator(self):
        test_data = self.data.Text_Reader('/src/UnitTestCSVFiles/Addition.csv')
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    # Subtraction Test
    def test_subtract_method_calculator(self):
        test_data = self.data.Text_Reader('/src/UnitTestCSVFiles/Subtraction.csv')
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    # Multiplication Test
    def test_multiplication_calculator(self):
        test_data = self.data.Text_Reader('/src/UnitTestCSVFiles/Multiplication.csv')
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'],  row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    # Division Test
    def test_division_calculator(self):
        test_data = self.data.Text_Reader('/src/UnitTestCSVFiles/Division.csv')
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    # Squaring a Value Test
    def test_square_calculator(self):
        test_data = self.data.Text_Reader('/src/UnitTestCSVFiles/Square.csv')
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    # Taking Square Root of Value Test
    def test_squareRoot_calculator(self):
        test_data = self.data.Text_Reader('/src/UnitTestCSVFiles/SquareRoot.csv')
        for row in test_data:
            self.assertEqual(self.calculator.squared_root(row['Value 1']), round(float(row['Result']), 8))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 8))


if __name__ == '__main__':
    unittest.main()
