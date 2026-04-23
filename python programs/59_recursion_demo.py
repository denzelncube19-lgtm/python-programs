# Recursion Examples
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} = {factorial(num)}")
print(f"Fibonacci  of {num} = {fibonacci(num)}")
b, e = int(input("Base: ")), int(input("Exponent: "))
print(f"{b}^{e} = {power(b, e)}")
