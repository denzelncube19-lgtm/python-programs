# Number Pattern Printer
n = int(input("Enter number of rows: "))
print("\nPattern 1 - Right Triangle:")
for i in range(1, n+1):
    print(' '.join(str(j) for j in range(1, i+1)))
print("\nPattern 2 - Inverted Triangle:")
for i in range(n, 0, -1):
    print(' '.join(str(j) for j in range(1, i+1)))
