# # Day 005 - Error Handling
#
# Learn: `try`, `except`, handling bad input, division by zero, and validation.
#
# Practice: improve your calculator so it never crashes on wrong input.
#
# Output: a calculator that handles invalid numbers and invalid operations.
#
# Review: what errors can users cause in your code?
#

# Code here
def add_numbers(a, b):
    return a + b


def sub_numbers(a, b):
    return a - b


def mul_numbers(a, b):
    return a * b


def div_numbers(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b


try:

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print("\n---- Select Option ----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Select option: "))

    if choice == 1:
        print("Sum =", add_numbers(a, b))

    elif choice == 2:
        print("Difference =", sub_numbers(a, b))

    elif choice == 3:
        print("Product =", mul_numbers(a, b))

    elif choice == 4:
        print("Division =", div_numbers(a, b))

    else:
        print("Invalid option")


except ValueError:
    print("Please enter valid numbers only")