# num = int(input("Enter a number: "))
# if num >0 and num % 2 == 0:
#     print("The number is positive and even.")
# elif num > 0 and num % 2 != 0:
#         print("The number is positive and odd.")
# elif num < 0 and num % 2 == 0:  
#         print("The number is negative and even.")
# elif num <0 and num % 2 !=0:
#         print("The number is negative and odd.")

# a = int(input("Enter a number: "))
# b = int(input("Enter 2nd number: "))
# c = int(input("Enter 3rd number: "))
# d = int(input("Enter 4th number: "))
# e = int(input("Enter 5th number: "))

# list = [a,b,c,d,e]
# print("The largest number is: ", max(list))
# print("The smallest number is",min(list))
# sum = a + b + c + d + e
# print("The sum of the numbers is: ", sum)
# avg = sum/5
# print("The average of the numbers is: ", avg)

# store = []
# for i in range(5):
#     num = int(input("Enter a number: "))
#     store.append(num)


# print (store)
# print ("the largest number is ",max(store))
# print ("the smallest number is ",min(store))
# print ("The sum is ",sum(store))




# num = int(input("Enter a number: "))
# is_prime = True


# if num >1:
#     for i in range(2,num):
#         if num % i ==0:
#             is_prime = False
#             break


#     if is_prime:
#         print("Number is prime")
#     else:
#         print("Number is not prime")

# else:
#     print("Number is not prime")


# def add_numbers(a,b):
#     return a+b
# def subtract_numbers(a,b):
#     return a-b  
# def multiply_numbers(a,b):              
#     return a*b
# def divide_numbers(a,b):    
#     if b != 0:
#         return a/b
#     else:
#         return "Error: Division by zero is not allowed."
    
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))    
# print("Addition: ", add_numbers(num1,num2))
# print("Subtraction: ", subtract_numbers(num1,num2))
# print("Multiplication: ", multiply_numbers(num1,num2))
# print("Division: ", divide_numbers(num1,num2))


# Name  = input("Enter your name:")
# sub1 = int(input("Enter marks for subject 1: "))
# sub2 = int(input("Enter marks for subject 2: "))    
# sub3 = int(input("Enter marks for subject 3: "))
# total  = sub1+sub2+sub3
# average =total/3

# if average >= 90:
#     grade = "A"
# elif average >= 80:
#     grade = "B"
# elif average >= 70:
#     grade = "C"
# elif average >= 60:
#     grade = "D"
# else:
#     grade = "F"


# print("Name: ", Name)
# print("Total Marks: ", total)
# print("Average Marks: ", average)
# print("Grade: ", grade)


# numbers = []
# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)





# print("The numbers are: ", numbers)
# print("The largest number is: ", max(numbers))
# print("The smallest number is: ", min(numbers))
# print("The sum of the numbers is: ", sum(numbers))
# print("The average of the numbers is: ", sum(numbers)/5)

student  = {
    "name":"xyx",
    "age":19,
    "course": "Ai"
}

print(student["name"])