# 15. Read a Python source file and create another file after removing single-line comments.

filename = input("enter python file name: ")
newfile = input("enter new file name: ")

file = open(filename,"r")
lines = file.readlines()
file.close()

file = open(newfile,"w")

for line in lines:
    if "#" in line:
        line = line[:line.index("#")]

    if line.strip() != "":
        file.write(line)

file.close()

print("file created")
