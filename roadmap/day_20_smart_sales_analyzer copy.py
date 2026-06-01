# Day 020 Mini Project: Smart Sales Analyzer
#
# Real-world use case:
# Analyze one month of shop sales and help the owner spot best days, slow days,
# above-average sales days, and simple simulated future sales.
#
# Skills from days 011-020:
# OOP basics, packages, debugging, NumPy arrays, vectorized operations,
# filtering, random numbers, and simple numerical simulations.
#
# Build checklist:
# - Store daily sales in a NumPy array.
# - Calculate total, average, best day, worst day, and days above average.
# - Use boolean masks to filter strong and weak sales days.
# - Simulate a next-month sales estimate using NumPy random numbers.
# - Wrap the analysis in a small class or reusable functions.


# Start coding your project here.
import numpy as np


class SmartSalesAnalyzer:

    def __init__(self, sales):
        self.sales = np.array(sales)

    def summary(self):
        print("\n===== SALES SUMMARY =====")

        print("Total Sales:", np.sum(self.sales))
        print("Average Sales:", np.mean(self.sales))

        print("Best Sale:", np.max(self.sales))
        print("Best Day:", np.argmax(self.sales) + 1)

        print("Worst Sale:", np.min(self.sales))
        print("Worst Day:", np.argmin(self.sales) + 1)

    def filter_sales(self):
        avg = np.mean(self.sales)

        strong_days = self.sales[self.sales > avg]
        weak_days = self.sales[self.sales < avg]

        print("\n===== SALES FILTERING =====")

        print("Days Above Average:")
        print(strong_days)

        print("\nDays Below Average:")
        print(weak_days)

    def next_month_sale(self):
        np.random.seed(42)

        avg = np.mean(self.sales)
        std = np.std(self.sales)

        future_sales = np.random.normal(
            loc=avg,
            scale=std,
            size=30
        ).astype(int)

        print("\n===== NEXT MONTH ESTIMATE =====")
        print(future_sales)

        print("\nPredicted Total Sales:",
              np.sum(future_sales))

        print("Predicted Average Sales:",
              np.mean(future_sales))


# Sample sales data for one month
sales_data = [
    1200, 1500, 1800, 1700, 2000,
    2200, 2100, 1900, 2500, 2400,
    2600, 2300, 2800, 3000, 2900,
    2700, 3200, 3100, 3300, 3400,
    3500, 3600, 3700, 3800, 3900,
    4000, 4100, 4200, 4300, 4500
]

# Create object
analyzer = SmartSalesAnalyzer(sales_data)

# Run analysis
analyzer.summary()
analyzer.filter_sales()
analyzer.next_month_sale()



