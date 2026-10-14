# Question: Store five medicine prices in a dictionary and search by name.
medicines = {"Paracetamol": 20, "Cetirizine": 30, "Amoxicillin": 80, "VitaminC": 50, "Antacid": 25}
name = input("Enter medicine name: ").strip()
match = next((key for key in medicines if key.lower() == name.lower()), None)
if match:
    print("Price:", medicines[match])
else:
    print("Medicine not available")
