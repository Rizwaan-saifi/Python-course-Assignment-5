# Task 1: Create a Dictionary of Student Marks
# Problem Statement: Write a Python program that:

# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.

student_marks = { 'Alice': 85, 'Bob': 90, 'Carol': 70, 'David': 80 }

student_name = input('Enter the student name: ')
if student_name in student_marks:
    mark = student_marks[student_name]
    print(f'The mark of {student_name} is: {mark}')
else:
    print('Student not found')