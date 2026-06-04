# # Day 022 - Reading CSV With Pandas
#
# Learn: `pd.read_csv`, `.head()`, `.info()`, `.describe()`.
#
# Practice: load your student CSV from Day 007 using pandas.
#
# Output: inspect shape, columns, data types, and summary.
#
# Review: what does `.info()` tell you?
#

# Code here
import pandas as pd
df = pd.read_csv("students.csv")
print (df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()

print(df.describe())