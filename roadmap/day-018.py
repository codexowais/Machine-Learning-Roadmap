# # Day 018 - NumPy Filtering
#
# Learn: boolean masks, filtering arrays, conditional selection.
#
# Practice: filter student marks above 75 and prices below a budget.
#
# Output: use masks instead of manual loops.
#
# Review: what does a boolean mask contain?
#

# Code here
import numpy as np

temperatures = np.array([22, 35, 40, 18, 30, 45, 28])

temp_above30 = temperatures[temperatures > 30]
temp_below25 = temperatures[temperatures < 25]
in_between = temperatures[(temperatures > 20) & (temperatures < 40)]
temps_above30 = temperatures[temperatures>30]

print(temp_above30)
print(temp_below25)
print(in_between)
print(temps_above30)