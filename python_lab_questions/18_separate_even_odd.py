# Separate even and odd numbers from a list using a function.
def separate_even_odd(numbers):
    even = [number for number in numbers if number % 2 == 0]
    odd = [number for number in numbers if number % 2 != 0]
    return even, odd

if __name__ == '__main__':
    numbers = list(range(1, 16))
    even, odd = separate_even_odd(numbers)
    print('Even:', even)
    print('Odd:', odd)
