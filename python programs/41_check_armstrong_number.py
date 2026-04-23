# Armstrong Number Checker
num = int(input("Enter a number: "))
digits = str(num)
n = len(digits)
total = sum(int(d)**n for d in digits)
if total == num:
    print(f"{num} is an ARMSTRONG number")
else:
    print(f"{num} is NOT an Armstrong number")
