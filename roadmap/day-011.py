# # Day 011 - Object-Oriented Programming Basics
#
# Learn: classes, objects, attributes, methods, `__init__`.
#
# Practice: create a `Student` class with marks and average calculation.
#
# Output: `student_oop.py` with at least 3 student objects.
#
# Review: what is the difference between a dictionary and an object?
#

# Code here
class Student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def Calculate_average(self):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        return (m1+m2+m3)/3
    

name = input("Enter Name:")
m1 = int(input("Enter Mark1:"))
m2 = int(input("Enter Mark2:"))
m3 = int(input("Enter Mark3:"))

details = Student(name,m1,m2,m3)
average = details.Calculate_average()

print(details.name)
print("average",average)