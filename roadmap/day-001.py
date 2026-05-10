# # Day 001 - Dictionaries and Nested Data
#
# Learn: dictionary keys/values, updating entries, `.get()`, loops over dictionaries, nested dictionaries.
#
# Practice: create a `student_report.py` program with 3 students, their marks, average, and grade.
#
# Output: print each student's name, marks, average, and grade cleanly.
#
# Review: when should you use a dictionary instead of a list?
#

# Code here
#Student report
students = {

    "owais":{
        "maths":90,
        "english":90,
        "dsa":100
    },

    "rishan":{
        "maths":98,
        "english":89,
        "dsa":77
    },

    "sameer" : {
        "maths":56,
        "english":99,
        "dsa":100
    }

}

for student_name, data in students.items():

    total_marks = (
        data["maths"] +
        data["english"] +
        data["dsa"]
    )

    average = total_marks / 3

    print("Student:", student_name)
    print("Total Marks:", total_marks)
    print("Average:", average)
    print()
