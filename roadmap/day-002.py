# # Day 002 - Tuples, Sets, and Choosing Data Structures
#
# Learn: tuples, sets, uniqueness, membership checks, and when to use list vs tuple vs set vs dict.
#
# Practice: build a small contact manager that prevents duplicate phone numbers.
#
# Output: a script that adds, searches, and displays contacts.
#
# Review: why are sets useful for duplicate removal?
#

# Code here
# number = int(input("Enter your number:"))
# numbers = {
#     9182823302,
#     1283234382,
#     9754895652,
#     8879798923
# }

# if number in numbers:
#     print("Number already present")
# else:
#     numbers.add(number)
#     print("Number added successfully") 

# print(numbers)
       
contacts = {}

numbers ={8455126564,
          66566466654,
          566564841131}

name = input("enter your name:")
number = int(input("Enter your number:"))

if number in numbers:
    print("Number already exists")
else:
    numbers.add(number)
    contacts[name]=number

print("contact added successfully")

print(contacts)
