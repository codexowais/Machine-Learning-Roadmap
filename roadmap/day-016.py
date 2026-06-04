# # Day 016 - NumPy Arrays
#
# Learn: arrays, shapes, dimensions, indexing, slicing.
#
# Math checkpoint (Required foundation): learn vectors, matrices, dimensions,
# rows, and columns. NumPy arrays are how ML stores numerical data.
#
# Practice: create arrays for marks, prices, and temperatures.
#
# Output: calculate min, max, mean, and selected slices using NumPy.
#
# Review: how is a NumPy array different from a Python list?
#

# Code here
import numpy as np

marks = np.array([90,85,78,92,88])

print("Array",marks)
print ("Shape:",marks.shape)
print("Dimensions:",marks.ndim)
print("First value:",marks[0])
print("slice:",marks[1:4])
print("Minimum:",marks.min())
print("Maximum:",marks.max())
print("Mean:",marks.mean())
