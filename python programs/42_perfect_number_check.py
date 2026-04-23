# Perfect Number Checker
num = int(input("Enter a number: "))
divisors = [i for i in range(1, num) if num % i == 0]
if sum(divisors) == num:
    print(f"{num} is a PERFECT number")
    print(f"Divisors: {divisors}")
else:
    print(f"{num} is NOT a perfect number")
