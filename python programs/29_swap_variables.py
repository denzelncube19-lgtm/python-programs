# Swap Two Variables (3 Methods)
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print(f"\nBefore swap: a={a}, b={b}")

# Method 1: Using temp variable
temp = a; a = b; b = temp
print(f"After swap (temp): a={a}, b={b}")

# Method 2: Without temp (arithmetic)
a = a + b; b = a - b; a = a - b
print(f"After swap (math): a={a}, b={b}")

# Method 3: Python tuple swap
a, b = b, a
print(f"After swap (tuple): a={a}, b={b}")
