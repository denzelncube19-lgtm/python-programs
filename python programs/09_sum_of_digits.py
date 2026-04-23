# Sum of Digits of a Number
num = input("Enter a number: ")
total = sum(int(d) for d in num if d.isdigit())
print(f"Sum of digits of {num} = {total}")
