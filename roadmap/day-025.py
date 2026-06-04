# # Day 025 - Grouping and Aggregation
#
# Learn: `groupby`, aggregate functions, category summaries.
#
# Practice: group sales data by product category.
#
# Output: total, average, and count per category.
#
# Review: why is grouping useful in real datasets?
#

# Code here
import pandas as pd

sales = {
    "Category": [
        "Electronics",
        "Clothing",
        "Electronics",
        "Books",
        "Clothing",
        "Books",
        "Electronics"
    ],
    "Sales": [
        5000,
        2000,
        7000,
        1500,
        3000,
        2500,
        6000
    ]
}

df = pd.DataFrame(sales)

print(df)

category_avg = df.groupby("Category")["Sales"].mean()
print(category_avg)
