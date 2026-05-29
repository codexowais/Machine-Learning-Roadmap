# # Day 017 - NumPy Operations
#
# Learn: vectorized operations, broadcasting, element-wise math.
#
# Practice: convert Celsius to Fahrenheit for an array of temperatures.
#
# Output: compare loop-based and NumPy-based calculations.
#
# Review: why is vectorization useful?
#

# Code here
import numpy as np

# celcius = np.array([39,45,96,90.80])

# fahrenheit_loop = []

# for temp in celcius:
#     fahrenheit_loop.append(float((temp*9/5)+32))ok

# print ("using loop:")
# print(fahrenheit_loop)    



# import numpy as np
# celcius = np.array([0,10,20,30,40])
# fahrenheit_numpy = (celcius*9/5)+32
# print ("using loop")
# print(fahrenheit_numpy)


arr = np.array([70,66,56,98])
cost_after_gst = (arr*1.18)
print("The cost after gst :",cost_after_gst)
