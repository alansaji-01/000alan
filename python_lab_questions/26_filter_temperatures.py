# Filter temperatures between 20 and 35 using list comprehension.
def filter_temperatures(temperatures):
    return [temp for temp in temperatures if 20 <= temp <= 35]

if __name__ == '__main__':
    values = [18, 22, 30, 36, 25, 40, 20, 35]
    print(filter_temperatures(values))
