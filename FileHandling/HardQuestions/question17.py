# 17. Create a file containing student records in the format: RollNo,Name,Marks
# Sample data format:
# 101,Amit,85
# 102,Priya,92
# 103,Rahul,78
# Write a program to display all records, find the student with highest marks, calculate average marks, and display students who scored more than 80.

file = open("students.txt", "r")
lines = file.readlines()
file.close()

marks = []
highest = 0
topper = ""

for line in lines:
    data = line.strip().split(",")
    roll = data[0]
    name = data[1]
    m = int(data[2])
    marks.append(m)

    if m > highest:
        highest = m
        topper = name

    if m > 80:
        print("scored more than 80 =", name)

print("topper =", topper, "marks =", highest)
print("average marks =", sum(marks) / len(marks))
