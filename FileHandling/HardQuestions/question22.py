# 22. Read the contents of two text files and create a third file containing the contents of both files.

file1 = input("enter first file name: ")
file2 = input("enter second file name: ")
file3 = input("enter new file name: ")

file = open(file1,"r")
s1 = file.read()
file.close()

file = open(file2,"r")
s2 = file.read()
file.close()

file = open(file3,"w")
file.write(s1)
file.write("\n")
file.write(s2)
file.close()

print("file created")
