# # Day 024 - Cleaning Missing Data
#
# Learn: missing values, `.isna()`, `.dropna()`, `.fillna()`.
#
# Practice: create a small dataset with missing marks and clean it.
#
# Output: compare before and after cleaning.
#
# Review: what are the risks of filling missing values blindly?
#

# Code here
# Day 024 - Cleaning Missing Data

import pandas as pd
import numpy as np

# Create dataset with missing marks
students = {
    "Name": ["Ali", "Fatima", "Omar", "Noor"],
    "Marks": [92, np.nan, 81, np.nan],
    "Age": [18, 19, np.nan, 20]
}

df = pd.DataFrame(students)

missing_values = df.isna()

missing_count = missing_values.sum()

clean_df = df.dropna()

print(df)
print(missing_values)
print(missing_count)
print(clean_df)

avg_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(avg_marks)

avg_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(avg_age)


print(avg_marks)


print(avg_age)

print("\nCleaned DataFrame:")
print(df)
