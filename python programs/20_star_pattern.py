# Star Pattern Printer
n = int(input("Enter number of rows: "))
print("\nRight-angle Triangle:")
for i in range(1, n+1):
    print("* " * i)
print("\nPyramid:")
for i in range(1, n+1):
    print(" " * (n - i) + "* " * i)
