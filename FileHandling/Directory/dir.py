import os

print(os.getcwd())
print(os.listdir())

os.mkdir("test")
# os.rmdir("test")

print(os.path.exists("ex.txt"))
print(os.path.isfile("ex.txt"))
print(os.path.isdir("test"))

# os.rename("ex.txt", "new.txt")
# os.remove("new.txt")