# Attendance Analysis System using Sets

attendance = {
    "Monday": {"Amit", "Rahul", "Chetan"},
    "Tuesday": {"Amit", "Chetan", "Rohit"},
    "Wednesday": {"Amit", "Chetan"},
    "Thursday": {"Amit", "Rahul", "Chetan"},
    "Friday": {"Amit", "Chetan", "Sneha"}
}

# 1. Total unique students throughout the week
all_students = set()
for day, attendees in attendance.items():
    all_students = all_students.union(attendees)

print("Total unique students:", len(all_students), "->", all_students)

# 2. Students who attended every single day
all_attended = set(all_students)
for day, attendees in attendance.items():
    all_attended = all_attended.intersection(attendees)

print("Students who attended all classes:", all_attended)

# 3. Students who attended only one day
only_one = set()
for student in all_students:
    count = sum(1 for day, attendees in attendance.items() if student in attendees)
    if count == 1:
        only_one.add(student)

print("Students who attended only one day:", only_one)
