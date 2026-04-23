# Lambda, Map, Filter, Reduce
from functools import reduce

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

squared = list(map(lambda x: x**2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
total = reduce(lambda x, y: x + y, nums)

print(f"Original : {nums}")
print(f"Squared  : {squared}")
print(f"Evens    : {evens}")
print(f"Sum (reduce): {total}")
