# Number System Converter
print("Number System Converter")
print("1. Decimal to Binary  2. Decimal to Octal  3. Binary to Decimal  4. Octal to Decimal")
ch = input("Choose: ")
if ch == '1':
    n = int(input("Decimal: "))
    print(f"Binary: {bin(n)[2:]}")
elif ch == '2':
    n = int(input("Decimal: "))
    print(f"Octal: {oct(n)[2:]}")
elif ch == '3':
    b = input("Binary: ")
    print(f"Decimal: {int(b, 2)}")
elif ch == '4':
    o = input("Octal: ")
    print(f"Decimal: {int(o, 8)}")
