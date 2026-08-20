# 5: Sum series 1 + 1/1! + 1/2! + ... + 1/n!
n = int(input("Enter n for series (5): "))
fact = 1
total = 1.0
for i in range(1, n+1):
	fact *= i
	total += 1 