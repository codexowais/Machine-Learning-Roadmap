# # Day 023 - Selecting and Filtering Data
#
# Learn: selecting columns, `.loc`, `.iloc`, conditions.
#
# Practice: filter students by grade and marks.
#
# Output: show students above average and selected columns only.
#
# Review: when do you use `.loc` vs `.iloc`?
#

# Code here
import pandas as pd

students = {
    "Name": ["Ayan", "Sara", "Rohan", "Zara"],
    "Age": [18, 19, 18, 20],
    "Marks": [85, 92, 78, 90],
    "Grade": ["B", "A", "C", "A"]

}

df = pd.DataFrame(students)

print(df)


print(df["Marks"])
print (df[["Marks","Name"]])

print(df.loc[[3,"age"]])
print(df.loc[2:3,["Name","Age"]])

high_marks = df[df["Marks"]>85]
print(high_marks)

grade_a = df[df["Grade"]=="A"]
print(f"A Grade is {grade_a}")

avg_marks = df["Marks"].mean()

above_avg = df[df["Marks"]>avg_marks]

print(above_avg)

print(df["Name"])

print(df["Marks"])