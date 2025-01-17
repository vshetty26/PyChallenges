class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        return f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display(self):
        return f"{super().display()}, Department: {self.department}"

# Example Usage
manager = Manager("Alice", "M101", 80000, "HR")
print(manager.display())
