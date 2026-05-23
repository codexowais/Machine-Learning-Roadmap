# # Day 007 - CSV Files
#
# Learn: CSV structure, Python `csv` module, rows, headers, basic parsing.
#
# Practice: create `students.csv` and calculate averages from it.
#
# Output: a script that reads CSV data and prints sorted student results.
#
# Review: why are CSV files common in data science?
#

# Code here
import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:

        name = row[0]

        maths = int(row[1])
        english = int(row[2])
        dsa = int(row[3])

        average = (maths + english + dsa) / 3

        print(f"{name} → Average: {average}")