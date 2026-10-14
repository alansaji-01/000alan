# Question: User-defined exception if voting age is less than 18.
class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise AgeError("Not eligible to vote")
    print("Eligible to vote")
except ValueError:
    print("Enter a valid integer age")
except AgeError as error:
    print(error)
