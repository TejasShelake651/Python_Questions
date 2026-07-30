# #Program to check num is Even or Odd
# num=int(input("Enter the number"))
# if(num%2 == 0):
#     print(num,"is Even")
# else:
#     print(num,"is Odd")


# #Year is Leap Year or not
# year=int(input("Enter the year"))
# if(year%4==0):
#     print(year,"is Leap Year")
# else:
#     print(year,"is not Leap Year")


#Driver insurence conditions

status=str(input("Enter the Status"))
gender=str(input("enter the Gender"))
age=int(input("Enter the age"))

if(status == "married"):
    print("Driver is insured")
elif(status == "unmarried" and gender == "male" and age>30):
    print("driver is insured")
elif(status=="unmarried" and gender == "female" and age>25):
    print("driver is insured")
else:
    print("Driver is not insured")