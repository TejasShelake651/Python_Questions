"""
9. Write a program to develop an attendance system for a classroom. The system should track students who attended classes over a week. You need to:
● Store the names of students who attended class each day in a dictionary, where the day of the week is the key and the set of students is the value.
● Identify students who attended all classes during the week.
● Identify students who attended only one class during the week.
● Count the total number of unique students who attended at least one class during the week.
Tasks:
● Use a dictionary where the keys are days of the week, and the values are sets of students.
● Use set operations to find students who attended all or only one class.
"""

attendance = {
    "Mon": {"Alice", "Bob"},
    "Tue": {"Alice", "Charlie"},
    "Wed": {"Alice", "Bob", "Charlie"}
}

all_students = set().union(*attendance.values())
attended_all = set.intersection(*attendance.values()) if attendance else set()

counts = {}
for day, students in attendance.items():
    for student in students:
        counts[student] = counts.get(student, 0) + 1

attended_one = {student for student, count in counts.items() if count == 1}

print("Attended all:", attended_all)
print("Attended one:", attended_one)
print("Total unique:", len(all_students))
