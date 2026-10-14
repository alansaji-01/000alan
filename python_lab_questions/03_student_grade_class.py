# Question: Student class to calculate total, average and grade.
class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.marks = [mark1, mark2, mark3]
    def total(self):
        return sum(self.marks)
    def average(self):
        return self.total() / 3
    def display_grade(self):
        avg = self.average()
        grade = "A" if avg >= 80 else "B" if avg >= 60 else "C"
        print("Name:", self.name, "\nTotal:", self.total(), "\nAverage:", round(avg, 2), "\nGrade:", grade)

if __name__ == "__main__":
    Student("Alan", 85, 75, 90).display_grade()
