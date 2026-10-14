# Question: Increase employee salary by 15% if it is below 20000.
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id, self.name, self.salary = emp_id, name, salary
    def increase_salary(self):
        if self.salary < 20000:
            self.salary *= 1.15
        print("Employee:", self.name)
        print("Salary:", round(self.salary, 2))

if __name__ == "__main__":
    Employee(101, "Alan", 18000).increase_salary()
