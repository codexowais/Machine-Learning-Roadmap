# # Day 010 - Practice Project: Student Analytics CLI
#
# Learn: combine lists, dictionaries, functions, files, and CSV.
#
# Practice: build a command-line student analytics program.
#
# Output: add students, save to CSV, load from CSV, calculate class average, find topper.
#
# Review: which part of your code should become a function?
#

# Code here
import csv
from pathlib import Path

csv_path = Path(__file__).with_name("students_data.csv")

students = []

with open(csv_path, "r", newline="") as file:

    reader = csv.reader(file)

    next(reader, None)

    for row in reader:

        student = {

            "name": row[0],
            "math": int(row[1]),
            "english": int(row[2]),
            "dsa": int(row[3]),
            "python": int(row[4])

        }

        students.append(student)


def calculate_average(student):

    return (
        student["math"] +
        student["english"] +
        student["dsa"] +
        student["python"]
    ) / 4


def class_topper(students):

    highest_average = 0
    topper = None

    for student in students:

        average = calculate_average(student)

        if average > highest_average:

            highest_average = average
            topper = student

    return topper


top_student = class_topper(students)

if top_student:

    average = calculate_average(top_student)

    print("Class Topper:", top_student["name"])
    print("Math:", top_student["math"])
    print("English:", top_student["english"])
    print("DSA:", top_student["dsa"])
    print("Python:", top_student["python"])
    print("Average:", average)

else:

    print("No student records found.")