# List Sorting (Bubble Sort)
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(f"Sorted list (Ascending): {arr}")
print(f"Sorted list (Descending): {arr[::-1]}")
