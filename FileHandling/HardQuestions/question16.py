# 16. Read a text file and create another file containing the same text in uppercase.

filename = input("enter file name: ")
newfile = input("enter new file name: ")

file = open(filename,"r")
s = file.read()
file.close()

s = s.upper()

file = open(newfile,"w")
file.write(s)
file.close()

print("file created")
