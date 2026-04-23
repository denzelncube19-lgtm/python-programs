# Area Calculator for Different Shapes
import math
print("Area Calculator")
print("1. Circle  2. Rectangle  3. Triangle  4. Square")
choice = input("Choose shape: ")
if choice == '1':
    r = float(input("Enter radius: "))
    print(f"Area of Circle = {math.pi * r**2:.2f}")
elif choice == '2':
    l, w = float(input("Length: ")), float(input("Width: "))
    print(f"Area of Rectangle = {l * w:.2f}")
elif choice == '3':
    b, h = float(input("Base: ")), float(input("Height: "))
    print(f"Area of Triangle = {0.5 * b * h:.2f}")
elif choice == '4':
    s = float(input("Side: "))
    print(f"Area of Square = {s**2:.2f}")
