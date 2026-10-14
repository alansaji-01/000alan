# Import functions from 14_math_module.py to calculate circle area and factorial.
import math_module
radius = float(input('Enter radius: '))
number = int(input('Enter a non-negative integer: '))
print('Circle area:', round(math_module.circle_area(radius), 2))
print('Factorial:', math_module.factorial(number))
