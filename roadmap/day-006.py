# # Day 006 - Files: Read and Write Text
#
# Learn: `open()`, `with`, reading lines, writing text files, appending logs.
#
# Practice: save student report results into `reports.txt`.
#
# Output: a script that reads marks, calculates grades, and writes a report file.
#
# Review: why do we use `with open(...)`?
#

# Code here

def calculate_average(marks):

    total = sum(marks.values())
    average = total / len(marks)

    return average


def assign_grade(average):

    if average >= 90:
        return "A"

    elif average >= 75:
        return "B"

    elif average >= 50:
        return "C"

    else:
        return "Fail"


name = input("Enter student name: ")

marks = {}

for i in range(3):

    subject = input("Enter subject name: ")
    score = int(input(f"Enter marks for {subject}: "))

    marks[subject] = score


average = calculate_average(marks)
grade = assign_grade(average)



with open("detail.txt","a") as file:


    file.write("Hello Owais\n")

    file.write(f"Student:{name}\n")
    file.write(f"Average:{average}\n")
    file.write(f"Grade:{grade}\n")
    file.write("------------------------\n")



