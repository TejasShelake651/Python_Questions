# # 1.	Write a program to building a simple student grade management system 
# # for a class of students. The system will store student
# #  names and their grades (both as lists) and should be
# # able to perform the following operations:
# Student_List=[]

# def addStudent(name, grade):
#     Student_List.append((name, grade))
#     print("Student {name} with grade {grade} added.")
#     print("Current Student List:")
#     for student in Student_List:
#         print(student)

# addStudent("Tejas","A")
# addStudent("samir","B")
# addStudent("aman","C")
# addStudent("sahil","D")

# def updateGrade(name1,grade,updatedGrade):
#     if name1 in Student_List:
#         if grade in Student_List:
#             grade.replace(updatedGrade) 
#     print("student",name1 ,"grade updated to" ,updatedGrade)




# updateGrade("samir","B","Z")


# def deleteStudent(name):
#     for student in Student_List:
#         if student[0] == name:
#             Student_List.remove(student)
#             print(f"Student {name} deleted.")
#             break
#     else:
#         print(f"Student {name} not found.")

# deleteStudent("Tejas")

# def averageGrade():
#     total = 0
#     for student in Student_List:
#         grade = student[1]
#         if grade == "A":
#             total += 4
#         elif grade == "B":
#             total += 3
#         elif grade == "C":
#             total += 2
#         elif grade == "D":
#             total += 1
#     average = total / len(Student_List) if Student_List else 0
#     print(f"Average Grade: {average:.2f}")

# averageGrade()

# def highestGrade():
#     highest = None
#     for student in Student_List:
#         grade = student[1]
#         if highest is None or grade < highest:
#             highest = grade
#     print(f"Highest Grade: {highest}")

# def lowestGrade():
#     lowest = None
#     for student in Student_List:
#         grade = student[1]
#         if lowest is None or grade > lowest:
#             lowest = grade
#     print(f"Lowest Grade: {lowest}")

# highestGrade()
# lowestGrade()



# 7.	Write a program to develop an inventory system for a small store.
#     Each product has a name and a quantity in stock.
#     The system should allow you to:

# ●	Add new products with their quantities.
# ●	Update the quantity of an existing product.
# ●	Display the product with the highest stock.
# ●	Remove a product from the inventory once it is sold out (quantity reaches 0).
# ●	Display the total number of unique products in the inventory.

stock=[]

def addProducts(names,quantity):
    stock.append(names)

addProducts("Samosa",20)
print(stock)




