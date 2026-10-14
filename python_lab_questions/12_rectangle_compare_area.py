# Question: Rectangle area and perimeter; compare two rectangle objects.
class Rectangle:
    def __init__(self, length, breadth):
        self.length, self.breadth = length, breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)

if __name__ == "__main__":
    r1, r2 = Rectangle(10, 5), Rectangle(8, 7)
    print("Rectangle 1 area:", r1.area(), "perimeter:", r1.perimeter())
    print("Rectangle 2 area:", r2.area(), "perimeter:", r2.perimeter())
    if r1.area() > r2.area(): print("Rectangle 1 has larger area")
    elif r2.area() > r1.area(): print("Rectangle 2 has larger area")
    else: print("Both have equal area")
