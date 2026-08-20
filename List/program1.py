"""
1. Write a program to building a simple student grade management system for a class of students. The system will store student names and their grades (both as lists) and should be able to perform the following operations:
● Add a new student and their grade.
● Update the grade of an existing student.
● Remove a student from the list.
● Calculate and display the average grade of the class.
● Display the highest and lowest grades in the class.
Tasks:
● Use lists to store the student names and their corresponding grades.
● Implement functions to add, update, remove, and calculate the average and extreme grades.
"""

names = []
grades = []

def add_student(name, grade):
    names.append(name)
    grades.append(grade)

def update_grade(name, new_grade):
    if name in names:
        idx = names.index(name)
        grades[idx] = new_grade

def remove_student(name):
    if name in names:
        idx = names.index(name)
        names.pop(idx)
        grades.pop(idx)

def show_stats():
    if not grades:
        return
    avg = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    print(f"Average: {avg}, Highest: {highest}, Lowest: {lowest}")

add_student("Alice", 85)
add_student("Bob", 90)
update_grade("Alice", 88)
remove_student("Bob")
show_stats()
