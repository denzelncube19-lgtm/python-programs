# Simple Interest Calculator
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (% per year): "))
time = float(input("Enter time (in years): "))
si = (principal * rate * time) / 100
total = principal + si
print(f"\nSimple Interest: {si:.2f}")
print(f"Total Amount   : {total:.2f}")
