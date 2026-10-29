# 18. Store employee ID, name, department, and salary in a file. Write functions to display all employees, find the highest-paid employee, calculate average salary, and display employees earning above a given salary.

def display():
    file = open("employees.txt","r")

    for line in file:
        print(line.strip())

    file.close()


def highest():
    file = open("employees.txt","r")

    highest_salary = 0
    highest_name = ""

    for line in file:
        data = line.strip().split(",")
        salary = float(data[3])

        if salary > highest_salary:
            highest_salary = salary
            highest_name = data[1]

    file.close()

    print("highest paid employee =",highest_name)
    print("salary =",highest_salary)


def average():
    file = open("employees.txt","r")

    total = 0
    count = 0

    for line in file:
        data = line.strip().split(",")
        total += float(data[3])
        count += 1

    file.close()

    print("average salary =",total/count)


def above():
    amount = float(input("enter salary: "))

    file = open("employees.txt","r")

    for line in file:
        data = line.strip().split(",")

        if float(data[3]) > amount:
            print(data[1],data[3])

    file.close()


display()
highest()
average()
above()
