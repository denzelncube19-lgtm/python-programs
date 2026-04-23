# GCD and LCM Calculator
import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd = math.gcd(a, b)
lcm = abs(a * b) // gcd
print(f"GCD of {a} and {b} = {gcd}")
print(f"LCM of {a} and {b} = {lcm}")
