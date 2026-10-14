# Question: Remove duplicate crop names and display unique names alphabetically.
def unique_crops(crops):
    return sorted(set(crops))

if __name__ == "__main__":
    crops = ["Rice", "Wheat", "Rice", "Maize", "Wheat", "Coconut"]
    print("Unique crops:", unique_crops(crops))
