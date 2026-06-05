# # Day 027 - Data Visualization With Matplotlib
#
# Learn: line plots, bar charts, labels, titles, figure size.
#
# Practice: plot student marks and monthly sales.
#
# Output: save at least 2 charts as PNG files.
#
# Review: what makes a chart easy to understand?
#

# Code here
import matplotlib.pyplot as plt

students = ["Ali", "Sara", "Omar", "Noor"]
marks = [89, 88.5, 79, 92.5]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

boys = ["owais","sameer","qaasim","sourabh"]

marks = [90,70,85,63]

plt.bar(boys,marks)

plt.title("Boys Marks")
plt.xlabel("boys")
plt.ylabel("marks")

plt.show()