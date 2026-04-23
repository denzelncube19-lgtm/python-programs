# Student Class - OOP Basics
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
    def is_pass(self):
        return self.grade >= 50

s = Student(input("Student name: "), int(input("Age: ")), float(input("Grade: ")))
s.display()
print("Status:", "PASS" if s.is_pass() else "FAIL")
