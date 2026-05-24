# # Day 009 - List Comprehensions
#
# Learn: compact loops, filtering, transforming lists, readable comprehensions.
#
# Practice: clean a list of numbers, keep only positives, and square them.
#
# Output: one normal loop version and one list comprehension version.
#
# Review: when is a list comprehension too hard to read?
#

# Code here

numbers = [1,5,9,-7,10,-6,-2,0,5]
positive_squared = []

for number in numbers:
    if number>0:
        positive_squared.append(number**2)

print (positive_squared)        