# Question: Find second-largest distinct number in a tuple without sorting.
def second_largest(numbers):
    largest = second = None
    for number in numbers:
        if largest is None or number > largest:
            if number != largest:
                second = largest
            largest = number
        elif number != largest and (second is None or number > second):
            second = number
    return second

if __name__ == "__main__":
    values = (10, 25, 8, 40, 15, 30, 5, 35, 20, 12)
    print("Second largest:", second_largest(values))
