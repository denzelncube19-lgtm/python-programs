# Remove Duplicates from a List (Preserve Order)
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
seen = set()
unique = []
for n in nums:
    if n not in seen:
        unique.append(n)
        seen.add(n)
print(f"Original : {nums}")
print(f"Unique   : {unique}")
