# # Day 026 - Sorting and Creating Columns
#
# Learn: sorting rows, adding columns, applying simple formulas.
#
# Practice: add average and grade columns to a student DataFrame.
#
# Output: sorted student leaderboard.
#
# Review: why should raw data and derived columns be separated mentally?
#

# Code here
import pandas as pd

students = {
    "Name": ["Ali", "Sara", "Omar", "Noor"],
    "Math": [90, 85, 78, 95],
    "Science": [88, 92, 80, 90]
}

df = pd.DataFrame(students)

print(df)
df["Average"] = (df["Math"]+df["Science"])/2


def assign_grade(average):
    if average>=90:
        return "A"
    elif average>=80:
        return "B"
    else:
        return "C"
    
df["Grade"] = df["Average"].apply(assign_grade)

df["Status"] = df["Average"].apply(
    lambda x : "Pass" if x>= 85 else "Needs Improvement"
)

leaderboard = df.sort_values(
    by="Average",
    ascending = False
)

print ("======STUDENT LEADERBOARD ====")
print(leaderboard)