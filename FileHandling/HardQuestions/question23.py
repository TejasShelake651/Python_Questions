# 23. Write a program to compare two text files and display whether their contents are identical. If different, identify the first line where they differ.

file1 = input("enter first file name: ")
file2 = input("enter second file name: ")

f1 = open(file1, "r")
lines1 = f1.readlines()
f1.close()

f2 = open(file2, "r")
lines2 = f2.readlines()
f2.close()

same = True

length = min(len(lines1), len(lines2))

for i in range(length):
    if lines1[i] != lines2[i]:
        print("files are different")
        print("first different line =", i + 1)
        same = False
        break

if same:
    if len(lines1) == len(lines2):
        print("files are identical")
    else:
        print("files are different")
        print("first different line =", length + 1)
