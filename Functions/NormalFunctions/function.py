def sum(a,b):
    return a+b

print(sum(2,3))


def greet(msg):
    return "hello " + msg

print(greet("tejas"))


def square(n):
    return n*n

print(square(5))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))