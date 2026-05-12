# # Day 004 - Functions With Clean Inputs and Outputs
#
# Learn: parameters, return values, default arguments, small reusable functions.
#
# Practice: rewrite your calculator and grade programs using functions only.
#
# Output: `functions_practice.py` with at least 5 clear functions.
#
# Review: what makes a function easy to test?
#

# Code here
def add_numbers(a,b):
    return a+b
def sub_numbers(a,b):
    return a-b
def mul_numbers(a,b):
    return a*b
def div_numbers(a,b):
    if b == 0:
        print("invalid")
    else:
        return a/b

a = int(input("Enter a:"))
b = int(input("Enter b:"))

add  = add_numbers(a,b)
sub = sub_numbers(a,b)
mul = mul_numbers(a,b)
div = div_numbers(a,b)

print("sum = ",add)
print ("diff =",sub)
print ("product =",mul)
print("division = ",div)