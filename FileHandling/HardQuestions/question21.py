# 21. Maintain book records containing book ID, title, author, and availability status. Implement operations to add a book, search for a book, issue a book, return a book, and display available books.

def add_book():
    id = input("enter book id: ")
    title = input("enter title: ")
    author = input("enter author: ")

    file = open("books.txt","a")
    file.write(id + "," + title + "," + author + ",available\n")
    file.close()

    print("book added")


def search_book():
    title = input("enter title: ")

    file = open("books.txt","r")

    found = False

    for line in file:
        data = line.strip().split(",")

        if data[1].lower() == title.lower():
            print(line.strip())
            found = True

    file.close()

    if not found:
        print("book not found")


def issue_book():
    id = input("enter book id: ")

    file = open("books.txt","r")
    lines = file.readlines()
    file.close()

    file = open("books.txt","w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == id:
            data[3] = "issued"
            line = ",".join(data) + "\n"

        file.write(line)

    file.close()

    print("book issued")


def return_book():
    id = input("enter book id: ")

    file = open("books.txt","r")
    lines = file.readlines()
    file.close()

    file = open("books.txt","w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == id:
            data[3] = "available"
            line = ",".join(data) + "\n"

        file.write(line)

    file.close()

    print("book returned")


def available_books():
    file = open("books.txt","r")

    for line in file:
        data = line.strip().split(",")

        if data[3] == "available":
            print(line.strip())

    file.close()


add_book()
search_book()
issue_book()
return_book()
available_books()
