# 14. Read a text file and replace all occurrences of a specified word with another word. Save the modified text in the same file or a new file.

filename = input("enter file name: ")
old = input("enter word to replace: ")
new = input("enter new word: ")

file = open(filename,"r")
s = file.read()
file.close()

s = s.replace(old,new)

newfile = input("enter new file name: ")

file = open(newfile,"w")
file.write(s)
file.close()

print("file saved")
