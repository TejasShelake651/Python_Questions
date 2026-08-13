# #program to print the natural numbers upto n
# n=int(input("enter the n"))

# for i in range(1,n):
#     print(i)

# #program to print even numbers upto n

# num=int(input("Enter the number"))
# for i in range(1,num+1):
#     if(i%2 == 0):
#         print(i)

# #Program to print Odd numbers upto n
# num=int(input("Enter the n"))
# for i in range(1,num):
#     if(i%2 != 0):
#         print(i)

# #program that prints the sqaures upto n
# n=int(input("Enter the n"))
# for i in range(1,n):
#     print(i*i)

# 5: Sum series 1 + 1/1! + 1/2! + ... + 1/n!
n = int(input("Enter n for series (5): "))
fact = 1
total = 1.0
for i in range(1, n+1):
	fact *= i
	total += 1 / fact
print(total)

# 6: Cosine series approximation cos(x) = 1 - x^2/2! + x^4/4! - ...
x = float(input("Enter x (radians) for cosine series (6): "))
terms = int(input("Enter number of terms: "))
cos_approx = 0.0
for k in range(0, terms+1):
	num = x**(2*k)
	denom = 1
	for j in range(1, 2*k+1):
		denom *= j
	cos_approx += ((-1)**k) * num / denom
print(cos_approx)

# 7: Check whether square root (if perfect square) is prime or not
import math
num = int(input("Enter number to check sqrt prime (7): "))
root = math.isqrt(num)
if root*root != num:
	print("Not a perfect square")
else:
	if root <= 1:
		print("Square root is not prime")
	else:
		is_p = True
		i = 2
		while i*i <= root:
			if root % i == 0:
				is_p = False
				break
			i += 1
		print("Prime" if is_p else "Not prime")

# 8: Print ABC block (3 lines)
for _ in range(3):
	print("A B C")

# 9: Increasing letter triangle
n = int(input("Enter n for increasing letters (9): "))
for i in range(1, n+1):
	print(' '.join(chr(65+j) for j in range(i)))

# 10: Decreasing letter triangle
n = int(input("Enter n for decreasing letters (10): "))
for i in range(n, 0, -1):
	print(' '.join(chr(65+j) for j in range(i)))

# 11: Increasing number triangle
n = int(input("Enter n for increasing numbers (11): "))
for i in range(1, n+1):
	print(' '.join(str(j) for j in range(1, i+1)))

# 12: Repeated-row number triangle
n = int(input("Enter n for repeated numbers (12): "))
for i in range(1, n+1):
	print(' '.join([str(i)]*i))

