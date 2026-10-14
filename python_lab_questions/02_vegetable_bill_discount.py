# Question: Vegetable bill with 10% discount when quantity > 10 kg.
def calculate_bill(quantity, price_per_kg):
    total = quantity * price_per_kg
    if quantity > 10:
        total *= 0.90
    return total

if __name__ == "__main__":
    vegetable = input("Enter vegetable name: ")
    quantity = float(input("Enter quantity in kg: "))
    price = float(input("Enter price per kg: "))
    print("Vegetable:", vegetable)
    print("Total bill:", round(calculate_bill(quantity, price), 2))
