import pandas as pd

students = {
    "Name": ["Rahul", "Aisha", "Arjun", "Fatima", "Priya"],
    "Math": [88, 92, 79, 95, 85],
    "Science": [84, 95, 81, 91, 89],
    "Hours_Studied": [6, 8, 5, 9, 7]
}


df = pd.DataFrame(students)

print(df.head())
print(df.columns)
print(df.describe())

print(df["Math"])
print(df["Math"]>85)
avg = ((df["Math"])+(df["Science"]))/2
print(avg)
