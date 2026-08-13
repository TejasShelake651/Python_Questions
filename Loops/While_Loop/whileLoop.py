# 1: Print natural numbers up to n
n = int(input("Enter n for natural numbers (1): "))
i = 1
while i <= n:
    print(i)
    i += 1

# 2: Print even numbers up to n
n = int(input("Enter n for even numbers (2): "))
i = 2
while i <= n:
    print(i)
    i += 2

# 3: Print odd numbers up to n
n = int(input("Enter n for odd numbers (3): "))
i = 1
while i <= n:
    print(i)
    i += 2

# 4: Sum of natural numbers up to n
n = int(input("Enter n to sum natural numbers (4): "))
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print(s)

# 5: Sum of odd numbers up to n
n = int(input("Enter n to sum odd numbers (5): "))
s = 0
i = 1
while i <= n:
    s += i
    i += 2
print(s)

# 6: Sum of even numbers up to n
n = int(input("Enter n to sum even numbers (6): "))
s = 0
i = 2
while i <= n:
    s += i
    i += 2
print(s)

# 7: Print natural numbers in reverse up to n
n = int(input("Enter n to print reverse (7): "))
i = n
while i >= 1:
    print(i)
    i -= 1

# 8: Fibonacci series up to n terms
n = int(input("Enter number of terms for Fibonacci (8): "))
a, b = 0, 1
count = 0
while count < n:
    print(a)
    a, b = b, a + b
    count += 1

# 9: Factorial of given number
num = int(input("Enter number to find factorial (9): "))
res = 1
i = 1
while i <= num:
    res *= i
    i += 1
print(res)

# 10: Check whether entered number is prime
num = int(input("Enter number to check prime (10): "))
if num <= 1:
    print("Not prime")
else:
    i = 2
    is_p = True
    while i * i <= num:
        if num % i == 0:
            is_p = False
            break
        i += 1
    print("Prime" if is_p else "Not prime")

# 11: Sum of digits of given number
num = int(input("Enter number to sum digits (11): "))
s = 0
n_temp = abs(num)
while n_temp > 0:
    s += n_temp % 10
    n_temp //= 10
print(s)

# 12: Check whether entered number is palindrome
num = int(input("Enter number to check palindrome (12): "))
orig = num
rev = 0
n_temp = abs(num)
while n_temp > 0:
    rev = rev * 10 + n_temp % 10
    n_temp //= 10
if rev == abs(orig):
    print("Palindrome")
else:
    print("Not palindrome")
