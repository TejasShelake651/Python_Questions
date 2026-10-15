file = open("ex.txt", "r")

print(file.read())# reads the enitre file and give the normal output file
print(file.readline())# reads the first line of the file
print(file.readlines())#reads the entire file and gives the output in list format

file.close()

file = open("ex.txt", "w")
file.write("This is random file")
file.close()

file = open("ex.txt", "a")
file.write("\nNew line")
file.close()

file = open("ex.txt", "r+")
print(file.read())
file.write("\nUpdated")
file.close()

file = open("ex.txt", "w+")
file.write("New content")
file.seek(0)
print(file.read())
file.close()

file = open("ex.txt", "a+")
file.write("\nAppend content")
file.seek(0)
print(file.read())
file.close()