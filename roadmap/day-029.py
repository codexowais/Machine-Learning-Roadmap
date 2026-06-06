# # Day 029 - Basic Statistics for ML
#
# Learn: mean, median, mode, variance, standard deviation, correlation.
#
# Math checkpoint (Required): study each statistic manually, including how
# outliers affect summaries and why correlation does not prove causation.
#
# Practice: calculate statistics manually and with pandas.
#
# Output: explain the difference between mean and median using data.
#
# Review: why can outliers affect the mean?
#

# Code here
import math
import pandas as pd

data = {
    "Name": ["Rahul", "Aisha", "Arjun", "Fatima",
             "Priya", "Omar", "Neha", "David"],

    "Marks": [88, 92, 79, 95, 85, 90, 87, 82],

    "Hours_Studied": [6, 8, 5, 9, 7, 8, 6, 5]
}

df = pd.DataFrame(data)

length = len(df["Marks"])
sum = df["Marks"].sum()
mean = df["Marks"].mean()
median = df["Marks"].median()
mode = df["Marks"].mode()
variance =df["Marks"].var()
sd = math.sqrt(variance)

print (length)
print (sum)
print (mean)
print(median)
print (mode)
print(variance)
print(sd)