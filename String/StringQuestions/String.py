●	Write a program to input a string and display its length without using the len() function. 

string=str(input("Enter the string"))
count=0

for i in string:
    count+=1
print("Length of the string is ",count)


●Count the number of vowels, consonants, digits, spaces, and special characters in a given string. 

string1=str(input("Enter the string"))

for i in string1:
    if(i>='a' and i<='z') or (i>='A' and i<='Z'):
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            print(i,"is vowel")
        
        else:
            print(i,"is consonant")
    elif(i>='0' and i<='9'):
        print(i,"is digit")
    elif(i==" "):
        print("space")
    else:
        print(i,"is special character")

# ●	Reverse the given string without using built-in reverse functions. 

# string2=str(input("Enter the strings"))

# string2=string2[::-1]
# print(string2)

#●	Check whether the entered string is a palindrome. 

# string3=str(input("Enter the string"))

# string=string3[::-1]

# if(string3 == string):
#     print("the string is palindrome")

# else:
#     print("The string is not palindrome")

#●	Count the number of uppercase and lowercase letters in a string. 

# string=str(input("enter the string"))
# countL=0
# countU=0
# for i in string:
#     if(i>='a' and i<='z'):
#         countL+=1
       
#     else:
#        countU+=1

# print("lowercase =",countL)
# print("uppercase ",countU)

# #●	Replace all occurrences of a given character with another character
# string=str(input('Enter the strings'))
# for i in string:
#     if(i=='a'):
#         string=string.replace('a','A')
# print(string)

#●	Remove all spaces from the input string. 

# string=str(input("Enter the string"))
# for i in string:
#     if(i==" "):
#         string=string.replace(" ","")
# print(string)

#●	Find the number of times a specified character appears in a string. 

# string=str(input("Enter the string"))
# n=str(input("enter the ch"))
# for i in string:
#     if(i==n):
#         count=string.count(n)
# print(count)

#●	Print the first and last character of a string. 

# string=str(input("Enter the string"))
# FirstChar=string[0]
# LastChar=string[-1]

# print(FirstChar)
# print(LastChar)

#●	Display each character of a string along with its ASCII value.
# string=str(input("Enter the string"))

# for i in string:
#     char=ord(i)
#     print(i,"=",char)


#a.	Count the total number of words in a sentence. 

# string =str(input("Enter the string"))
# count=0
# for i in string:
#     if(i == " "):
#         count+=1
# print(count+1)


#a.	Find the longest word in a given sentence. 
# string=str(input("enter the string"))
# for char in string:
#     if char in ['.',',','!','?']:
#         string=string.replace(char,"")

# words=string.split(" ")
# longest_word = ""

str="tejas"
str.lo