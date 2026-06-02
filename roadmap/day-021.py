# # Day 021 - Pandas Series and DataFrames
#
# Learn: Series, DataFrame, columns, rows, loading data.
#
# Practice: create a DataFrame of students and marks.
#
# Output: print columns, first rows, and summary statistics.
#
# Review: why is pandas central to data science?
#

# Code here
import pandas as pd

# marks = pd.Series([85, 92, 78, 90])

# print(marks)

students = {
    "Name":["Ayan", "Sara", "Rohan", "Zara"],
    "Age":[18,19,18,20],
    "Marks":[85, 92, 78, 90]
}
df = pd.DataFrame(students)
print(df)
print(df.columns)
print (df.head(2))
print(df.describe())
print(df["Marks"])