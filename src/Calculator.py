from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from division import division
from square import square_value
from square_root import square_root


class Calculator:
    result = 0

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square_value(a)
        return self.result

    def squared_root(self, a):
        self.result = square_root(a)
        return self.result

    def __init__(self):
        pass
