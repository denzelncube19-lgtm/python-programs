# Sum of Even and Odd Numbers in a List
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
evens = [n for n in nums if n % 2 == 0]
odds  = [n for n in nums if n % 2 != 0]
print(f"Even numbers: {evens}  -> Sum = {sum(evens)}")
print(f"Odd numbers : {odds}   -> Sum = {sum(odds)}")
