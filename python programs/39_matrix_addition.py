# Matrix Addition (2x2)
print("Enter Matrix A (2x2):")
A = [[int(input(f"A[{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]
print("Enter Matrix B (2x2):")
B = [[int(input(f"B[{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]
C = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
print("\nResult (A + B):")
for row in C:
    print(row)
