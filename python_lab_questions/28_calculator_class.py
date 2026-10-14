# Calculator class with addition, subtraction, multiplication and division.
class Calculator:
    def __init__(self, first, second):
        self.first, self.second = first, second
    def add(self): return self.first + self.second
    def subtract(self): return self.first - self.second
    def multiply(self): return self.first * self.second
    def divide(self):
        try:
            return self.first / self.second
        except ZeroDivisionError:
            return 'Cannot divide by zero'

if __name__ == '__main__':
    calc = Calculator(10, 5)
    print('Addition:', calc.add())
    print('Subtraction:', calc.subtract())
    print('Multiplication:', calc.multiply())
    print('Division:', calc.divide())
