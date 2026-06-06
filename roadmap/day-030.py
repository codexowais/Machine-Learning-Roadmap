# # Day 030 - Exploratory Data Analysis Project
#
# Learn: EDA workflow.
#
# Practice: choose a small CSV dataset and explore it.
#
# Output: notebook or script with loading, cleaning, stats, charts, and 5 insights.
#
# Review: what questions did your data answer?
#

# Code here
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("StudentPerformanceFactors.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isna().sum())

#STATISTICS

print("\n===== EXAM SCORE STATISTICS =====")

mean_score = df["Exam_Score"].mean()
median_score = df["Exam_Score"].median()
mode_score = df["Exam_Score"].mode()[0]
variance_score = df["Exam_Score"].var()
std_score = df["Exam_Score"].std()

print("Mean:", mean_score)
print("Median:", median_score)
print("Mode:", mode_score)
print("Variance:", variance_score)
print("Standard Deviation:", std_score)


print("\n===== CORRELATION =====")

corr_hours = df["Hours_Studied"].corr(df["Exam_Score"])
corr_attendance = df["Attendance"].corr(df["Exam_Score"])
corr_previous = df["Previous_Scores"].corr(df["Exam_Score"])

print("Hours Studied vs Exam Score:", corr_hours)
print("Attendance vs Exam Score:", corr_attendance)
print("Previous Scores vs Exam Score:", corr_previous)

#HISTOGRAM

plt.figure(figsize=(8,5))

sns.histplot(df["Exam_Score"],bins = 15)
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")

plt.savefig("exam_score_histogram.png")
plt.show()


# ==========================
# CHART 2 - SCATTER PLOT
# ==========================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    x="Hours_Studied",
    y="Exam_Score",
    data=df
)

plt.title("Hours Studied vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")

plt.savefig("hours_vs_score.png")
plt.show()

# ==========================
# CHART 3 - BAR CHART
# ==========================

avg_scores = (
    df.groupby("Motivation_Level")["Exam_Score"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(8, 5))

sns.barplot(
    x="Motivation_Level",
    y="Exam_Score",
    data=avg_scores
)

plt.title("Average Exam Score by Motivation Level")
plt.xlabel("Motivation Level")
plt.ylabel("Average Exam Score")

plt.savefig("motivation_vs_score.png")
plt.show()

# ==========================
# INSIGHTS
# ==========================

print("\n===== SAMPLE INSIGHTS =====")

print("1. Most students scored around the average range.")
print("2. Hours studied appears related to exam performance.")
print("3. Previous scores help predict future scores.")
print("4. Motivation level may influence performance.")
print("5. Attendance and exam scores can be compared for trends.")