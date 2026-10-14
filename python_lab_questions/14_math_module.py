import math

def circle_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    return math.pi * radius ** 2

def factorial(number):
    if number < 0:
        raise ValueError('Number cannot be negative')
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result
