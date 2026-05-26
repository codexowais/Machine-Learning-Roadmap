# Day 010 Mini Project: Student Performance Tracker
#
# Real-world use case:
# Build a small command-line tool for a teacher or tutor who wants to track
# students, subject marks, averages, grades, and the class topper.
#
# Skills from days 001-010:
# dictionaries, nested data, strings, functions, error handling, text files,
# CSV files, modules, and list comprehensions.
#
# Build checklist:
# - Add students with subject marks.
# - Validate marks so bad input does not crash the program.
# - Save and load student records from a CSV file.
# - Show class average, each student's average, grade, and topper.
# - Keep repeated logic inside clean functions.


# Start coding your project here.
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
            "english": int(row[1]),
            "math": int(row[2]),
            "python": int(row[3]),
            "dsa": int(row[4])
        }

        students.append(student)


def calculate_avg(student):

    return (
        student["english"] +
        student["math"] +
        student["python"] +
        student["dsa"]
    ) / 4


def class_topper():

    highest_average = 0
    topper = None

    for student in students:

        average = calculate_avg(student)

        if average > highest_average:
            highest_average = average
            topper = student

    return topper


top_student = class_topper()

if top_student:

    average = calculate_avg(top_student)

    print("Class Topper:", top_student["name"])
    print("Math:", top_student["math"])
    print("English:", top_student["english"])
    print("DSA:", top_student["dsa"])
    print("Python:", top_student["python"])
    print("Average:", average)

else:
    print("No student records found.")