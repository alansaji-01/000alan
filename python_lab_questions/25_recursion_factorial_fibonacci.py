# Calculate factorial and Fibonacci series recursively and iteratively.
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_loop(n):
    result = 1
    for value in range(1, n + 1):
        result *= value
    return result

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_loop(terms):
    a, b, result = 0, 1, []
    for _ in range(terms):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == '__main__':
    n = int(input('Enter a non-negative integer: '))
    if n < 0:
        print('Enter a non-negative integer')
    else:
        print('Recursive factorial:', factorial_recursive(n))
        print('Loop factorial:', factorial_loop(n))
        print('Recursive Fibonacci:', [fibonacci_recursive(i) for i in range(n)])
        print('Loop Fibonacci:', fibonacci_loop(n))
