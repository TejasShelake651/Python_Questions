# 13. Accept a word from the user and search for it in a text file. Display the number of occurrences and the line numbers where it appears.

filename = input("enter file name: ")
word = input("enter word to search: ")

file = open(filename,"r")
lines = file.readlines()
file.close()

count = 0
line_numbers = []

for i in range(len(lines)):
    words = lines[i].split()

    for j in words:
        if j == word:
            count += 1

            if i+1 not in line_numbers:
                line_numbers.append(i+1)

print("occurrences =",count)
print("line numbers =",line_numbers)
