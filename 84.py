class Student:
    def __init__(self, name, student_id, grades):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# Example Usage
student = Student("Alice", "S101", [85, 90, 78])
print("Average Grade:", student.average_grade())
