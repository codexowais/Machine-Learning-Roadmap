# # Day 028 - Visualization With Seaborn
#
# Learn: histograms, scatter plots, box plots, pair plots.
#
# Practice: visualize marks or a simple public dataset.
#
# Output: create 3 plots and write one insight for each.
#
# Review: which plot shows distribution best?
#

# Code here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

students = {
    "Name": ["Rahul", "Aisha", "Arjun", "Fatima",
             "Priya", "Omar", "Neha", "David"],

    "Marks": [88, 92, 79, 95, 85, 90, 87, 82],

    "Hours_Studied": [6, 8, 5, 9, 7, 8, 6, 5]
}

df = pd.DataFrame(students)

sns.histplot(df["Marks"])

plt.show()