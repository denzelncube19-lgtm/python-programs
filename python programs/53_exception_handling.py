# Exception Handling Demo
print("Exception Handling Examples")

# Division by zero
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(f"Result: {a / b}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter integers.")
finally:
    print("Division operation complete.")

# File not found
try:
    with open("nonexistent.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found!")
