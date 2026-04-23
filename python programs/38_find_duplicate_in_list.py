# Find Duplicates in a List
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
seen = set()
duplicates = set()
for n in nums:
    if n in seen:
        duplicates.add(n)
    seen.add(n)
if duplicates:
    print(f"Duplicates found: {sorted(duplicates)}")
else:
    print("No duplicates found.")
