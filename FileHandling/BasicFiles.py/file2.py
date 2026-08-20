file = open("ex.txt", "r")

print(file.read())
print(file.readline())
print(file.readlines())

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