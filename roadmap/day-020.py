# # Day 020 - NumPy Mini Project
#
# Learn: use NumPy for numerical analysis.
#
# Practice: analyze a fake month of sales data.
#
# Output: total sales, best day, worst day, average sales, days above average.
#
# Review: what tasks became easier with NumPy?
#

# Code here
import numpy as np

sales = np.array([
    1200, 1500, 1800, 1700, 2000,
    2200, 2100, 1900, 2500, 2400,
    2600, 2300, 2800, 3000, 2900,
    2700, 3200, 3100, 3300, 3400,
    3500, 3600, 3700, 3800, 3900,
    4000, 4100, 4200, 4300, 4500
])

total_sales = np.sum(sales)+1
best_day = np.max(sales)+1
worst_day  = np.min(sales)
avg_sales = np.mean(sales)
days_above_avg = sales[sales > avg_sales]

print (total_sales)
print (best_day)
print (worst_day)
print (avg_sales)
print (days_above_avg)