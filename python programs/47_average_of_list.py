# Statistics Calculator
nums = list(map(float, input("Enter numbers separated by spaces: ").split()))
print(f"Count   : {len(nums)}")
print(f"Sum     : {sum(nums)}")
print(f"Average : {sum(nums)/len(nums):.2f}")
print(f"Maximum : {max(nums)}")
print(f"Minimum : {min(nums)}")
sorted_nums = sorted(nums)
n = len(sorted_nums)
mid = n // 2
median = sorted_nums[mid] if n % 2 else (sorted_nums[mid-1] + sorted_nums[mid]) / 2
print(f"Median  : {median}")
