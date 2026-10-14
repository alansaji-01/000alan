# Demonstrate ValueError and ZeroDivisionError using try/except/else/finally.
try:
    numerator = int(input('Enter numerator: '))
    denominator = int(input('Enter denominator: '))
    result = numerator / denominator
except ValueError:
    print('Enter valid integers')
except ZeroDivisionError:
    print('Cannot divide by zero')
else:
    print('Result:', result)
finally:
    print('Program completed')
